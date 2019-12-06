from gpiozero import LED
from time import sleep

SwitchOne = LED(4)
SwitchTwo = LED(14)
i = 0

print ("Test Switch 1...")

while i < 100:
    SwitchOne.on()
    sleep(0.1)
    SwitchOne.off()
    sleep(0.1)
    i += 1

print ("Test Switch 2...")
i = 0

while i < 100:
    SwitchTwo.on()
    sleep(0.1)
    SwitchTwo.off()
    sleep(0.1)
    i += 1

print ("Test Complete")