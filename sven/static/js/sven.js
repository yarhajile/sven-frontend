var output_actions;
var module_listing = []
var module_factory_status;

var SvenWSCallbacks = {
  'core': {
    'ArmedStatus': function(data) {
    }
  },
  'setGlobalOutputActions': function(data) {
    output_actions = data;
  },
  'setGlobalModuleListing': function(data) {
    module_listing = data;

    // There's probably a much more elegant solution for this, but this allows
    // any page to listen for updates to the websocket callbacks through a
    // pseudo dummy input field.
    $('.global_module_listing').change();
  },
  'moduleFactoryStatus' : function(data) {
    module_factory_status = data;
    $('.module_factory_status').change();
  }
}

function WSWrapper() {
  if ("WebSocket" in window) {
    var ws = new WebSocket("ws://10.0.1.35:7654/");
    var self = this;

    ws.onopen = function () {
      console.log("Opening new WebSocket connection...");
      window.identified = false;
    }

    ws.onclose = function (e) {
      // Re-connect if the other end killed us.
      setTimeout(function () {
        console.warn("WebSocket connection closed, attempting to re-connect...");
        wsw = new WSWrapper();
      }, 1000);
    }

    ws.onmessage = function (e) {
      wsMessage = $.parseJSON(e.data);

      console.info(wsMessage);

      if (wsMessage.callback) {
        eval('SvenWSCallbacks.' + wsMessage.callback + '(' + JSON.stringify(wsMessage.data) + ')');
      }
      else {
        console.warn('No callback for WebSocket data...')
        console.log(wsMessage);
      }
    }

    ws.onerror = function (e) {
      console.error(e.data);
    }

    this.send = function (message, callback) {
      this.waitForConnection(function () {
        console.info('Sending ' + message);

        ws.send(message);

        if (typeof callback !== 'undefined') {
          callback();
        }
      }, 1000);
    }

    this.waitForConnection = function (callback, interval) {
      if (ws.readyState === 1) {
        callback();
      }
      else {
        var that = this;

        setTimeout(function () {
          console.info('Waiting ' + interval + 'ms for connection...');

          that.waitForConnection(callback, interval);
        }, interval);
      }
    }
  }
}

var wsw = new WSWrapper();


$(function() {
  wsw.send(JSON.stringify({ 'action': 'OutputActions', 'callback': 'setGlobalOutputActions' }));

  // Populate list of available interfaces and their modules
  wsw.send(JSON.stringify({ 'action': 'ModuleListing', 'callback': 'setGlobalModuleListing' }));

  // Populate list of available interfaces and their modules
  wsw.send(JSON.stringify({ 'action': 'ModuleFactoryStatus', 'callback': 'moduleFactoryStatus' }));

  $('.module_factory_status').change(function(){
    // Finally, build out our widgets.
    $('#sven-widgets').load('/monitor/ajaxLoadWidgets', {'data' : JSON.stringify(module_factory_status)});
  });
});
