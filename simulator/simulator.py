import models  
from time import sleep

motor1 = models.motor(True, speed = 15, minimum = 10, maximum = 30)
pump1 = models.pump(True, 60, minimum= 600, maximum=620)

while True:
    motor1.simulate_speed()
    motor1.publish_state()
    motor1.publish_speed()
    pump1.simulate_pressure()
    pump1.publish_pressure()
    pump1.publish_state()
    sleep(3)