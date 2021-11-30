import time
class notebook:
    __screensize= 0.0#屏幕大小 英寸
    __price= 0#价格  人民币
    __cpu= ""#CPU型号
    __memory= 0#内存大小
    __StandbyT= 0#待机时长
#----------------------------------------
    def setscreensize(self,screensize):
        if screensize != 15.6 and screensize!= 17.4 and screensize!= 18.4:
            print("你不正常")
        else:
            self.__screensize = screensize
    def getscreensize(self):
        return self.__screensize
#--------------------------------------------
    def setprice(self,price):
        if price > 100000 or   price<50:
            print("你应该有大病")
        else:
            self.__price=price
    def getprice(self):
        return self.__price
#-------------------------------
    def setcpu(self,cpu):
        if  cpu!="英特尔" and  cpu!="AMD" :
            print("请输入正确的CPU型号")
        else:
            self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
#-------------------------------------
    def setmemory(self,memory):
        if memory!=8 and  memory!=16:
            print("没有选择内存")
        else:
            self.__memory = memory
    def getmemory(self):
        return self.__memory
#-------------------------------------------------------
    def setStandbyT(self,StandbyT):
        if StandbyT != 4 and  StandbyT!=3 :
            print("请输入正确的待机时长")
        else:
            self.__StandbyT=StandbyT
    def getStandbyT(self):
        return self.__StandbyT
#-------------------------------------------------------
    def typing(self,dazsj):
        for i in range(2):
            print(".", end="")
            time.sleep(1)
        print("打字", dazsj, "小时")
    def playgames(self,playgame,hour):
        for i in range(2):
            print(".", end="")
            time.sleep(1)
        print("打" ,playgame,"游戏",hour, "小时")
    def video(self,name,hour):
        for i in range(2):
            print(".",end="")
            time.sleep(1)
        print("播放",name,"视频",hour,"小时")

    def zong(self):
        print("电脑屏幕为",self.__screensize,"英寸",
              "价格为",self.__price,"元",
              "CPU型号为",self.__cpu,
              "内存大小为",self.__memory,"G"
              "待机时长",self.__StandbyT,"小时"
              )
n=notebook()
n.setscreensize(17.4)
n.setprice(6000)
n.setcpu("英特尔")
n.setmemory(16)
n.setStandbyT(4)
print(n.getscreensize())
print(n.getprice())
print(n.getcpu())
print(n.getmemory())
print(n.getStandbyT())
n.typing(1)
n.playgames("LOL",2)
n.video("王者荣耀",2)
n.zong()
