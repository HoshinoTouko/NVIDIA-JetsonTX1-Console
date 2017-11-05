import Modules.Camera
import thread

from Modules.MainProc import MainProcess
from Modules.StopProc import StopProcess

def main():
    stopProcess = StopProcess()
    thread.start_new_thread(stopProcess.stopProcess, (0.1, ))

    mainProcess = MainProcess('MainProcess')
    mainProcess.run()

if __name__ == '__main__':
    main()
