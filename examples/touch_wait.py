from libsoc_zero.GPIO import Button

touch = Button('GPIO-C')

print('Waiting for press event...')
touch.wait_for_press()
print('Button was pressed!')
