import paho.mqtt.publish as publish
import random
HOSTNAME = "mqtt.eclipse.org"

class pump:

    def __init__(self, state, pressure, minimum, maximum):

        self.state = state
        self.pressure = pressure
        self.minimum = minimum
        self.maximum = maximum

    def simulate_pressure(self):

        if self.state == True:
            self.pressure = float(random.randint(self.minimum, self.maximum))

    
    def publish_state(self):

        publish.single("mqttsimulator/pump/state", self.state, hostname=HOSTNAME)
        print("send {} to {}".format(self.state,HOSTNAME))

    def publish_pressure(self):
    
        publish.single("mqttsimulator/pump/pressure", self.pressure, hostname=HOSTNAME)
        print("send {} to {}".format(self.pressure,HOSTNAME))
    

class motor:

    def __init__(self, state, speed, minimum, maximum):
        self.state = state
        self.speed = speed
        self.minimum = minimum
        self.maximum = maximum
        

    def simulate_speed(self):
        
        if self.state == True:
            self.speed = float(random.randint(self.minimum, self.maximum))
        else:
            self.speed = 0.0
        
    def publish_state(self):
        publish.single("mqttsimulator/motor/state", self.state, hostname=HOSTNAME)
        print("send {} to {}".format(self.state,HOSTNAME))

    def publish_speed(self):
        publish.single("mqttsimulator/motor/speed", self.speed, hostname=HOSTNAME)
        print("send {} to {}".format(self.speed,HOSTNAME))





#TODO: Implementar publish múltiplo


