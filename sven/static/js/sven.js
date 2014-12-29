var output_actions;

var SvenWSCallbacks = {
  'core': {
    'ArmedStatus': function(data) {
      console.log(data);
    }
  },
  'RCSwitchTriggered': function(data) {
    $('#eventCounter').html(parseInt($('#eventCounter').html()) + 1);
    console.info(data);
  },
  'setGlobalOutputActions': function(data) {
    output_actions = data;
    console.log(data);

    // Finally, build out our widgets.
    $('#sven-widgets').load('/monitor/ajaxLoadWidgets', {'data' : JSON.stringify(data)});
  }
}

function WSWrapper() {
  if ("WebSocket" in window) {
    var ws = new WebSocket("ws://10.0.0.222:7654/");
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
})