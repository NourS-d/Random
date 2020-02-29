import matplotlib.pyplot as plt
import numpy as np
SIZE = 10
plt.rcParams["figure.figsize"] = (SIZE,SIZE)

# This simulation is based on the lesson by Brian Douglas 
# on the MathWorks page
# https://www.mathworks.com/videos/state-space-part-4-what-is-lqr-control-1551955957637.html

SCALE =0.285

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
        
        # System Dynamic Model
        self._A = np.array( [[0.0, 1],
                             [0.1, 0]
                             ])
        self._B = np.array([[0],[1]])
        self._C = np.array( [1, 0])
        self._D = np.array([0])

        self.dt = 0.05

        # Fuel Level
        self.fuel = 0

    def run_step(self, x, u):
        x0 = x[1,0] # nitial velocity
        print(x0)
        x_dot = np.dot(self._A, x) + np.dot(self._B, u)
        #y = np.dot(self._C, x) + np.dot(self._C, u)

        x += self.dt* x_dot

        x1 = x[1,0] # New velocity
        
        acc =  (x1 - x0)/self.dt

        # Fuel is proportional to the integral of acceleration
        self.fuel = self.fuel + SCALE * abs(acc)

        return x

    def get_model(self):
        """Return the state space model of the system (A,B,C,D)
        
        """
        return self._A, self._B, self._C, self._D

    def update_model(self, A=None, B=None, C=None, D=None):
        """
        Updates the state space model.
        """
        self._A = self._check_update_matrix(self._A, A)
        self._B = self._check_update_matrix(self._B, B)
        self._C = self._check_update_matrix(self._C, C)
        self._D = self._check_update_matrix(self._D, D)

        print("New model: \n")
        self.print_ss()

    def _check_update_matrix(self, A0, A1):
        if A1 is not None:
            A1 = np.array(A1)
            if A1.shape == A0.shape:
                return A1
            else:
                print("The following matrix has the wrong shape: ")
                print(A1)
                print("Please make sure it is of shape ", A0.shape)
        return A0

    def print_ss(self):
        print("A=\n{}\n\nB=\n{}\n\nC=\n{}\n\nD=\n{}\n".format(self._A, self._B,
                                                            self._C ,self._D))
        
    def plot_ufo(self, alpha, xy = [0, 4.5], degrees = False):
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
        plt.fill(ufo_x,ufo_y)
        plt.text(0,-0.5, "Fuel: {}".format(self.fuel))
        plt.axis("equal")
        plt.xlim([-SIZE / 2, SIZE / 2])
        plt.ylim([-1, SIZE + 1])
        plt.pause(0.001)

if __name__ == "__main__":
    ufo = UFO()
    ufo.plot_ufo(np.pi/2,[1,2])
    plt.show()
    ufo.plot_ufo(0,[1,2])
    plt.show()