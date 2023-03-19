# 1 概述

一个可以通过 Python 脚本，通过串口远程控制链接 Arduino 的电磁阀的软件。

分为两个文件夹：

1. “Arduino 端代码” 文件夹：写入Arduino端的程序
2. “Python 端代码” 文件夹：电脑端库以及示范

# 2 环境配置

1. 首先 pip 安装 Python - Arduino 支持：pip install arduino-python3

2. 接着，上传 Arduino 端代码 到 Arduino Mega 2560 中

3. 运行 “Python 端代码” 文件夹中的示范

# 3 库用法

valve 库用于控制阀门，电脑插入 Arduino 控制器后，通过调用 valve.init() 可以自动搜索控制器端口并自动建立连接，初始化通讯。 valve.trig 函数可以设置阀门状态，状态为 0 或 1，对应两个阀门的物理状态 (Port 2-3 pass , 1 is blocked  或 Port 1-2 pass, 3 is blocked)。

**典型用法：**

```python
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
```

