from gpiozero import LED
from time import sleep

SwitchOne = LED(4)
SwitchTwo = LED(14)
i = 0

print ("Starting...")

while True:
    SwitchOne.on()
    SwitchTwo.on()
    sleep(0.1)
    SwitchOne.off()
    SwitchTwo.off()
    sleep(0.1)
    
