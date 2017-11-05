#coding=utf-8
import serial
import time
from Modules.DistanceQueue import DistanceQueue

from FindSerials import plist
if 0 == len(plist):
    print 'No device'

    try:
        ser = serial.Serial(str(plist[0]).split('-')[0].replace(' ', ''), 115200)
    except Exception as e:
        print e

    exit(0)

class CarController:

    # ser = serial.Serial('COM3', 115200)
    try:
        ser = serial.Serial(str(plist[0]).split('-')[0].replace(' ', ''), 115200)
    except Exception as e:
        print e

    def __init__(self):
        self.ser = CarController.ser
        time.sleep(1)

    def readdata(self):
        return self.ser.read_until().replace('\t', '').replace('\n', '')

    def readDistance(self):
        return DistanceQueue.last()['front'], DistanceQueue.last()['back']

    def eventHandler(self, object):
        eventDict = {
            'cat': self.rush,
            'bicycle': self.reverse,
            'sofa': self.turn_right,
            'dog': self.turn_left,
            'train': self.turn_right_and_rush,
            'bus': self.turn_right_and_rush,
            'car': self.turn_left_and_rush
        }
        func = eventDict.get(object) if object in eventDict.keys() else self.noUse
        return func()

    def noUse(self):
        return 0

    def setTime(self, longlong):
        self.ser.write(int(longlong))
        return '1'

    def go(self):
        print 'Rush! The car will go ahead.'
        self.ser.write('G')
        return '1'

    def back(self):
        print 'Go back! The car will go back.'
        self.ser.write('H')
        return '1'

    def rush(self):
        print 'Rush! The car will go ahead 2 secs.'
        self.ser.write('A')
        return 2

    def reverse(self):
        print 'Reverse! The car will go back 2 secs.'
        self.ser.write('B')
        return 2

    def right_turn(self):
        print 'Turn right! The car will turn right.'
        self.ser.write('J')
        return '1'

    def left_turn(self):
        print 'Turn left! The car will turn left.'
        self.ser.write('I')
        return '1'

    def turn_right(self):
        print 'Turn right! The car will turn right 360 degree.'
        self.ser.write('C')
        return 8.6

    def turn_left(self):
        print 'Turn right! The car will turn left 360 degree.'
        self.ser.write('D')
        return 8.6

    def turn_left_and_rush(self):
        print 'Turn right and rush! The car will turn right 360 degree.'
        self.ser.write('E')
        return 4.3

    def turn_right_and_rush(self):
        print 'Turn left and rush! The car will turn left 360 degree.'
        self.ser.write('F')
        return 4.3

    def turn_left_ahead(self):
        print 'turn_left_ahead'
        self.ser.write('L')
        return '1'

    def turn_right_ahead(self):
        print 'turn_right_ahead'
        self.ser.write('K')
        return '1'

    def stop(self):
        print 'Stop the car.'
        self.ser.write('S')
        return '1'

    def speed_up(self):
        print 'speed_up'
        self.ser.write('X')
        return '1'



def main():
    carCtrl = CarController()
    time.sleep(3)
    carCtrl.rush()

if __name__ == '__main__':
    main()

