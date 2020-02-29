import numpy as np
import matplotlib.pyplot as plt
import pendulum
from PID import PID_Control

if __name__ =="__main__":

    P = pendulum.Pendulum()
    PID = PID_Control(150,2,10) # Some values for Kp, Ki and Kd

    # Initial Condition
    X  = np.array([ [0],
                    [0],
                    [0.4],
                    [0]]
                    )

    thetas = [float(X[2])]
    for i in range(0,100):

        u = PID.update(float(X[2]))

        X = P.run_step(X,u)

        x = float(X[0])
        theta = float(X[2])
        thetas.append(theta)
    
        P.plot_pendulum(x,theta)
    
    plt.figure('Response')
    plt.plot(thetas)
    plt.show()