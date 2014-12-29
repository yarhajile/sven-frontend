function updateAction( element )
{
    var parameter = $( element ).attr( 'name' ).replace( 'input_', '' );

    var requestData = {
        'location_group_id' : $( '#location_group_id').val( ),
        'parameter'         : parameter,
        'value'             : $( element ).val( )
    }

    if ( $( element ).attr( 'name' ) == current_parameter_name && requestData.value == current_parameter_value )
    {
        // No need to trouble the server if all we are doing is performing a blur or keyup on unchanged values
        return false;
    }

    $.post(
        '/monitor/ajaxUpdateLocationGroup',
        requestData,
        function( responseData ) {
            if ( responseData.success == true )
            {
                if ( requestData.parameter == 'name' )
                {
                    $( '#location_group_name').html( requestData.value )
                }
            }
            else
            {
                alert( responseData.message );
            }
        }
    );
}

$( function( ) {
    $( '#table_data_container').load( '/monitor/ajaxListLocations', { 'location_group_id' : $( '#location_group_id').val( ) } );


    /*
     * Set active state for locations
     */
    $( '#table_data_container' ).on( 'click', '.location_active_state', function ( ) {
        var requestData = {
            'location_id'     : $( this ).attr( 'rel' ),
            'parameter'     : 'active',
            'value'         : $( this ).val( )
        }

        $.post( '/monitor/ajaxUpdateLocation', requestData );
    });


    /*
     * Checkbox "With Selected" actions
     */
    $( '#table_data_container').on( 'click', '#actions_submit', function( ) {
        var id_list = [];

        $( '#table_data_container table tbody tr' ).find( 'input[type=checkbox]:checked').each( function( ) {
            id_list.push( $( this ).val( ) );
        } );

        var action = $( '#group_actions').val( );

        var data = {
            'action'                : action,
            'id_list'               : id_list,
            'location_group_id'     : $( '#location_group_id').val( )
        }

        $( '#table_data_container').load( '/monitor/ajaxListLocations', data );

        return false;
    } );
} );