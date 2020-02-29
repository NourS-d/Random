import numpy as np
import scipy
from scipy import signal
import UFO
import matplotlib.pyplot as plt

SIMULATION_TIME = 6
if __name__ == "__main__":

    ufo = UFO.UFO()

    A, B, C, D = ufo.get_model()
    Q = np.array( [ [1, 0], 
                    [0, 1]
                    ])

    R = np.diag([1])

    # Riccati Equation
    P = scipy.linalg.solve_continuous_are(A,B,Q,R)

    # LQR Gain
    K = np.dot(np.dot(np.linalg.inv(R),np.transpose(B)), P)

    # Initial Condition
    X  = np.array([ [3.0],
                    [0.0]
                    ])

    # Target
    target = np.array([[0]])
    thetas = []

    time = np.arange(0,SIMULATION_TIME,ufo.dt)
    for i in time:
        u = target - np.dot(K,X) 
        X = ufo.run_step(X, u)
        thetas.append(X[0,0])
        ufo.plot_ufo(X[0,0])
        

    plt.figure('Response')
    plt.plot(time,thetas)
    plt.show()