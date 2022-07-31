import os
import time
import ADS1x15

ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

ADS.setGain(ADS.PGA_1_024V)
f = ADS.toVoltage()

while True :
    val_0 = ADS.readADC(1)
    print("%.6f %.6f" % (val_0, f))
    time.sleep(1)
