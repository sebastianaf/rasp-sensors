# raspInit
Raspberry python scripts for five different sensors.
The code is tested to be used over RaspberryPi with Python, the components are: an analog to digital converter [ADS1015](https://pdf1.alldatasheet.com/datasheet-pdf/view/292738/TI/ADS1015.html), Temperature and humidity sensor [DHT11](https://components101.com/sensors/dht11-temperature-sensor), a water flow sensor [YF-S201](https://www.mantech.co.za/datasheets/products/yf-s201_sea.pdf), no invasive current sensor [SCT013](https://pdf1.alldatasheet.com/datasheet-pdf/view/1160244/YHDC/SCT013-050.html) and a voltage metter sensor [ZMPT101B](https://pdf1.alldatasheet.com/datasheet-pdf/view/1131993/ETC2/ZMPT101B.html).

##Requirements
1. Activate I2C Interface with `raspi-config`
2. Type the next commands to install the requirements.
```python
sudo apt-get install python3-pip
pip3 install Adafruit_DHT
pip3 install ADS1x15
```
##Seting up
It's recommended to adjust the `factor` python variables depending of the calibration of the sensors in your setup, make sure to change the `pins` python variables too.
