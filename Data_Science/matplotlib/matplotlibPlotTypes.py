import numpy as np
import matplotlib.pyplot as plt

# Histograms
# Gaussian bell curve, Standard normal distribution.
mu, sigma = 172, 4
x = mu + sigma * np.random.randn(10000)
plt.hist(x, 100, density=True, facecolor="blue")
plt.xlabel("Height")
plt.ylabel("Probability")
plt.title("Height of Students")
plt.text(160, 0.125, "μ = 172, σ = 4")
plt.axis([155, 190, 0, 0.15])
plt.grid(True)
plt.show()

# Bar Chart
bob = (90, 67, 87, 76)
charles = (80, 80, 47, 66)
daniel = (40, 95, 76, 89)

skills = ("Python", "Java", "Networking", "Machine Learning")

width = 0.2
index = np.arange(4)
plt.bar(index, bob, width=width, label="Bob")
plt.bar(index + width, charles, width=width, label="Charles")
plt.bar(index + width * 2, daniel, width=width, label="Daniel")

plt.xticks(index + width, skills)
plt.ylim(0, 120)
plt.title("IT Skill Levels")
plt.ylabel("Skill Level")
plt.xlabel("IT Skill")
plt.legend()
plt.show()

# Pie Chart
labels = ('American', 'German', 'French', 'Other')
values = (47, 23, 20, 10)
plt.pie(values, labels=labels, autopct="%.2f%%", shadow=True)
plt.title("Student Nationalities")
plt.show()

# Scatter Plots
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y)
plt.show()

# Boxplot
mu, sigma = 172, 4
values = np.random.normal(mu, sigma, 200)
plt.boxplot(values)
plt.title("Student's Height")
plt.ylabel("Height")
plt.show()

# 3D plots
from mpl_toolkits import mplot3d
z = np.linspace(0, 20, 100)
x = np.sin(z)
y = np.cos(z)
ax  = plt.axes(projection='3d')
ax.plot3D(x,y,z)
plt.show()

# Surface Plots
ax = plt.axes(projection='3d')
def z_function(x,y):
    return np.sin(np.sqrt(x ** 2  + y ** 2))
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X,Y = np.meshgrid(x,y)
Z = z_function(X,Y)
ax.plot_surface(X,Y,Z)
plt.show()
