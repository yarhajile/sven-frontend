import os
#import json

import time
import string
import logging
import traceback
import simplejson as json

from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django import template
from models import *

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def template_exists(template_name):
  try:
    template.loader.get_template(template_name)
    return "Template exists"
  except template.TemplateDoesNotExist:
    return "Template doesn't exist"


def svenCommonData(request):
  data = {
    'base_url': request.build_absolute_uri('/')[:-1],
    'menu_items': Location_Group.objects.all().prefetch_related()
  }

  return data


def svenCommonAjaxData(request):
  data = {
    'success': True,
    'message': None,
    'data': {},
    'base_url': request.build_absolute_uri('/')[:-1]
  }

  return data


@csrf_exempt
def index(request):
  return render(request, 'monitor/index.html', svenCommonData(request))


@csrf_exempt
def locationGroups(request):
  return render(request, 'monitor/locationGroups.html', svenCommonData(request))


@csrf_exempt
def locationGroup(request, id):
  location_group = Location_Group.objects.prefetch_related('location_set')\
    .get(pk = id)

  request.session['location_group_id'] = id

  data = svenCommonData(request)
  data['location_group'] = location_group

  return render(request, 'monitor/locationGroup.html', data)


@csrf_exempt
def location(request, id = 'new'):
  location = None

  location_group = Location_Group.objects.get(
    pk = request.session['location_group_id'])

  if id != 'new' and int(id) > 0:
    #
    # Edit operation
    #
    request.session['location_id'] = id
    location = Location.objects.get(pk = id)
#    print location.location_group_id
  elif id != 'new':
    #
    # We can't be here without a location group
    #
    raise Http404()

  data = svenCommonData(request)
  data['location'] = location
  data['location_group'] = location_group

  return render(request, 'monitor/location.html', data)


@csrf_exempt
def device(request, id = 'new'):
  data = svenCommonData(request)

  device = None
  location = Location.objects.get(pk = request.session['location_id'])
  location_group = Location_Group.objects.get(pk = location.location_group_id)

  if id != 'new' and int(id) > 0:
    # Edit operation
    request.session['device_id'] = id
    device = Device.objects.get(pk = id)

    data['device'] = Device.objects.get(pk = id)

    for parameter in Device_Parameter.objects.filter(device = device):
      if parameter.parameter == 'interface':
        data['interface'] = parameter.value

      if parameter.parameter == 'bus':
        data['bus'] = parameter.value

    data['pageTemplate'] = None

    if 'interface' in data and 'bus' in data:
      pageTemplatePath = os.path.abspath(
        os.path.dirname(__file__)) + '/../../templates/monitor/modules/' + data[
                           'interface'] + '/' + data['bus'] + '/index.html'

      if os.path.isfile(pageTemplatePath):
        data['pageTemplate'] = pageTemplatePath

  elif id != 'new':
    # We can't be here without a device id or 'new'
    raise Http404()

  data.update({
    'location_group': location_group,
    'location': location,
  })

  return render(request, 'monitor/device.html', data)


def calculatePercentageComplete(device, module_listing):
  if device is None:
    return 0

  try:
    # calculate the percentage complete
    total = int(len(module_listing[
      'parameters_required'])) + 2 # Remove 2 for 'name' and 'description'
    complete = 0
  except:
    return 0

  logger.info(module_listing['parameters_required'])

  for key in ['name', 'description']:
    if getattr(device, key):
      complete += 1

  try:
    objects = Device_Parameter.objects.filter(
        device = device,
        parameter__in = module_listing['parameters_required'])

    for object in objects:
      if object.value is not None and object.value != '':
        complete += 1
  except:
    pass

  return int(100 * complete / total)


#
# Ajax update methods
#

@csrf_exempt
def ajaxUpdateLocationGroup(request):
  response_data = svenCommonAjaxData(request)

  if request.is_ajax() and request.method == 'POST':
    try:
      p = request.POST['parameter']
      v = request.POST['value']

      if request.POST['location_group_id']:
        # Update
        location_group = Location_Group.objects.get(
          pk = request.POST['location_group_id'])

        if p == 'name':
          location_group.name = v

        if p == 'description':
          location_group.description = v

        if p == 'active':
          location_group.active = True if v == '1' else False

        location_group.save()

      else:
        # Insert
        location_group = Location_Group(
            name = request.POST.get('name', ''),
            description = request.POST.get('description', ''),
            active = request.POST.get('active', 1))
        location_group.save()

      # Set the device_id to pass back in the response.  This has the effect
      # of turning the 'add' form into an 'edit' form after the first save.
      response_data['data']['location_group_id'] = location_group.id

    except KeyError as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

  else:
    response_data['success'] = False
    response_data['message'] = 'Only POST via ajax is supported'

  return HttpResponse(json.dumps(response_data),
                      content_type = "application/json")


