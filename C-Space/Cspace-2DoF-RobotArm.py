import matplotlib.pyplot as plt
import numpy as numpy


class Canvas():
    def __init__(self):
        
        self.fig = plt.figure("World")

        self.ax = plt.axes([0.1,0.1,0.785,0.785])
        plt.xlim(-5,+5)
        plt.ylim(-5,+5)

        plt.show()


if __name__ == "__main__":
    c = Canvas()