import matplotlib.pyplot as plt
import numpy as np

SIZE = 10
plt.rcParams["figure.figsize"] = (SIZE,SIZE)

class Pendulum():

    def __init__(self):
        # Base Dimensions 
        self.base_width = 1
        self.base_height = 0.2

        # Wheel Radius
        self.wheel_radius = 0.1

        # Ball Radius
        self.ball_radius = 0.1

        # Bar Length
        self.bar_length = 1.5

        
    def plot_pendulum(self,xt,theta, radians = True):
        
        # Clear figure
        plt.clf()

        if not radians:
            theta = np.radians(theta)

        # Model Coordiates
        base_xy =[-self.base_width/2, self.base_height/2]  # Base coordiates
        
        wr_xy = [self.base_width/2 - self.wheel_radius, -self.base_height/2+self.wheel_radius]  # Right Wheel
        wl_xy = [-self.base_width/2 + self.wheel_radius, -self.base_height/2+self.wheel_radius] # Left Wheel

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
        plt.xlim([-SIZE / 2, SIZE / 2])
        plt.ylim([-1.1 * self.bar_length, SIZE - 1.1 * self.bar_length])
        plt.pause(0.01)

P= Pendulum()
for x in range(0,50,1):
    x=x/10
    P.plot_pendulum(x,0)