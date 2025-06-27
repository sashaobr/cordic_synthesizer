import numpy as np
import fxpmath

number_of_iterations = 40
xi = fxpmath.Fxp(1, signed = True, n_word = 64, n_frac = 32)
yi = fxpmath.Fxp(0, signed = True, n_word = 64, n_frac = 32)
xip1 = fxpmath.Fxp(-7.25, signed = True, n_word = 64, n_frac = 32)
yip1 = fxpmath.Fxp(-7.25, signed = True, n_word = 64, n_frac = 32)

desired_angle = np.pi/4
beta = desired_angle

K_40 = 1
for i in range(number_of_iterations):
    K_40 = K_40 * 1/(np.sqrt(1 + 2**(-2*i)))

gamma = np.zeros(number_of_iterations)
for i in range(number_of_iterations):
    gamma[i] = np.arctan(2**(-i))

sigma = 1
for i in range(number_of_iterations):
    if (beta >= 0):
        sigma = 1
    else:
        sigma = -1

    beta = beta - sigma*gamma[i]

    xip1.set_val(xi - sigma*(yi >> i))
    yip1.set_val(sigma*(xi >> i) + yi)

    xi.set_val(xip1)
    yi.set_val(yip1)

    print((xip1,yip1))

xip1.set_val(xip1*K_40)
yip1.set_val(yip1*K_40)
print((xip1,yip1))
#print(np.arctan(v_n[1]/v_n[0]))
 
