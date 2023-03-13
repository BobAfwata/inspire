from machine import ADC, Pin, I2C
import ssd1306
import time
from time import sleep
import dht 
 


class LDR:
    """This class read a value from a light dependent resistor (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100):
        """
        Initializes a new instance.
        :parameter pin A pin that's connected to an LDR.
        :parameter min_value A min value that can be returned by value() method.
        :parameter max_value A max value that can be returned by value() method.
        """

        if min_value >= max_value:
            raise Exception('Min value is greater or equal to max value')

        # initialize ADC (analog to digital conversion)
        self.adc = ADC(Pin(pin))

        # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        #self.adc.atten(ADC.ATTN_11DB)

        self.min_value = min_value
        self.max_value = max_value

    def read(self):
        """
        Read a raw value from the LDR.
        :return A value from 0 to 4095.
        """
        return self.adc.read()

    def value(self):
        """
        Read a value from the LDR in the specified range.
        :return A value from the specified [min, max] range.
        """
        return (self.max_value - self.min_value) * self.read() / 4095


# initialize an LDR
ldr = LDR(28)

# using default address 0x3C
i2c = I2C(1,sda=Pin(26), scl=Pin(27))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

sensor = dht.DHT11(Pin(16))


while True:
    # read a value from the LDR
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print('Temperature: %3.1f C' %t)
    print('Humidity: %3.1f %%' %h)
    value = ldr.value()
    print('value = {}'.format(value))
    display.text('Temp:{}'.format(t) , 0, 0, 1)
    display.text('Hum:{}'.format(h), 10, 0, 1)
    display.text('Light: {}'.format(value), 20, 0, 1)
    display.show()

    # a little delay
    time.sleep(3)