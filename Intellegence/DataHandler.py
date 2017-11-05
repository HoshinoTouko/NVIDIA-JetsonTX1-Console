class DataHandler:
    def __init__(self,MAXN=200,STEP=20):
        self.MAXN=MAXN
        self.STEP=STEP
        self.lis=["None" for i in range(self.MAXN)]
        self.num={}
        self.num["None"] = self.MAXN
        self.nums = [{"None" : self.STEP} for i in range(self.MAXN//self.STEP)]
    def deal(self,i_data):
        now={"None" : 0}
        for i in range(self.STEP):
            try:
                now[i_data[i]]+=1
            except KeyError:
                now[i_data[i]]=1
            except IndexError:
                now["None"]+=1
        for key in now:
            try:
                self.num[key]+=now[key]
            except KeyError:
                self.num[key]=now[key]

        self.nums=[now]+self.nums
        now=self.nums.pop()
        for key in now:
            self.num[key]-=now[key]
        max = ("None",0)
        for key in self.num:
            if (self.num[key]>max[1] and key!="None"):
                max=(key,self.num[key])
        tmp=0
        for i in range(10):
            try:
                tmp+=self.nums[i][max[0]]*(10-i)
            except KeyError:
                pass
        if (tmp>=2*self.MAXN and max[0]!="None"):
            return max[0]
        return False
    def clear(self):
        self.lis=["None" for i in range(self.MAXN)]
        self.num={}
        self.num["None"] = self.MAXN
        self.nums = [{"None" : self.STEP} for i in range(self.MAXN//self.STEP)]

if __name__ == "__main__":
    ans=DataHandler();
    aa=[
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[],
[],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'bottle', u'sofa', u'sofa', u'sofa', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'bottle', u'sofa', u'sofa', u'sofa', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'chair', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'chair', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa', u'sofa'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'person', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'person'],
[u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'bottle', u'person', u'person'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'sofa', u'sofa'],
[u'bottle', u'bottle', u'person', u'person', u'person', u'person', u'person', u'person', u'sofa', u'sofa'],
[u'bottle', u'bottle', u'person'],
[u'bottle', u'bottle', u'person'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'bottle', u'bottle'],
[u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor', u'tvmonitor'],
[u'aeroplane', u'car', u'car', u'person', u'person', u'person'],
[u'aeroplane', u'car', u'car', u'person', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person', u'person'],
[u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person'],
[u'aeroplane', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person'],
[u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person'],
[u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person'],
[u'aeroplane', u'person'],
[u'person'],
[u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'person', u'person', u'person'],
[u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[],
[],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'car', u'person', u'person', u'person'],
[u'aeroplane', u'car', u'person', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'aeroplane', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'car', u'person', u'person', u'person'],
[u'aeroplane', u'car', u'person', u'person', u'person'],
[u'person'],
[u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'aeroplane', u'person', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'aeroplane', u'aeroplane', u'person', u'person'],
[u'person', u'person', u'person'],
[u'person', u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'aeroplane', u'person'],
[u'aeroplane', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person'],
[u'person', u'person']
        ]
    for i in aa:
        print(ans.deal(i))
