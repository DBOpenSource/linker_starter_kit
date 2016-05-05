from libsoc_zero.GPIO import Tilt

tilt = Tilt('GPIO-C')

tilt.wait_for_tilt()

print('Tilt happened')
