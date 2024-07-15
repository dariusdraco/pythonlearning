class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        z = Complex()
        z.real = self.real + other.real
        z.imag = self.imag + other.imag
        return z

    def __sub__(self, other):
        z = Complex()
        z.real = self.real - other.real
        z.imag = self.imag - other.imag
        return z

c1 = Complex(1.1, 0.2)
c2 = Complex(1.1, 0.2)
c3 = c1 + c2
c3.display()  # Assuming you still have a display method

c4 = c1 - c2
c4.display()  # Assuming you still have a display method
