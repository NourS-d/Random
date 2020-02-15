import matplotlib.pyplot as plt
import numpy as np

SIZE = 10
plt.rcParams["figure.figsize"] = (SIZE,SIZE)

def plot_pendulum(xt,theta, radians = True):

    if not radians:
        theta = np.radians(theta)
    
    # Base Dimensions 
    base_width = 1
    base_height = 0.2

    # Wheel Radius
    wheel_radius = 0.1

    # Ball Radius
    ball_radius = 0.1

    # Bar Length
    bar_length = 1.5

    # Model Coordiates
    base_xy =[-base_width/2,base_height/2]  # Base coordiates
    
    wr_xy = [base_width/2 - wheel_radius, -base_height/2+wheel_radius]  # Right Wheel
    wl_xy = [-base_width/2 + wheel_radius, -base_height/2+wheel_radius] # Left Wheel

    bar_xs = np.array([0, bar_length * np.sin(-theta)])
    bar_ys = np.array([base_height, bar_length * np.cos(-theta) + base_height])

    base_xy[0] += xt
    wr_xy[0] += xt
    wl_xy[0] += xt
    bar_xs += [xt,xt]
    
    # Model Shapes and Plot
    # Cart
    base = plt.Rectangle(base_xy, base_width, base_height,
                        fc="#073642",
                        ec="#2E3436")

    wheel_r = plt.Circle(wr_xy, wheel_radius,
                        fc="#469EBD",
                        ec="#469EBD",
                        )
    wheel_l = plt.Circle(wl_xy, wheel_radius,
                        fc="#469EBD",
                        ec="#469EBD",
                        )
    plt.gca().add_patch(base)
    plt.gca().add_patch(wheel_l)
    plt.gca().add_patch(wheel_r)

    # Pendulum
    ball = plt.Circle((bar_xs[1], bar_ys[1]), ball_radius,
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
    plt.ylim([-1.1 * bar_length, SIZE - 1.1 * bar_length])
    plt.show()

plot_pendulum(1,0, False)