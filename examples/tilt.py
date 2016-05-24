from libsoc_zero.GPIO import Tilt

tilt = Tilt('GPIO-G')

tilt.wait_for_tilt()

print('Tilt happened')
