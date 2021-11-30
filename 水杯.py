class Watercup:
    __height= 0.0#高度  cm
    __volume= 0#容积  毫升
    __colour= ""#颜色
    __material= ""#材质
#------------------------------------------------
    def setheight(self,height):
        if height <0.1 or height>30:
            print("你搁这玩呢？？")
        else:
            self.__height=height
    def getheight(self):
        return self.__height
#-----------------------------------------------------
    def setvolume(self,volume):
        if volume<20 or volume>10000:
            print("跟谁俩呢？")
        else:
            self.__volume=volume
    def getvolume(self):
        return self.__volume
#------------------------------------------------
    def setcolour(self,colour):
        if colour=="":
            print("没这个颜色")
        else:
            self.__colour=colour
    def getcolour(self):
        return self.__colour
#---------------------------------------------------
    def setmaterial(self,material):
        if material=="":
            print("你还是个啥")
        else:
            self.__material=material
    def getmaterial(self):
        return self.__material
#----------------------------------------
    def deposit(self):
        print("水杯高度",self.__height,"厘米",
              "水杯容积",self.__volume,"毫升",
              "水杯颜色",self.__colour,"色",
              "水杯材质",self.__material,"材质")
w = Watercup()

w.setheight(30)
w.setvolume(50)
w.setcolour("红")
w.setmaterial("玻璃")

print(w.getheight())
print(w.getvolume())
print(w.getcolour())
print(w.getmaterial())

w.deposit()
