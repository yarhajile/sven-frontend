function updateAction(element) {
  var parameter = $(element).attr('name').replace('input_', '');

  var requestData = {
    'device_id': $('#device_id').val(),
    'location_id': $('#location_id').val(),
    'parameter': parameter,
    'value': $(element).val(),
    'moduleListing': {}
  }

  if (moduleListing != {}) {
    requestData['moduleListing'] = JSON.stringify(getModulesForSelectedInterface());
  }

  if ($(element).attr('name') == current_parameter_name && requestData.value == current_parameter_value) {
    // No need to trouble the server if all we are doing is performing a blur or keyup on unchanged values
    return false;
  }

  $.post(
      '/monitor/ajaxUpdateDevice',
      requestData,
      function (responseData) {
        if (responseData.success == true) {
          if (requestData.parameter == 'name') {
            $('#device_name').html(requestData.value)
          }

          // Set the device_id since this is multi-purpose add / edit function
          $('#device_id').val(responseData.data.device_id);
          $('#device_progress').setProgressValue(responseData.data.percentage_complete);
          $('#percentage_complete_text').html(responseData.data.percentage_complete);

          if (parseInt(responseData.data.percentage_complete) == 100) {
            // Notify the back-end that we can dispatch this module now, if it hasn't already done so.
            var formElements = {}

            $.each($('#input_form').serializeArray(), function () {
              formElements[this.name] = this.value;
            });

            wsw.send(JSON.stringify({ 'action': 'DispatchModule', 'parameters': formElements }));
          }
        }
        else {
          alert(responseData.message);
        }
      }
  );
}

moduleListing = []

$(function () {
  $('body').on('change', 'select[name=input_interface]', function () {
    // load input_bus values
    $('select[name=input_bus]').empty().append('<option selected>Choose a bus</option>');

    $.each(moduleListing[ $(this).val() ]['modules'], function (moduleKey, moduleValue) {
      $('select[name=input_bus]').append('<option value="' + moduleValue.module + '">' + moduleValue.meta.name + '</option>');
    });

    $('select[name=input_bus]').trigger('silent-change');

    $('#bus-selection').show();
    $('#bus-components').html('')
  });

  $('body').on('change', 'select[name=input_bus]', function () {
    $('#bus-components').load('/monitor/ajaxInputMatrix', { 'interface': $('select[name=input_interface]').val(), 'bus': $(this).val(), 'device_id': $('#device_id').val(), 'moduleListing': JSON.stringify(getModulesForSelectedInterface()) });
    $('#bus-selection').show();
  });

  // Show the status of the devices completion
  $('#device_progress').progress(
      {
        size: '100%',
        value: $('#percentage_complete').val(),
        innerMarksOverBar: true,
        bottomMarks: [
          { value: 0, label: 'Nope' },
          { value: 25, label: 'Go on' },
          { value: 50, label: 'Better' },
          { value: 75, label: 'Almost' },
          { value: 100, label: 'Done!' }
        ],
        topMarks: 25,
        topLabel: '[value]%'
      }
  );

  $('body').on('click', '#testDeviceCallback', function () {
    wsw.send(JSON.stringify({ 'action': 'callback', 'device_id': $('#device_id').val() }));
  });

  // Populate list of available interfaces and their modules
  wsw.send(JSON.stringify({ 'action': 'ModuleListing', 'callback': 'PopulateModuleListing' }));
});

function getModulesForSelectedInterface() {
  var moduleDetailsForInterface = {};

  var interface = $('select[name=input_interface]').val();

  $.each(moduleListing, function (interfaceKey, interfaceValues) {
    if (interface == interfaceKey) {
      $.each(moduleListing[ interface ]['modules'], function (moduleKey, moduleValues) {
        if (moduleValues.module == $('select[name=input_bus]').val()) {
          moduleDetailsForInterface = moduleValues;
        }
      });
    }
  });

  return moduleDetailsForInterface;
}

$('#edit-device-button').click(function () {
  $('#edit-device-container').toggle();
  return false;
});
