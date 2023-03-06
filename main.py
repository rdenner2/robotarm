import RPi.GPIO as GPIO

def motorinit():
    GPIO.setmode(GPIO.BOARD)

if __name__ == "__main__":
    motorinit()

