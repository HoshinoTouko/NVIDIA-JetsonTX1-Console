from flask import Flask, render_template, Response
import cv2
import Modules.Camera as cam


class VideoCamera(object):
    def __init__(self):
        pass
        # self.video = cv2.VideoCapture(0)

    def __del__(self):
        pass
        # self.video.release()

    def get_frame(self):
        success, image = cam.Camera.getCamera()
        res = cv2.resize(image, (320, 280), interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', res)
        return jpeg.tobytes()


app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = 5000)
