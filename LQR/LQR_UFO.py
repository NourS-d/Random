import numpy as np
import UFO
import LQR
import matplotlib.pyplot as plt

SIMULATION_TIME = 6
if __name__ == "__main__":

    # UFO Model
    ufo = UFO.UFO()    
    A, B, C, D = ufo.get_model()

    # Controller
    Q = np.array( [ [1, 0], 
                    [0, 1]
                    ])

    R = np.diag([0.1])

    lqr = LQR.LQR_Control(A,B,Q,R)

    # Initial Condition
    X  = np.array([ [3.0],
                    [0.0]
                    ])

    time = np.arange(0,SIMULATION_TIME,ufo.dt)
    thetas = []
    for i in time:

        X = ufo.run_step(X, lqr.get_u(X))
        thetas.append(X[0,0])
        ufo.plot_ufo(X[0,0])
        

    plt.figure('Response')
    plt.plot(time,thetas)
    plt.show()