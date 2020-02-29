import time
import matplotlib.pyplot as plt
import numpy as np
class PID_Control():
    """
    Class implemented a simple PID controller
    """
    def __init__(self,Kp, Ki, Kd, target = 0):

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.error = 0          # Current Error
        self.error_prev = 0     # Error at Previous time
        self.error_cum = 0      # Cumulative Error

        self.target = target    # Goal
        self.dt = 0.01          # delta time

    def update(self,value):
        
        self.error = self.target - value
        self.error_cum += self.error 

        P = self.Kp * self.error
        I = self.Ki * (self.error_cum) * self.dt
        D = self.Kd * (self.error - self.error_prev) / self.dt

        self.error_prev = np.copy(self.error)

        return P+I+D

    def set_target(self, target):
        """
        Update the set point for the PID
        """
        self.target = target

    def set_dt(self, dt):
        """
        Update delta t
        """
        self.dt = dt
