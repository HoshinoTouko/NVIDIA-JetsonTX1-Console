import thread
import cv2
from Modules.mode import Mode

from flask import Flask, session, g
from WebView.Views.index import INDEX
from WebView.Views.ctrl import CTRL
from WebView.Views.camera import CAMERA

from Modules.MainProc import MainProcess
from Modules.StopProc import StopProcess

# PyCtrl
stopProcess = StopProcess()
thread.start_new_thread(stopProcess.stopProcess, (0.1, ))


def runServer():
    # Web view
    # Instance relative config
    print 'Running main server...'
    APP = Flask(__name__, instance_relative_config=True)
    # Blueprint
    APP.register_blueprint(INDEX, url_prefix='/')
    APP.register_blueprint(CTRL, url_prefix='/api')
    APP.register_blueprint(CAMERA, url_prefix='/video_feed')
    APP.run(host='0.0.0.0', debug=False, port=1235, threaded=True)

thread.start_new_thread(runServer, ())
# thread.start_new_thread(hotCam.runCameraApp, ())

mainProcess = MainProcess('MainProcess')
mainProcess.run(Mode)
