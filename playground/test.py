#!/usr/bin/python

class Meta( object ):
    meta = {}

    def __init__( self, *args, **kwargs ):
        if args:
            # args[0] *should* be a dict of meta values
            for key, value in args[0].items():

                self.meta[key] = value
        else:
            self.meta = kwargs

    def __getattr__(self, name):
        return self.meta.get( name, None )


    def __setattr__( self, name, value ):
        self.meta[name] = value


    def __getitem__( self, name ):
        return self.meta.get( name, None)

    def __str__( self ):
        return self.meta




class Outer( object ):

    def __init__( self ):
        print "Outer constructor"

    class action_testing( object ):
        self.meta = Meta( { 'name' : 'Yay!', 'description' : 'something' } )

        def __init__( self, outer ):
            print "Uh oh 1"
            pass


    class action_testing2( object ):
#        meta = DeviceActionMeta( name = 'Yay!', description = 'blah2' )

        def __init__( self, outer ):
            self.meta = Meta( { 'name' : 'Yay2!', 'description' : 'something2' } )
            print "uh oh 2"

#    def run( self ):
#        getattr( self, 'action_testing' )( self, 'Inner attribute got through!' )


obj = Outer()

#obj.run( )

one = obj.action_testing( obj )
print one.meta.name

two = obj.action_testing2( obj )
print two.meta.name

