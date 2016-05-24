from libsoc_zero.GPIO import Button

touch = Button('GPIO-C')

while True:
    if touch.is_pressed():
        print("Button is pressed")
    else:
        print("Button is not pressed")
