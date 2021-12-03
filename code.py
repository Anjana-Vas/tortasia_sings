import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D1)
led.switch_to_output()
button = digitalio.DigitalInOut(board.D0)
button.switch_to_output()
cs = digitalio.DigitalInOut(board.D10)
cs.switch_to_output()
dio = digitalio.DigitalInOut(board.D9)
dio.switch_to_output()


while True:
    led.value = True
    time.sleep(5.00)

    led.value = False
    time.sleep(0.25)

    button.value = True
    time.sleep(5.00)

    button.value = False
    time.sleep(0.25)

    cs.value = True
    time.sleep(5.00)

    cs.value = False
    time.sleep(0.25)

    dio.value = True
    time.sleep(5.00)

    dio.value = False
    time.sleep(0.25)