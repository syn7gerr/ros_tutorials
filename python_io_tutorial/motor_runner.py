import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time


motor_1_pin_1 = "P8_11"
motor_1_pin_2 = "P8_12"
motor_1_pin_pwm = "P8_13"

motor_2_pin_1 = "P8_17"
motor_2_pin_2 = "P8_18"
motor_2_pin_pwm = "P8_19"

motor_3_pin_1 = "P9_11"
motor_3_pin_2 = "P9_12"
motor_3_pin_pwm = "P9_14"

motor_4_pin_1 = "P9_17"
motor_4_pin_2 = "P9_18"
motor_4_pin_pwm = "P9_16"


GPIO.setup(motor_1_pin_1, GPIO.OUT)
GPIO.setup(motor_1_pin_2, GPIO.OUT)
GPIO.output(motor_1_pin_1, GPIO.HIGH)
GPIO.output(motor_1_pin_2, GPIO.LOW)

GPIO.setup(motor_2_pin_1, GPIO.OUT)
GPIO.setup(motor_2_pin_2, GPIO.OUT)
GPIO.output(motor_2_pin_1, GPIO.HIGH)
GPIO.output(motor_2_pin_2, GPIO.LOW)

GPIO.setup(motor_3_pin_1, GPIO.OUT)
GPIO.setup(motor_3_pin_2, GPIO.OUT)
GPIO.output(motor_3_pin_1, GPIO.HIGH)
GPIO.output(motor_3_pin_2, GPIO.LOW)

GPIO.setup(motor_4_pin_1, GPIO.OUT)
GPIO.setup(motor_4_pin_2, GPIO.OUT)
GPIO.output(motor_4_pin_1, GPIO.HIGH)
GPIO.output(motor_4_pin_2, GPIO.LOW)


PWM.start(motor_1_pin_pwm, 50)
PWM.start(motor_2_pin_pwm, 50)
PWM.start(motor_3_pin_pwm, 50)
PWM.start(motor_4_pin_pwm, 50)


time.sleep(5)


PWM.stop(motor_1_pin_pwm)
PWM.stop(motor_2_pin_pwm)
PWM.stop(motor_3_pin_pwm)
PWM.stop(motor_4_pin_pwm)
PWM.cleanup()