something = { { 'user_alert_dialog' : {
'604854' : { '$version' : -725645354, 'dialog_id' : 'confirm-pairing', 'dialog_data' : '',
             '$timestamp' : 1389479057121L } }, 'user_settings' : {
'604854' : { 'lang' : 'en_US', 'tos_current_version' : 1381190400000L, 'tos_accepted_version' : 1381190400000L,
             'tos_minimum_version' : 1381190400000L, 'receive_marketing_emails' : True, 'receive_nest_emails' : True,
             'email_verified' : True, 'max_thermostats' : 10, 'max_smoke_detectors' : 36,
             'max_thermostats_per_structure' : 10, 'max_structures' : 2, 'max_smoke_detectors_per_structure' : 18,
             '$version' : -1006688034, '$timestamp' : 1389478538295L, 'receive_support_emails' : True } },
                'schedule' : { '02AA01AC371305HK' : { 'ver' : 2, 'name' : 'Nest Current Schedule', 'days' : { '1' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 19.756, 'entry_type' : 'setpoint', 'touched_at' : 1398714225,
                        'time' : 25200, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'continuation', 'touched_at' : 1403680846,
                        'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'setpoint', 'touched_at' : 1395419345,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '0' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 19.756, 'entry_type' : 'setpoint', 'touched_at' : 1398714227,
                        'time' : 25200, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.179, 'entry_type' : 'continuation',
                        'touched_at' : 1403680846, 'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'setpoint', 'touched_at' : 1398714192,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '3' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 19.756, 'entry_type' : 'setpoint', 'touched_at' : 1398714220,
                        'time' : 25200, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'continuation', 'touched_at' : 1403680846,
                        'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'setpoint', 'touched_at' : 1395419342,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '2' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 19.913, 'entry_type' : 'setpoint', 'touched_at' : 1398714223,
                        'time' : 25200, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'continuation', 'touched_at' : 1403680846,
                        'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'setpoint', 'touched_at' : 1398714189,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '5' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 20.0, 'entry_type' : 'setpoint', 'touched_at' : 1398714181,
                        'time' : 30600, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'continuation', 'touched_at' : 1403680846,
                        'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.179, 'entry_type' : 'setpoint', 'touched_at' : 1395419289,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '4' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 19.756, 'entry_type' : 'setpoint', 'touched_at' : 1398714217,
                        'time' : 25200, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'continuation', 'touched_at' : 1403680846,
                        'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.0, 'entry_type' : 'setpoint', 'touched_at' : 1395419333,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } }, '6' : {
                '1' : { 'touched_tzo' : -25200, 'temp' : 20.0, 'entry_type' : 'setpoint', 'touched_at' : 1398714184,
                        'time' : 30600, 'touched_by' : 4, 'type' : 'HEAT' },
                '0' : { 'touched_tzo' : -25200, 'temp' : 10.179, 'entry_type' : 'continuation',
                        'touched_at' : 1403680846, 'time' : 0, 'touched_by' : 1, 'type' : 'HEAT' },
                '2' : { 'touched_tzo' : -25200, 'temp' : 10.179, 'entry_type' : 'setpoint', 'touched_at' : 1395419293,
                        'time' : 76500, 'touched_by' : 4, 'type' : 'HEAT' } } }, 'schedule_mode' : 'HEAT',
                                                      '$version' : -1669087572, '$timestamp' : 1403680847199L } },
                'track' : { '02AA01AC371305HK' : { '$version' : -1095824635, 'last_ip' : '97.114.117.134',
                                                   'last_connection' : 1403707772278L, '$timestamp' : 1403707772278L,
                                                   'online' : True } }, 'user' : {
'604854' : { '$version' : -348516181, 'structures' : [ 'structure.dbd0c390-7b0d-11e3-9da1-12313b0281cc' ],
             'email' : 'elijahe@gmail.com', '$timestamp' : 1389478520396L, 'name' : 'elijahe@gmail.com' } },
                'demand_response' : { '02AA01AC371305HK' : { '$version' : -1, '$timestamp' : 1 } },
                'device_alert_dialog' : {
                '02AA01AC371305HK' : { '$version' : 43157518, 'dialog_id' : 'confirm-pairing', 'dialog_data' : '',
                                       '$timestamp' : 1389479057121L } }, 'link' : {
'02AA01AC371305HK' : { '$version' : -1104391926, 'structure' : 'structure.dbd0c390-7b0d-11e3-9da1-12313b0281cc',
                       '$timestamp' : 1389479057121L } },
                'message_center' : { '604854' : { '$version' : -1, 'messages' : [ ], '$timestamp' : 1325379661000L } },
                'tuneups' : { '02AA01AC371305HK' : { '$version' : -1, '$timestamp' : 1 } }, 'device' : {
'02AA01AC371305HK' : { 'heat_pump_comp_threshold' : -31.5, 'backplate_model' : 'Backplate-2.7',
                       'gear_threshold_low' : 0.0, 'lower_safety_temp_enabled' : True, 'postal_code' : '99208',
                       'learning_mode' : True, 'country_code' : 'US', 'star_type' : 'unknown', 'heat_x3_source' : 'gas',
                       'fan_timer_duration' : 1800, 'backplate_serial_number' : '02BA02AC381300UR',
                       'hvac_wires' : 'Heat,Cool,Fan,Common Wire,Rh', 'humidifier_type' : 'unknown',
                       'sunlight_correction_active' : False, 'logging_priority' : 'informational',
                       'temperature_lock' : False, 'auto_away_reset' : False, 'dual_fuel_breakpoint_override' : 'none',
                       'has_x3_heat' : False, 'cooling_x2_delivery' : 'unknown',
                       'maint_band_lower' : 0.39000000000000001, 'device_locale' : 'en_US', 'learning_time' : 1246,
                       'has_fan' : True, 'pin_rh_description' : 'power', 'has_x2_alt_heat' : False,
                       'leaf_away_high' : 28.879999999999999, 'heat_x2_source' : 'gas', 'aux_heat_source' : 'electric',
                       'filter_changed_date' : 0, 'equipment_type' : 'electric',
                       'dehumidifier_orientation_selected' : 'unknown', 'forced_air' : True, 'aux_lockout_leaf' : 10.0,
                       'filter_reminder_level' : 0, 'humidifier_state' : False, 'error_code' : '',
                       'switch_system_off' : False, 'has_x2_cool' : False, 'serial_number' : '02AA01AC371305HK',
                       'hvac_pins' : 'W1,Y1,C,Rh,G', 'fan_cooling_enabled' : True,
                       'heat_pump_comp_threshold_enabled' : False, 'pin_star_description' : 'none',
                       'sunlight_correction_enabled' : True, 'learning_days_completed_cool' : 0,
                       'away_temperature_low_enabled' : True, 'note_codes' : [ ],
                       'leaf_threshold_heat' : 18.803000000000001, 'y2_type' : 'unknown', 'leaf' : False,
                       'auto_dehum_enabled' : False, 'alt_heat_x2_source' : 'gas', 'has_humidifier' : False,
                       'gear_threshold_high' : 0.0, 'current_schedule_mode' : 'HEAT', 'backplate_bsl_info' : 'BSL',
                       'fan_cooling_readiness' : 'not ready', 'battery_level' : 3.9180000000000001,
                       'humidity_control_lockout_end_time' : 0, 'ob_persistence' : True,
                       'hvac_safety_shutoff_active' : False, 'schedule_learning_reset' : False,
                       'pin_y2_description' : 'none', 'is_on_stand' : False, 'emer_heat_source' : 'electric',
                       'filter_reminder_enabled' : False, 'compressor_lockout_leaf' : -17.800000000000001,
                       '$version' : -238409442, 'aux_heat_delivery' : 'forced-air',
                       'away_temperature_high' : 24.443999999999999, 'fan_duty_start_time' : 0,
                       'learning_days_completed_range' : 0, 'target_humidity_enabled' : False,
                       'leaf_threshold_cool' : 0.0, 'sunlight_correction_ready' : True, 'fan_timer_timeout' : 0,
                       'has_dual_fuel' : False, 'safety_temp_activating_hvac' : False, 'dual_fuel_selected' : False,
                       'heatpump_setback_active' : False, 'has_heat_pump' : False, 'fan_control_state' : False,
                       'model_version' : 'Display-2.8', 'has_aux_heat' : False, 'current_version' : '4.2.3',
                       'away_temperature_high_enabled' : False, 'alt_heat_delivery' : 'forced-air',
                       'current_humidity' : 44, 'target_humidity' : 35.0, 'upper_safety_temp' : 35.0,
                       'heater_delivery' : 'forced-air', 'preconditioning_ready' : True,
                       'backplate_mono_version' : '4.0.21', 'has_fossil_fuel' : True, 'mac_address' : '18b4300bbaef',
                       'cooling_source' : 'electric', 'type' : 'TBD', 'lower_safety_temp' : 4.444,
                       'emer_heat_delivery' : 'forced-air', 'humidity_control_lockout_start_time' : 0,
                       'creation_time' : 1389478233615L, 'fan_mode' : 'auto', 'filter_changed_set_date' : 0,
                       'range_enable' : True, 'heatpump_savings' : 'off', 'radiant_control_enabled' : False,
                       'temperature_lock_low_temp' : 20.0, 'where_id' : '00000000-0000-0000-0000-000100000006',
                       'pin_ob_description' : 'none', 'alt_heat_x2_delivery' : 'forced-air',
                       'humidity_control_lockout_enabled' : False, 'fan_duty_cycle' : 3600, 'heatpump_ready' : False,
                       'preconditioning_enabled' : False, 'target_time_confidence' : 0.0, 'click_sound' : 'on',
                       'pin_w1_description' : 'heat', 'has_air_filter' : True, 'auto_dehum_state' : False,
                       'cooling_x2_source' : 'electric', 'temperature_lock_high_temp' : 22.222000000000001,
                       'heat_pump_aux_threshold' : 10.0, 'rssi' : 67.0, 'has_emer_heat' : False, 'has_alt_heat' : False,
                       'leaf_schedule_delta' : 1.1100000000000001, 'backplate_bsl_version' : '2.1',
                       'user_brightness' : 'medium', 'preconditioning_active' : False, 'pin_w2aux_description' : 'none',
                       'pin_rc_description' : 'none', 'has_dehumidifier' : False,
                       'maint_band_upper' : 0.39000000000000001, 'leaf_learning' : 'ready',
                       'pin_y1_description' : 'cool', 'capability_level' : 4.0,
                       'available_locales' : 'en_US,fr_CA,es_US,en_GB', 'dehumidifier_state' : False,
                       'dehumidifier_type' : 'unknown', 'nlclient_state' : '', 'upper_safety_temp_enabled' : False,
                       'learning_state' : 'slow', 'time_to_target_training' : 'training', 'fan_cooling_state' : False,
                       'fan_duty_end_time' : 0, 'alt_heat_source' : 'gas', '$timestamp' : 1403706757405L,
                       'heat_link_connection' : 0, 'temperature_lock_pin_hash' : '', 'cooling_delivery' : 'unknown',
                       'heat_pump_aux_threshold_enabled' : True, 'leaf_away_low' : 10.0,
                       'heat_x3_delivery' : 'forced-air', 'ob_orientation' : 'O', 'touched_by' : { },
                       'temperature_scale' : 'F', 'emer_heat_enable' : False,
                       'backplate_mono_info' : 'TFE (BP_D2) 4.0.21 (root@bamboo) 2014-05-02 16:54:17',
                       'auto_away_enable' : True, 'pin_g_description' : 'fan', 'local_ip' : '10.0.0.124',
                       'has_x2_heat' : False, 'away_temperature_low' : 10.0, 'time_to_target' : 0,
                       'heat_x2_delivery' : 'forced-air', 'learning_days_completed_heat' : 165,
                       'dual_fuel_breakpoint' : -1.0, 'heater_source' : 'gas', 'pin_c_description' : 'power' } },
                'shared' : { '02AA01AC371305HK' : { 'hvac_ac_state' : False, 'compressor_lockout_timeout' : 0,
                                                    'hvac_alt_heat_x2_state' : False,
                                                    'compressor_lockout_enabled' : False, 'target_temperature' : 19.913,
                                                    'auto_away' : 0, 'can_heat' : True, 'hvac_aux_heater_state' : False,
                                                    'target_change_pending' : False, 'hvac_heat_x2_state' : False,
                                                    'target_temperature_low' : 20.0, 'target_temperature_high' : 24.0,
                                                    'hvac_heat_x3_state' : False, 'hvac_cool_x2_state' : False,
                                                    '$timestamp' : 1403704882380L, 'hvac_heater_state' : False,
                                                    'auto_away_learning' : 'ready', 'target_temperature_type' : 'heat',
                                                    'touched_by' : { }, 'name' : 'Nest', 'can_cool' : True,
                                                    'hvac_fan_state' : False, '$version' : -1132907975,
                                                    'current_temperature' : 21.84, 'hvac_emer_heat_state' : False,
                                                    'hvac_alt_heat_state' : False } },
                'message' : { '02AA01AC371305HK' : { '$version' : 837225278, '$timestamp' : 1389479071341L } },
                'metadata' : {
                '02AA01AC371305HK' : { '$version' : -1, 'last_ip' : '127.0.0.1', 'last_connection' : 1356998400000L,
                                       '$timestamp' : 1356998400000L } }, 'where' : {
'dbd0c390-7b0d-11e3-9da1-12313b0281cc' : { '$version' : -169651312, 'wheres' : [
    { 'where_id' : '00000000-0000-0000-0000-000100000001', 'name' : 'Basement' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000d', 'name' : 'Bedroom' },
    { 'where_id' : '00000000-0000-0000-0000-000100000003', 'name' : 'Den' },
    { 'where_id' : '00000000-0000-0000-0000-000100000010', 'name' : 'Dining Room' },
    { 'where_id' : '00000000-0000-0000-0000-000100000006', 'name' : 'Downstairs' },
    { 'where_id' : '00000000-0000-0000-0000-000100000000', 'name' : 'Entryway' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000b', 'name' : 'Family Room' },
    { 'where_id' : '00000000-0000-0000-0000-000100000002', 'name' : 'Hallway' },
    { 'where_id' : '00000000-0000-0000-0000-000100000008', 'name' : 'Kids Room' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000a', 'name' : 'Kitchen' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000c', 'name' : 'Living Room' },
    { 'where_id' : '00000000-0000-0000-0000-000100000005', 'name' : 'Master Bedroom' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000e', 'name' : 'Office' },
    { 'where_id' : '00000000-0000-0000-0000-00010000000f', 'name' : 'Upstairs' } ], '$timestamp' : 1389478520396L } },
                'structure' : {
                'dbd0c390-7b0d-11e3-9da1-12313b0281cc' : { 'num_thermostats' : 'unknown', 'away_timestamp' : 1389737117,
                                                           'touched_by' : { }, 'name' : '',
                                                           'hvac_safety_shutoff_enabled' : True,
                                                           'swarm' : [ 'device.02AA01AC371305HK' ], 'away' : False,
                                                           'creation_time' : 1389478520396L,
                                                           'devices' : [ 'device.02AA01AC371305HK' ],
                                                           'topaz_enhanced_auto_away_enabled' : False,
                                                           'renovation_date' : 'unknown', 'fabric_ids' : [ ],
                                                           'postal_code' : '99208', 'user' : 'user.604854',
                                                           'country_code' : 'US', '$version' : -759499338,
                                                           'house_type' : 'family', 'dr_reminder_enabled' : True,
                                                           'away_setter' : 1, '$timestamp' : 1403381910458L } },
                'utility' : { 'dbd0c390-7b0d-11e3-9da1-12313b0281cc' : { '$version' : -1, '$timestamp' : 1 } } }