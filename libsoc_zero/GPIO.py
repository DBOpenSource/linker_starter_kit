from libsoc import gpio


class LED:
    """
    Control an LED object
    The pin name should be of the format 'GPIO-A'
    """
    def __init__(self, pin):
        gpio.GPIO.set_debug(False)
        self.is_lit = 0
        self.gpio_output_int = gpio.GPIO.gpio_id(pin)
        self.gpio_out = gpio.GPIO(self.gpio_output_int, gpio.DIRECTION_OUTPUT)
        self.gpio_out.open()

    def close(self):
        """
        When you've finished close it all down nicely!
        """
        self.off()
        self.gpio_out.close()

    def on(self):
        """
        Turn the device on
        """
        self.is_lit = 1
        self.gpio_out.set_high()

    def off(self):
        """
        Turn the device off
        """
        self.is_lit = 0
        self.gpio_out.set_low()


class Input:
    """
    Control a digital input component
    The pin name should be of the format 'GPIO-A'
    """
    def __init__(self, gpio_input_id):
        self.ih = None
        gpio.GPIO.set_debug(False)
        self.gpio_input_int = gpio.GPIO.gpio_id(gpio_input_id)
        self.gpio_in = gpio.GPIO(self.gpio_input_int,
                                 gpio.DIRECTION_INPUT,
                                 gpio.EDGE_RISING)
        self.gpio_in.open()

    def close(self):
        """
        When you've finished close it all down nicely!
        """
        self.clear_when_pressed()
        self.gpio_in.close()

    def is_pressed(self):
        """
        Get the state of the input device
        :return:
        Returns 'True' if active. 'False' if not
        """
        return self.gpio_in.is_high()

    def trigger_on_rising_edge(self):
        """
        Set the edge that the interrupt will trigger off
        :return:
        """
        result = gpio.api.libsoc_gpio_set_edge(self.gpio_in._gpio, gpio.EDGE_RISING)
        if result != 0:
            raise IOError(u'Error setting edge for GPIO_{0:d}'.format(self.gpio_input_int))

    def get_edge(self):
        """
        Returns which edge is currently set for interrupt
        :return: integer
        0 = EDGE_NONE
        1 = EDGE_FALLING
        2 = EDGE_RISING
        3 = EDGE_BOTH
        """
        return gpio.api.libsoc_gpio_get_edge(self.gpio_in._gpio)

    def wait_for_press(self, timeout=10000000):
        """
        Pause the script until the device is activated or the timeout is reached
        """
        self.gpio_in.wait_for_interrupt(timeout)

    def when_pressed(self, interrupt_callback):
        self.trigger_on_rising_edge()
        self.ih = self.gpio_in.start_interrupt_handler(interrupt_callback)

    def clear_when_pressed(self):
        """
        Remove callback from when_pressed
        """
        if self.ih is not None:
            self.ih.stop()
            self.ih = None


class Button(Input):
    """
    Extends input class to define a button
    """
    def __init__(self, pin):
        Input.__init__(self, pin)


class Tilt(Input):
    """
    Extends input class to define digital tilt switch
    """
    def __init__(self, pin):
        Input.__init__(self, pin)

    def is_tilted(self):
        """
        Returns boolean of tilt state
        :return:
        """
        return self.is_pressed()

    def wait_for_tilt(self, timeout=None):
        """
        Pause the script until the device is tilted or the timeout is reached
        """
        if timeout is None:
            timeout = -1
        self.gpio_in.wait_for_interrupt(timeout)
