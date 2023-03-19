import valve
import time

valve.init()  #自动搜索阀门，初始化通讯
time.sleep(5)

while True:
    #
    time.sleep(0.05)
    valve.trig(0)   #状态0
    print("Trig 0")
    #
    time.sleep(0.05)
    valve.trig(1)   #状态1
    print("Trig 1")

