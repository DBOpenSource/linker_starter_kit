from libsoc_zero.GPIO import Button
from time import sleep

btn = Button('GPIO-G')

while True:
    sleep(0.25)
    if btn.is_pressed():
        print('Button is pressed!')
    else:
        print('Button is not pressed!')
