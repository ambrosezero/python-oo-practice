"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates a serial number object, which begins counting at start"""
        self.start = start
        self.current_num = start

    def generate(self):
        """Returns the current number in the serial number list, 
        and iterates the list by one"""
        rtn_num = self.current_num
        self.current_num = self.current_num + 1
        return rtn_num

    def reset(self):
        """resets the serial number list back to the original start number"""
        self.current_num = self.start
