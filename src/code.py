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

# 4) Pick the channel your servo is plugged into (0..15)
ch = pca.channels[0]

# 5) Create a servo object
# Most micro servos: pulse range ~500-2500 us is common
s = servo.Servo(ch, min_pulse=500, max_pulse=2500)

print("Starting servo test...")

while True:
    # Move to three positions
    s.angle = 90
    time.sleep(1)

    s.angle = 0
    time.sleep(1)

    s.angle = 180
    time.sleep(1)

    # Sweep smoothly
    for a in range(0, 181, 5):
        s.angle = a
        time.sleep(0.02)
    for a in range(180, -1, -5):
        s.angle = a
        time.sleep(0.02)
