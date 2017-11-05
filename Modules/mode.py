class Mode:
    mode = 0
    # mode0: manual
    # mode1: auto (6 pics)
    # mode2: auto track
    @staticmethod
    def changeMode(target):
        print 'Change mode to ' + target
        Mode.mode = int(target)

    @staticmethod
    def getMode():
        return Mode.mode
