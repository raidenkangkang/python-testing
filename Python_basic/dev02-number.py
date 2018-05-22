'''
3 number system: int, float, complex
'''
import numpy as np
import matplotlib.pyplot as plt

#program start
num_one = 100
print(type(num_one))

num_two = 3.141592678
print(type(num_two))

#showing e+36, 36's zero
print(num_two*100000000000000000000000000000000)

#some function with imported modules
x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)

plt.plot(x,y)
plt.show()