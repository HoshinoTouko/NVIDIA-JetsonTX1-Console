import time
from CarController import CarController


class StopProcess:

    enable = True

    def __init__(self):
        self.oldTime = time.time()
        self.carController = CarController()
        pass

    def stopProcess(self, delay):
        while(1):
            time.sleep(delay)
            self.checkStop()
            if not StopProcess.enable:
                self.carController.stop()

    def checkStop(self):
        return self.setRun()
        if time.time() - self.oldTime > 5 and time.time() - self.oldTime < 10:
            return self.setStop()
        else:
            return self.setRun()

    def setStop(self):
        StopProcess.enable = False
        return False

    def setRun(self):
        StopProcess.enable = True
        return True
