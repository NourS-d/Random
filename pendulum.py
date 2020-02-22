import matplotlib.pyplot as plt
import numpy as np

SIZE = 5
plt.rcParams["figure.figsize"] = (SIZE,SIZE)

# Gravity
g = 9.8  # [m/s^2]

class Pendulum():

    def __init__(self):
        # Base Dimensions 
        self.base_width = 1         # [m]
        self.base_height = 0.5      # [m]
        
        # Wheel Radius
        self.wheel_radius = 0.1     # [m]

        # Ball Radius
        self.ball_radius = 0.1      # [m]

        # Bar Length
        self.bar_length = 2         # [m]

        # Cart Mass
        self.M = 1                  # [kg]
        
        # Ball Mass
        self.m = 0.3                # [kg]

        # Time Step
        self.dt = 0.1             # [s]

  # Simulation
    def model_matrix(self):
        A = np.array([
            [0, 1, 0, 0],
            [0, 0, self.m * g / self.M, 0],
            [0, 0, 0, 1],
            [0, 0, g * (self.M + self.m) / (self.bar_length * self.M), 0]
            ])

        B = np.array([
            [0],
            [1 / self.M],
            [0],
            [1 / (self.bar_length * self.M)]
            ])

        return A, B

    def run_step(self, x, u):
        A, B = self.model_matrix()

        x_dot = np.dot(A, x) + np.dot(B, u).reshape((4,1))        
        x += self. dt * x_dot
        return x

    def plot_pendulum(self,xt,theta, radians = True):
        plt.figure("Simulation")

        # Clear figure
        plt.clf()

        if not radians:
            theta = np.radians(theta)

        # Model Coordiates
        base_xy =[-self.base_width/2, self.base_height/2]  # Base coordiates
        
        wr_xy = [self.base_width/2 - self.wheel_radius, abs(self.base_height/2-self.wheel_radius)]  # Right Wheel
        wl_xy = [-self.base_width/2 + self.wheel_radius, abs(self.base_height/2-self.wheel_radius)] # Left Wheel

        bar_xs = np.array([0, self.bar_length * np.sin(-theta)])
        bar_ys = np.array([self.base_height, self.bar_length * np.cos(-theta) + self.base_height])

        base_xy[0] += xt
        wr_xy[0] += xt
        wl_xy[0] += xt
        bar_xs += [xt,xt]
        
        # Model Shapes and Plot
        # Cart
        base = plt.Rectangle(base_xy, self.base_width, self.base_height,
                            fc="#073642",
                            ec="#2E3436")

        wheel_r = plt.Circle(wr_xy, self.wheel_radius,
                            fc="#469EBD",
                            ec="#469EBD",
                            )
        wheel_l = plt.Circle(wl_xy, self.wheel_radius,
                            fc="#469EBD",
                            ec="#469EBD",
                            )
        plt.gca().add_patch(base)
        plt.gca().add_patch(wheel_l)
        plt.gca().add_patch(wheel_r)

        # Pendulum
        ball = plt.Circle((bar_xs[1], bar_ys[1]), self.ball_radius,
                            zorder=10,
                            fc="#FFA000",
                            )
        pendulum_bar = plt.plot(bar_xs,bar_ys,
                                c="#CB1616",
                                lw=3,
                                )
        plt.gca().add_patch(ball)


        plt.axis("equal")
        
        if xt >SIZE or xt <-SIZE:
            plt.xlim([-SIZE / 2 + xt, SIZE / 2 + xt])
        else:
            plt.xlim([-SIZE / 2, SIZE / 2 ])
        plt.ylim([-1.1 * self.bar_length, SIZE - 1.1 * self.bar_length])
        plt.pause(0.001)

  # Paramter Update Functions
    def update_cart_dims(self, width, height, wheel_radius):
        if width <= 0 or height <= 0 or wheel_radius <= 0:
            print("Please enter positive nonzero values.")
            raise ValueError

        self.base_height = height
        self.base_width = width
        self.wheel_radius = wheel_radius

    def update_pendulum_dims(self, bar_length, ball_radius):
        if bar_length <=0 or ball_radius <= 0:
            print("Values must nonzero positives.")
            raise ValueError

        self.bar_length = bar_length
        self.ball_radius = ball_radius

    def update_masses(self, cart_mass, ball_mass):
        if cart_mass <= 0 or ball_mass <= 0:
            print("Masses must be positive nonzero values.")
            raise ValueError
        
        self.M = cart_mass
        self.m = ball_mass

if __name__ == "__main__":
    P= Pendulum()

    print(P.model_matrix())
    for x in range(0,10,1):
        x=x/10
        P.plot_pendulum(x,0)