import time
import cv2
import thread
import Modules.Camera as camModule
from Modules.DistanceQueue import DistanceQueue
from Intellegence.DataHandler import DataHandler
from flask import session
import Intellegence.ObjectTrack.ObjectTrack as Oj

from CarController import CarController
carCtrl = CarController()
from StopProc import StopProcess

# Import image detect
try:
    from Intellegence.ImageDetect import detect
except Exception as e:
    print e

class MainProcess:

    def __init__(self, processName):
        self.name = processName
        self.carController = CarController()

    @staticmethod
    def distanceQueue():
        while (1):
            front = -1
            back = -1
            try:
                while (carCtrl.ser.readable()):
                    command = carCtrl.readdata()
                    print 'Read distance read: ' + command
                    if 'front' in command:
                        command = carCtrl.readdata()
                        print 'Read distance read: ' + command
                        front = int(command)
                    if 'back' in command and front != -1:
                        command = carCtrl.readdata()
                        print 'Read distance read: ' + command
                        back = int(command)
                        break
            except Exception as e:
                print e

            DistanceQueue.add({
                'front': front,
                'back': back
            })
            time.sleep(0.2)

    def run(self, mode):
        # Run distance monitor
        thread.start_new_thread(MainProcess.distanceQueue, ())



        self.mode = mode
        allDict = {}
        dataHandler = DataHandler()

        while(1):
            result = False
            if self.mode.getMode() == 1:
                try:
                    top_labels = detect()
                    # print top_labels
                    result = dataHandler.deal(top_labels)
                except Exception as e:
                    print e
                    time.sleep(0.5)

                if result:
                    print 'FIND!! ' + result
                    sleepTime = carCtrl.eventHandler(result)
                    time.sleep(sleepTime)
                    if sleepTime != 0: dataHandler.clear()
            elif self.mode.getMode() == 0:
                time.sleep(3)
            else:
                # New object track
                objectTrack = Oj.ObjTrack(50)
                while (1):
                    if self.mode.getMode() != 2:
                        break
                    position, area = objectTrack.track()
                    if position > 65:
                        carCtrl.right_turn()
                        time.sleep(1)
                        carCtrl.stop()
                    elif position < 35:
                        carCtrl.left_turn()
                        time.sleep(1)
                        carCtrl.stop()
                    elif area > 80:
                        carCtrl.back()
                        time.sleep(1)
                        carCtrl.stop()
                    elif area < 20:
                        carCtrl.go()
                        time.sleep(1)
                        carCtrl.stop()


