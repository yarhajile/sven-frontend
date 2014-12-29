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

  $('#input_form input, #input_form textarea, #input_form select')
      .bind('blur keyup click change', function (event) {
    var that = this

    if (event.type == 'blur') {
      updateAction($(that));
    }
    else if (event.type == 'keyup' || event.type == 'change') {
      delay(function () {
        updateAction($(that));
      }, 300);
    }
    /*
     else if ( event.type == 'click' )
     {
     current_parameter_name    = $( this ).attr( 'name' );
     current_parameter_value   = $( this ).val( );
     }
     */
  });

  /*
   * Check all rows on page
   */
  $('#table_data_container').on('click', '#check-all', function () {
    $('table.table tbody').find(':checkbox').prop('checked', this.checked);
  });
});