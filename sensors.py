import gpiozero as gz
from gpiozero import MotionSensor, LED
import Adafruit_DHT as ht
from gpiozero import Motor
import time
"""
To Install Adafruit_Python_DHT lib follow the below steps

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
sudo python3 setup.py install
"""
#Humidity and Temperature sensor
HT_sensor_type=ht.DHT11
HT_gpio_pin=17

# Motor Init 
motor = Motor(forward=4, backward=14)

# Moisture sensor init
Moisture_sensor_pin=23

Moisture_sensor = gz.InputDevice(Moisture_sensor_pin)

print("Hello")

while True:
    
    # Humidity and Temperature

    humidity, temperature = ht.read_retry(HT_sensor_type, HT_gpio_pin)

    print("Humidity={},\n Temprature={}".format(humidity, temperature))

    
    #Moisture Sensor    
    
    ms_status = Moisture_sensor.is_active
    if ms_status:
        print("Moisture Sensor status: It is Dry")
        motor.forward()
        time.sleep(10)
    else:
        print("Moisture Sensor status: It is Moist")
        motor.stop()
    time.sleep(1)
