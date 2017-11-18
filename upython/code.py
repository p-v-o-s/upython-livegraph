import digitalio
import board
import time

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

i = 0
while True:
    i += 1
    ts = time.monotonic()
    print("<r>%0.2f, %d</r>" % (ts, i))
    led.value = not led.value
    time.sleep(1.0)
