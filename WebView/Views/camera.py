import cv2
import time
import Modules.Camera as camModule

from Modules.CarController import CarController
from flask import Blueprint, Response, render_template

CAMERA = Blueprint('camera', __name__)
carController = CarController()


class VideoCamera(object):
    def __init__(self, cam):
        self.video = cam

    def __del__(self):
        pass
        # self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # res = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        time.sleep(1)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@CAMERA.route('/')
def video_feed():
    return Response(gen(VideoCamera(camModule.Camera.getCap())),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

