import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal

class LQR_Control():
    """
    Continuous Infinite Horizon Linear Quadratic Control

    """
    def __init__(self, A, B, Q, R, target = 0):
        
        self.Q = Q
        self.R = R

        self. K = self._get_K(A,B,Q,R)
        self.target = target
    
    def get_u(self, x, target = None):
        if target is not None:
            self.target = target
        
        u = self.target - np.dot(self.K,x)
        return u 

    def _get_K(self, A, B, Q, R):
        # Ricatti Equation
        P = scipy.linalg.solve_continuous_are(A,B,Q,R)

        # Get feedback
        K = np.dot(np.dot(np.linalg.inv(R),np.transpose(B)), P)
        return K
