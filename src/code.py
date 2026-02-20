import time
import board
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# 1) I2C bus (Feather SDA/SCL pins)
i2c = busio.I2C(board.SCL, board.SDA)

# 2) PCA9685 at default address 0x40
pca = PCA9685(i2c, address=0x40)

# 3) Standard servo refresh rate
pca.frequency = 50

# 5) Create a servo object
# Most micro servos: pulse range ~500-2500 us is common
s1 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
s2 = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)

print("Starting servo test...")

while True:
    # Move to three positions
    s1.angle = 180
    s2.angle = 180
    time.sleep(1)

    s1.angle = 100
    s2.angle = 100
    time.sleep(1)
