class DistanceQueue:
    queue = []

    @staticmethod
    def add(dic):
        DistanceQueue.queue.append(dic)

    @staticmethod
    def last():
        return DistanceQueue.queue[len(DistanceQueue.queue)-1]
