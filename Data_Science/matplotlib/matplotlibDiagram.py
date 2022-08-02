import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

## example 1
# generating x-values and y-values
x_values = np.linspace(0, 20, 100)
y_values = np.sin(x_values)

#plot
#plt.plot(x_values,y_values)
#plt.show()

## example 2
# plotting my own function
x = np.linspace(0, 10, 100)
y = (6 * x - 30) ** 2
#plt.plot(x,y)
#plt.show()

## example 3
numbers = 10 * np.random.random(100)
#plt.plot(numbers, 'bo')
#plt.show()

## example 4
# multiple graphs
x = np.linspace(0, 5, 200)
y1 = 2 * x
y2 = x ** 2
y3 = np.log(x)

#plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
#plt.show()

## example 5
# subplots
x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

#plt.subplot(211)
#plt.plot(x, y1, 'r-')
#plt.subplot(212)
#plt.plot(x, y2, 'g--')
#plt.show()

# multiple plotting windows
#style.use('ggplot') # this is for plotting style
#plt.figure(1)
#plt.plot(x, y1, 'r-')
#plt.figure(2)
#plt.plot(x, y2, 'g--')
#plt.show()

# labels and legends
x = np.linspace(10, 50, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x/3)

plt.figure("My Figure")
plt.title("Sine Function")
plt.suptitle("Data Science")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.grid(True)
plt.plot(x,y1, 'b-', label="Sine")
plt.plot(x,y2, 'r-', label="Cosine")
plt.plot(x,y3, 'g-', label="Logarithm")
plt.legend(loc='upper left')
plt.show()
plt.savefig("functions.png")
