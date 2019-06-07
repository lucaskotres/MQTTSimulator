import models  

motor1 = models.motor(True, rotation = 15, minimum = 10, maximum = 30)
pump1 = models.pump(True, 60)

motor1.simulate_rotation()
motor1.publish_state()
motor1.publish_rotation()
