import paho.mqtt.publish as publish
import random

class pump:

    def __init__(self, state, pressure):

        self.state = state
        self.pressure = pressure

    def publish_pressure(self):

        publish.single("mqttsimulator/pump/pressure", self.pressure, hostname="iot.eclipse.org")

    def publish_state(self):

        publish.single("mqttsimulator/pump/state", self.state, hostname="iot.eclipse.org")
        

class motor:

    def __init__(self, state, rotation, minimum, maximum):
        self.state = state
        self.rotation = rotation
        self.minimum = minimum
        self.maximum = maximum
        

    def simulate_rotation(self):
        
        if self.state == True:
            self.rotation = float(random.randint(self.minimum, self.maximum))
        else:
            self.rotation = 0.0
        
    def publish_state(self):
        publish.single("mqttsimulator/motor/state", self.state, hostname="iot.eclipse.org")

    def publish_rotation(self):
        publish.single("mqttsimulator/motor/rotation", self.rotation, hostname="iot.eclipse.org")



motor1 = motor(True, rotation = 15, minimum = 10, maximum = 30)
pump1 = pump(True, 60)

motor1.simulate_rotation()
motor1.publish_state()
motor1.publish_rotation()


pump1 = pump(True, 60)


pump1.publish_pressure()
pump1.publish_state()

#TODO: Implementar publish múltiplo


