import cv2
import numpy
import matplotlib.pyplot as plot

class Camera:
    cap = cv2.VideoCapture(0)

    @staticmethod
    def getCamera():
        ret, frame = Camera.cap.read()
        return ret, frame

    @staticmethod
    def getCap():
        return Camera.cap


def main():
    camera = Camera()
    while(1):
        ret, frame = camera.getCamera()

        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.cap.release()
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
