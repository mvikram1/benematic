// VIN
var vinElem = document.getElementById('vin');
gm.info.getVehicleConfiguration(function(data) {
  vinElem.innerHTML = gm.info.getVIN();
});


var Formatters = {
    onOff: function(value) {
        return value ? 'On' : 'Off';
    },
    turnSignal: function(value) {
        var values = ['No activation', 'Left', 'Right']
        return values[value];
    }
};



var TelematicsSession = function() {
    // Initialize current values
    this.metrics = {
    };
    

    // Begin current value recorder
    gm.info.watchVehicleData(this.recordData.bind(this), TelematicsSession.METRICS);
    
    // Begin data analysis
    //this.interval = window.setInterval(this.analyzeMetrics, 1000);
}

TelematicsSession.METRICS = {
    'average_speed': 'kph',
    'engine_speed': 'rpm',
    'speed_limit': 'mph',
    
    'accelerator_position': '%',
    'brake_position': '%',
    
    'wheel_angle': 'deg',
    'yaw_rate': 'deg/s',

    'turn_signal': Formatters.turnSignal,
    
    'driver_seatbelt_fastened': Formatters.onOff,
    'passenger_present': Formatters.onOff,
    'passenger_seatbelt_fastened': Formatters.onOff,

    'high_beam_ind': Formatters.onOff
};

TelematicsSession.prototype = {
    recordData: function (data) {
        for (var metric in TelematicsSession.METRICS) {
            var value = data[metric];
            if (value !== undefined) {
                this.metrics[metric] = value;
                this.printMetric(metric, value);
            }
        }
    },

    printMetric: function(metric, value) {
        var modifier = TelematicsSession.METRICS[metric];
        if (typeof modifier === 'function') {
            displayValue = modifier(value);
        } else {
            displayValue = '' + value + ' ' + modifier;
        }

        var el = document.getElementById(metric);
        if (el) {
            el.innerHTML = value;
        } else {
            el = document.getElementById('metrics');
            el.innerHTML += '<dt>' + metric + '</dt><dd id="' + metric + '">' + displayValue + '</dd>';
        }
    },

    analyzeMetrics: function() {
        document.getElementById('time').innerHTML = (new Date()).toString();
    }
};


var session = new TelematicsSession();
