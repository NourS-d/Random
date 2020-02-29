import matplotlib.pyplot as plt
import numpy as np
SIZE = 10
plt.rcParams["figure.figsize"] = (SIZE,SIZE)

# This simulation is based on the lesson by Brian Douglas 
# on the MathWorks page
# https://www.mathworks.com/videos/state-space-part-4-what-is-lqr-control-1551955957637.html

class UFO():
    def __init__(self):
        
        # UFO Plot
        self.__ufo_data = np.array( [
            [0.54, .12],
            [0.48, 0.24],
            [0.42, 0.31],
            [0.3, 0.4],
            [0.18, 0.45],
            [0.06, 0.48],
            [-0.06, 0.48],
            [-0.18, 0.45],
            [-0.3, 0.4],
            [-0.42, 0.31],
            [-0.48, 0.24],
            [-0.54, .12],
            [0.54, .12],
            [0.54, 0.06],
            [0.6, 0.06],
            [0.78, 0.03], 
            [0.91, 0.01],
            [0.91, 0.03],
            [1.01, 0.03],
            [1.01, -0.01],   
            [1.1, -0.03], 
            [1.26, -0.12], 
            [1.36, -0.18], 
            [1.40, -0.21],
            [1.38, -0.24],
            [1.26, -0.27],
            [1.1, -0.3],  
            [1.01, -0.32],
            [1.01, -0.34],
            [0.91, -0.34],
            [0.91, -0.32],  
            [0.72, -0.34],
            [0.48, -0.35],
            [0.72, -0.6],
            [0.62, -0.6],
            [0.38, -0.35],
            [0.3, -0.35],
            [-0.3, -0.35],
            [-0.38, -0.35],
            [-0.62, -0.6],
            [-0.72, -0.6],
            [-0.48, -0.35],
            [-0.91, -0.32],
            [-0.91, -0.34],
            [-1.01, -0.34],
            [-1.01, -0.32],
            [-1.1, -0.3],
            [-1.26, -0.27],
            [-1.38, -0.24],
            [-1.40, -0.21],
            [-1.36, -0.18],
            [-1.26, -0.12],
            [-1.1, -0.03],
            [-1.01, -0.01],
            [-1.01, 0.03],
            [-0.91, 0.03],
            [-0.91, 0.01],
            [-0.78, 0.03],
            [-0.6, 0.06],
            [-0.54, 0.06],
            [0.54, 0.06],
            ])

    def plot_ufo(self, alpha, xy, degrees = False):
        plt.figure("Simulation")
        plt.clf()
        
        # Conversion to rads
        if degrees:
            alpha = np.rad2deg(alpha)
        
        x, y = xy
        
        # Rotation
        rot = np.array( [[np.cos(alpha), -np.sin(alpha)],
                         [np.sin(alpha),  np.cos(alpha)] ])
        
        # Apply rotation and translation
        ufo_x = np.dot(self.__ufo_data, rot[0,:]) + x
        ufo_y = np.dot(self.__ufo_data, rot[1,:]) + y
        
        # Plot UFO
        plt.axis("equal")
        plt.xlim([-SIZE / 2, SIZE / 2])
        plt.fill(ufo_x,ufo_y)
        plt.show()

ufo = UFO()
ufo.plot_ufo(0.3,[1,2])