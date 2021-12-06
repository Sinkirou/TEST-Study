var BASE_DEVICE_WIDTH = 750;
var isIOS = navigator.userAgent.match("iPhone");
var deviceWidth = window.screen.width || 375;
var deviceDPR = window.devicePixelRatio || 2;

function checkDeviceWidth() {
    var newDeviceWidth = window.screen.width || 375
    var newDeviceDPR = window.devicePixelRatio || 2
    const newDeviceHeight = window.screen.height || 375
    if(window.screen.orientation && /^landscape/.test(window.screen.orientation.type || '')) newDeviceWidth = newDeviceHeight
    if(newDeviceWidth !== deviceWidth || newDeviceDPR !== deviceDPR) {
        deviceWidth = newDeviceWidth
        deviceDPR = newDeviceDPR
    }
}
checkDeviceWidth()
var eps = 1e-4;

function transformRPX(number) {
    if(number === 0) return 0;
    number = number / BASE_DEVICE_WIDTH * deviceWidth;
    number = Math.floor(number + eps);
    if(number === 0) {
        if(deviceDPR === 1 || !isIOS) {
            return 1;
        } else {
            return 0.5;
        }
    }
    return number;
}
var setCssToHead = function(file, _xcInvalid) {
    var Ca = {};
    var _C = [];

    function makeup(file, suffix) {
        var _n = typeof(file) === "number";
        if(_n && Ca.hasOwnProperty(file)) return "";
        if(_n) Ca[file] = 1;
        var ex = _n ? _C[file] : file;
        var res = "";
        for(var i = ex.length - 1; i >= 0; i--) {
            var content = ex[i];
            if(typeof(content) === "object") {
                var op = content[0];
                if(op == 0)
                    res = transformRPX(content[1]) + "px" + res;
                else if(op == 1)
                    res = suffix + res;
                else if(op == 2)
                    res = makeup(content[1], suffix) + res;
            } else
                res = content + res
        }
        return res;
    }
    return function(suffix, opt) {
        if(typeof suffix === "undefined") suffix = "";
        if(opt && opt.allowIllegalSelector != undefined && _xcInvalid != undefined) {
            if(opt.allowIllegalSelector)
                console.warn("For developer:" + _xcInvalid);
            else {
                console.error(_xcInvalid + "This wxss file is ignored.");
                return;
            }
        }
        Ca = {};
        css = makeup(file, suffix);
        var style = document.createElement('style');
        var head = document.head || document.getElementsByTagName('head')[0];
        style.type = 'text/css';
        if(style.styleSheet) {
            style.styleSheet.cssText = css;
        } else {
            style.appendChild(document.createTextNode(css));
        }
        head.appendChild(style);
    }
}