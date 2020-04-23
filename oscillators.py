"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Instructor: Prof. Brian Drake
Course: MTH 302-02
Program: Project 3 - Salty Tanks

@date Friday, April 17, 2020
@author Scott VandenToorn
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import math as m


# ---------------------------------------------------------------------------
#  Functions
# ---------------------------------------------------------------------------

""" y(t) for part 1 """
def y(t):
  return exp(-1.5 * t) * ((2 * cos(2 * t) + 1.5 * sin(2 * t)))

""" y(t) for part 2 """
def y_2(t):
  return (7 / 3) * exp(-t) - (1 / 3) * exp(-7 * t)

def u(t):
  return exp(-(t - 5)) - exp(-7 * (t - 5))


# ---------------------------------------------------------------------------
#  Driver code
# ---------------------------------------------------------------------------

##############    Part 1    ##############
y_vals = []
x = []

for i in range(1500):
  x.append(i * 0.01)

for t in range(1500):
  y_vals.append(y(t * 0.01))

###   logarithmic decrement   ###
max_a = max(y_vals[250 : 350])
max_b = max(y_vals[500 : 950])
max_c = y_vals[942]
max_d = y_vals[1256]
idx_a = y_vals.index(max_a)
idx_b = y_vals.index(max_b)
idx_c = y_vals.index(max_c)
idx_d = y_vals.index(max_d)

print('\n\n')
print('ya:\n   value =', round(max_a, 8))
print('   index =', idx_a)
print('yb:\n   value =', round(max_b, 8))
print('   index =', idx_b)
print('Logarithmic Decrement:\t', round(log(max_a / max_b), 3))
print('pi * c / m * B:\t\t', round((m.pi * 12) / (4 * 2), 3))

print('\n\n')
print('yc:\n   value =', max_c)
print('   index =', idx_c)
print('yd:\n   value =', max_d)
print('   index =', idx_d)
print('Logarithmic Decrement:\t', round(log(max_c / max_d), 3))
print('pi * c / m * B:\t\t', round((pi * 12) / (4 * 2), 3))

print('\n\n')

###   Plot y(t)   ###
# plt.plot(x, y_vals)
# plt.title('Plot of y(t) (Part 1)')
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.grid()
# plt.show()


##############    Part 2    ##############
###   Plot y(t)   ###
y_2_vals = []

for t in range(1500):
  if t <= 500: y_2_vals.append(y_2(t * 0.01))
  else: y_2_vals.append(u(t * 0.01))

plt.plot(x, y_2_vals)
plt.title('Plot of y(t) (Part 2)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid()
plt.show()

