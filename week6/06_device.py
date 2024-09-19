class Device:
    def turn_on(self):
        pass

class TV(Device):
    def turn_on():
        return "TV is now on"
class Fan(Device):
    def turn_on():
        return "Fan is now spinning"
class Light(Device):
    def turn_on():
        return "Light is now on"
    
    
def activate_device(device):
    print(device.turn_on())

#create instances of each devices
tv=TV()
fan=Fan()
light=Light()


activate_device(tv)
activate_device(fan)
activate_device(light)