import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    plt.plot(data)
    plt.title('1D Plot')
    plt.show()


def plot_2d(x, y):
    plt.scatter(x, y)
    plt.title('2D Scatter Plot')
    plt.show()


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.title('3D Scatter Plot')
    plt.show()


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
