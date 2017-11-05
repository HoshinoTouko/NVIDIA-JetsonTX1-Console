function refresh_distance() {
    $.get("/api/get_distance/front", function (data) {
        $("#front-dis").html('Front: ' + data);
    });
    $.get("/api/get_distance/back", function (data) {
        $("#back-dis").html('Back: ' + data);
    });
}
setInterval("refresh_distance()", 1000);

window.onload = function () {
    document.getElementById("forward-left").onclick = function () {
        $.get("/api/left_ahead");
    };
    document.getElementById("forward").onclick = function () {
        $.get("/api/go");
    };
    document.getElementById("forward-right").onclick = function () {
        $.get("/api/right_ahead");
    };
    document.getElementById("left").onclick = function () {
        $.get("/api/left");
    };
    document.getElementById("stop").onclick = function () {
        $.get("/api/stop");
    };
    document.getElementById("right").onclick = function () {
        $.get("/api/right");
    };
    document.getElementById("back-left").onclick = function () {
        $.get("/api/dash");
    };
    document.getElementById("back").onclick = function () {
        $.get("/api/back");
    };
    document.getElementById("back-right").onclick = function () {
        $.get("/api/dash");
    };
    document.getElementById("but-one").onclick = function () {
        $.get("/api/change_mode/0");
    };
    document.getElementById("but-two").onclick = function () {
        $.get("/api/change_mode/1");
    };
    document.getElementById("but-three").onclick = function () {
        $.get("/api/change_mode/2");
    };

    document.onkeydown = function (event) {
        var e = event || window.event || arguments.callee.caller.arguments[0];
        if (e && e.keyCode == 37) {
            console.log("left");
        }
        if (e && e.keyCode == 38) {
            console.log("up");
        }
        if (e && e.keyCode == 39) {
            console.log("right");
        }
        if (e && e.keyCode == 40) {
            console.log("down");
        }
        if (e && e.keyCode == 32) {
            console.log("stop");
        }
    };
}