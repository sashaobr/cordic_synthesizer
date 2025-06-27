import numpy as np
import fxpmath

x = fxpmath.Fxp(-7.25, signed = True, n_word = 16, n_frac = 8)
y = [x, x]
z = y
y[0].set_val(0.5)
print(y)
print(z)
x.set_val(x >> 1)
x.info()