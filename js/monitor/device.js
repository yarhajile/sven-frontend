function updateAction( element )
{
    var parameter = $( element ).attr( 'name' ).replace( 'input_', '' );

    var requestData = {
        'device_id'     : $( '#device_id' ).val( ),
        'location_id'   : $( '#location_id' ).val( ),
        'parameter'     : parameter,
        'value'         : $( element ).val( )
    }


    if ( $( element ).attr( 'name' ) == current_parameter_name && requestData.value == current_parameter_value )
    {
        // No need to trouble the server if all we are doing is performing a blur or keyup on unchanged values
        return false;
    }

    $.post(
        '/monitor/ajaxUpdateDevice',
        requestData,
        function( responseData ) {
            if ( responseData.success == true )
            {
                if ( requestData.parameter == 'name' )
                {
                    $( '#device_name').html( requestData.value )
                }
                // Set the device_id since this is multi-purpose add / edit function
                $( '#device_id').val( responseData.data.device_id );

                $( '#device_progress').setProgressValue( responseData.data.percentage_complete );
                $( '#percentage_complete_text').html( responseData.data.percentage_complete );
            }
            else
            {
                alert( responseData.message );
            }
        }
    );
}

$( function( ) {
    //
    // Show the status of the devices completion
    //
    $( '#device_progress' ).progress(
        {
            size: '100%',
            value: $( '#percentage_complete').val( ),
            innerMarksOverBar: true,
            bottomMarks: [ { value: 0, label: 'Nope' }, { value: 25, label: 'Go on' }, { value: 50, label: 'Better' }, { value: 75, label: 'Almost' }, { value: 100, label: 'Done!' }],
            topMarks: 25,
            topLabel: '[value]%',
        }
    );

    $( 'body').on( 'click', '#testDeviceCallback', function() {
        wsw.send( JSON.stringify( { 'action' : 'callback', 'device_id' : $( '#device_id').val() } ) );
    } );
} );