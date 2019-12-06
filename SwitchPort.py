from gpiozero import LED
from time import sleep

SwitchOne = LED(4)
SwitchTwo = LED(14)
i = 0

while i < 10:
    SwitchOne.on()
    sleep(0.1)
    SwitchOne.off()
    sleep(0.1)
    i += 1