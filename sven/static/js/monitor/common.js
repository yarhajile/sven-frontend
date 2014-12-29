var current_parameter_name = '';
var current_parameter_value = '';

var delay = (function () {
  var timer = 0;

  return function (callback, ms) {
    clearTimeout(timer);

    timer = setTimeout(callback, ms);
  };
})();

$(function () {
  //Activate the validation engine on #input_form
  $("#input_form").validationEngine({ scroll: false });

  //Input changes
  $('body').on('change', '#input_form input, #input_form textarea, #input_form select', function (event) {
    var attr = $(this).attr('name');

    if (typeof attr !== typeof undefined && attr !== false) {
      updateAction($(this));
    }
  });

  //Check all rows on page
  $('#table-data-container').on('click', '#check-all', function () {
    $('table.table tbody').find(':checkbox').prop('checked', this.checked);
  });
});