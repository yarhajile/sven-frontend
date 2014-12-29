function updateAction(element) {
  return false;
}

$(function () {
  $('#table_data_container').load('/monitor/ajaxListLocationGroups');

  //Add new location group" button action
  $('#new_location_group_add').on('click', function () {
    $('#new_location_group_input').show(300);
    $(this).hide(300);
    return false;
  });

  // Close / Cancel the add new location group window
  $('#new_location_group_cancel, #new_location_group_input > .close').on('click', function () {
    $('#new_location_group_add').show(300);
    $('#new_location_group_input').hide(300);
    return false;
  });

  // Set active state for location groups
  $('#table_data_container').on('click touchend', '.location_group_active_state', function () {
    var requestData = {
      'location_group_id': $(this).attr('rel'),
      'parameter': 'active',
      'value': $(this).val()
    }

    $.post('/monitor/ajaxUpdateLocationGroup', requestData);
  });

  // Saving a new location group
  $('#new_location_group_save').on('click', function () {
    if ($("#input_form").validationEngine('validate') == true) {
      var data = {
        'action': 'new',
        'name': $('input[name=location_group_name]').val(),
        'active': $('input:radio[name=location_group_active]').val(),
        'description': $('textarea[name=location_group_description]').val()
      }

      $('#new_location_group_add').show(300);
      $('#new_location_group_input').hide(300);

      $('#table_data_container').load('/monitor/ajaxListLocationGroups', data);
    }

    return false;
  });

  // Checkbox "With Selected" actions
  $('#table_data_container').on('click', '#actions_submit', function () {
    var id_list = [];

    $('#table_data_container table tbody tr').find('input[type=checkbox]:checked').each(function () {
      id_list.push($(this).val());
    });

    var action = $('#group_actions').val();

    var data = {
      'action': action,
      'id_list': id_list,
      'location_group_id': $('#location_group_id').val()
    }

    $('#table_data_container').load('/monitor/ajaxListLocationGroups', data);

    return false;
  });
});