@csrf_exempt
def ajaxUpdateLocation(request):
  response_data = svenCommonAjaxData(request)

  if request.is_ajax() and request.method == 'POST':
    try:
      p = request.POST['parameter']
      v = request.POST['value']

      if request.POST['location_id']:
        # Update
        location = Location.objects.get(pk = request.POST['location_id'])

        if p == 'name':
          location.name = v

        if p == 'description':
          location.description = v

        if p == 'active':
          location.active = True if v == '1' else False

        location.save()

      else:
        # Insert
        if not request.POST['location_group_id']:
          raise KeyError(
            "Unable to add new location, location_group_id not passed")

        location_group = Location_Group.objects.get(
          pk = request.POST['location_group_id'])
        location = Location(name = request.POST.get('name', ''),
                            description = request.POST.get('description', ''),
                            active = request.POST.get('active', 1),
                            location_group = locationGroup)
        location.save()

      #
      # Set the device_id to pass back in the response.  This has the effect of turning the 'add' form into an 'edit' form after the first save
      #
      response_data['data']['location_id'] = location.id


    except KeyError as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

  else:
    response_data['success'] = False
    response_data['message'] = 'Only POST via ajax is supported'

  return HttpResponse(json.dumps(response_data),
                      content_type = "application/json")


# @todo This whole method is a fucked up mess.
@csrf_exempt
def ajaxUpdateDevice(request):
  response_data = svenCommonAjaxData(request)

  if request.is_ajax() and request.method == 'POST':
    try:
      p = request.POST['parameter']
      v = request.POST['value']

      if request.POST['device_id']:
        # Update
        device = Device.objects.get(pk = request.POST['device_id'])

        if p == 'name':
          device.name = v

        if p == 'description':
          device.description = v

        if p == 'active':
          device.active = True if v == '1' else False

        device.save()

      else:
        # Insert
        if not request.POST['location_id']:
          raise KeyError("Unable to add new device, location_id not passed")

        device = Device(name = request.POST.get('name', ''),
                        description = request.POST.get('description', ''),
                        active = request.POST.get('active', 1))
        device.save()

        location = Location.objects.get(pk = request.POST['location_id'])
        locationDevice = Location_Device(location = location, device = device)
        locationDevice.save()

      # Set the device_id to pass back in the response.  This has the effect of turning the 'add' form into an 'edit' form after the first save
      response_data['data']['device_id'] = device.id

      if p not in ['name', 'description', 'active']:
        if p == 'interface':
          # wipe all other parameters if the interface is being changed
          Device_Parameter.objects.filter(device = device).delete()

        if p == 'bus':
          # wipe all other parameters, except the interface, if the bus is being changed
          Device_Parameter.objects.filter(device = device).exclude(
            parameter = 'interface').delete()

        try:
          # Update existing parameter values if it exists
          parameter = Device_Parameter.objects.get(parameter = p,
                                                   device = device)
          parameter.value = v
          parameter.save()
        except:
          # Create new parameter since it doesn't exist
          Device_Parameter(parameter = p, value = v, device = device).save()

      response_data['data']['percentage_complete'] = calculatePercentageComplete(
        device, json.loads(request.POST['module_listing']))

    except:
      response_data['success'] = False
      response_data['message'] = traceback.format_exc()

  else:
    response_data['success'] = False
    response_data['message'] = 'Only POST via ajax is supported'

  return HttpResponse(json.dumps(response_data),
                      content_type = "application/json")


#
# Ajax listing methods
#

@csrf_exempt
def ajaxListLocationGroups(request):
  if request.is_ajax():
    response_data = svenCommonAjaxData(request)

    try:
      if request.method == 'POST':
        action = request.POST['action']

        if action in ['new', 'edit']:
          Location_Group(
            name = request.POST['name'],
            description = request.POST['description'],
            active = request.POST['active']
          ).save()

        else:
          id_list = request.POST.getlist('id_list[]')

          for id in id_list:
            location_group = Location_Group.objects.get(pk = id)

            if action == 'delete':
              location_group.delete()
              continue

            elif action == 'duplicate':
              location_group.pk = None
              location_group.id = None

            elif action == 'activate':
              location_group.active = True

            elif action == 'deactivate':
              location_group.active = False

            elif action == 'trash':
              #location.status = 'trash'
              pass

            location_group.save()

    except KeyError as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

    response_data['data']['location_groups'] = Location_Group.objects.all()

    return render_to_response('monitor/locationGroupList.html', response_data,
                              context_instance = RequestContext(request))

  raise Http404


