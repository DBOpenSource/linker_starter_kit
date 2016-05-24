from libsoc_zero.GPIO import Button
from libsoc_zero.GPIO import LED
from time import sleep

btn = Button('GPIO-G')
led = LED('GPIO-E')


while True:

    btn.wait_for_press()
    if led.is_lit:
        led.off()
    else:
        led.off()

    sleep(1)