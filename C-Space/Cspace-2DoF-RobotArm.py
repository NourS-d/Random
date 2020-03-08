import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, RectangleSelector
from matplotlib.patches import Rectangle


class Canvas():
    def __init__(self):
        
        # List of Obstacles
        self.objects = []

        # Figure
        self.fig = plt.figure("World", (7,7))

        self.ax = plt.axes([0.1,0.1,0.785,0.785])
        plt.xlim(-5,+5)
        plt.ylim(-5,+5)

        axbutton = plt.axes([0.51, 0.01, 0.15, 0.035])  
        self.buttonP = Button(axbutton, 'Add Rectangle')
        self.buttonP.on_clicked(self.drawRectangle)

        plt.show()

    def drawRectangle(self, click):
        print("Click, hold, and draw to draw rectangle.\n\n")
        self.rs = RectangleSelector(self.ax, self._drawRectangleEvent,
                        lineprops=dict(linewidth=1, alpha=0.6, color='k'),
                        drawtype='box', useblit=False, button=[1])

    def _drawRectangleEvent(self,eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        rect = Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2) , color=np.random.rand(3,))
        self.ax.add_patch(rect)
        self.objects.append(rect)
        del self.rs



if __name__ == "__main__":
    c = Canvas()