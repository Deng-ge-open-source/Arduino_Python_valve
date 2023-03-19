from Arduino import Arduino

def init():
    global board
    board = Arduino() #Auto search Arduino 2560 board
    board.pinMode(7, "OUTPUT")
    return 1


def trig(sta):
    if sta==0:
        board.digitalWrite(7, "LOW")
        return 0
    elif sta==1:
        board.digitalWrite(7, "HIGH")
        return 1
    
