from serial import Serial

arduinoData = Serial('com6', 9600)

def led_on():
    arduinoData.write(b'1')

def led_off():
    arduinoData.write(b'0')

t = 0
while(t<100000):
    if(t % 10 == 0):
        print(t)
    t+=1
led_on()