@csrf_exempt
def ajaxListLocations(request):
  if request.is_ajax():
    response_data = svenCommonAjaxData(request)

    try:
      if request.method == 'POST':
        action = request.POST['action']

        if action in ['new', 'edit']:
          Location(
            name = request.POST['name'],
            description = request.POST['description'],
            active = request.POST['active'],
            location_group = Location_Group(
              pk = request.POST['location_group_id'])
          ).save()
        else:
          id_list = request.POST.getlist('id_list[]')

          for id in id_list:
            location = Location.objects.get(pk = id)

            if action == 'delete':
              location.delete()
              continue

            elif action == 'duplicate':
              location.pk = None
              location.id = None

            elif action == 'activate':
              location.active = True

            elif action == 'deactivate':
              location.active = False

            elif action == 'trash':
              #location.status = 'trash'
              pass

            location.save()

    except KeyError as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

    response_data['location_group'] = Location_Group.objects.prefetch_related(
      'location_set').get(pk = request.session['location_group_id'])

    return render_to_response('monitor/locationList.html', response_data,
                              context_instance = RequestContext(request))

  raise Http404


@csrf_exempt
def ajaxListDevices(request):
  if request.is_ajax():
    response_data = svenCommonAjaxData(request)

    try:
      if request.method == 'POST':
        action = request.POST['action']
        id_list = request.POST.getlist('id_list[]')

        for id in id_list:
          device = Device.objects.get(pk = id)

          if action == 'delete':
            device.delete()
            continue

          elif action == 'duplicate':
            device.pk = None
            device.id = None

          elif action == 'activate':
            device.active = True

          elif action == 'deactivate':
            device.active = False

          elif action == 'trash':
            #location.status = 'trash'
            pass

          device.save()

    except KeyError as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

    response_data['location'] = Location.objects.prefetch_related(
      'location_device_set').get(pk = request.session['location_id'])

    return render_to_response('monitor/deviceList.html', response_data,
                              context_instance = RequestContext(request))

  else:
    raise Http404


@csrf_exempt
def ajaxInputMatrix(request):
  if request.is_ajax():
    response_data = svenCommonAjaxData(request)

    try:
      if request.method == 'POST':
        device = Device.objects.prefetch_related().get(
          pk = request.POST['device_id'])
        module_listing = json.loads(request.POST['module_listing'])

        response_data['data']['device'] = device
        response_data['data']['parameters'] = {}

        try:
          for parameter in Device_Parameter.objects.filter(device = device):
            response_data['data']['parameters'][
              parameter.parameter] = parameter.value
        except:
          pass

        logger.info(module_listing)

        if 'interface' in request.POST and 'bus' in request.POST:
          response_data['data']['modules'] = module_listing
          response_data['data']['pct_complete'] = calculatePercentageComplete(
            device, module_listing)
          return render_to_response('monitor/moduleComponents.html',
                                    response_data,
                                    context_instance = RequestContext(request))

    except:
      response_data['success'] = False
      response_data['message'] = traceback.format_exc()

    return render_to_response('monitor/inputMatrix.html', response_data,
                              context_instance = RequestContext(request))
  raise Http404


@csrf_exempt
def ajaxUpdateDeviceAction(request):
  response_data = svenCommonAjaxData(request)

  if request.is_ajax() and request.method == 'POST':
    try:
      json_data = json.loads(request.POST['data'])

      input_device = Device.objects.get(pk = int(json_data['device_id']))

      Input_Device_Callback_Action.objects.filter(
        input_device = input_device).delete()

      for action in json_data['actions']:
        Input_Device_Callback_Action(
          input_device = input_device,
          output_device = Device.objects.get(pk = action['device_id']),
          action = action['action'],
          parameters = json.dumps(action['parameters']),
          conditions = json.dumps(action['conditions'])
        ).save()

    except Exception as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

  else:
    response_data['success'] = False
    response_data['message'] = 'Only POST via ajax is supported.'

  return HttpResponse(json.dumps(response_data),
                      content_type = "application/json")

@csrf_exempt
def ajaxLoadWidgets(request):
  response_data = svenCommonAjaxData(request)
  if request.is_ajax() and request.method == 'POST' and 'data' in request.POST:
    try:
      data = json.loads(request.POST['data'])

      for key, values in data.iteritems():
        interface = key.replace('Sven.Module.', '')
        interface = interface[:interface.find('.')]
        bus = values['meta']['module_name']

        template_location = '%s/%s' % (interface, bus)

        widget_path = '%s/../../templates/monitor/modules/%s/widget.html' \
          % (os.path.dirname(os.path.realpath(__file__)), template_location)

        if os.path.isfile(widget_path):
          key_new = key.replace('.', '_')

          response_data['data'][key_new] = values
          response_data['data'][key_new]['template_location'] = '%s' \
            % template_location

      return render_to_response(
        'monitor/modules/widgets.html',
        response_data,
        context_instance = RequestContext(request))
    except Exception as ex:
      response_data['success'] = False
      response_data['message'] = ex.args[0]

  else:
    response_data['success'] = False
    response_data['message'] = 'Only POST via ajax is supported.'
