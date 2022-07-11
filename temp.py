import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 20

while True:
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

  print ('Humedad: ' , humedad)
  print ('Temp ºC: ' , temperatura)

  time.sleep(1)
