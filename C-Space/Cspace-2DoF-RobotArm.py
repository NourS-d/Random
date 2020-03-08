import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, RectangleSelector, PolygonSelector, EllipseSelector
from matplotlib.patches import Rectangle, Polygon, Ellipse

# Robot Arm Params
L1 = 2
L2 = 1.5

# Resolution
RES = 360

class Canvas():
    def __init__(self):
        
        # List of Obstacles
        self.objects = []

        # Robot Params
        self.l1 = L1
        self.l2 = L2

        # C-space Matrix
        self.image = np.zeros((RES,RES,3), dtype = np.uint8)
        self.image.fill(255)

        # Figure
        self.fig = plt.figure("World", (7,7))

        self.ax = plt.axes([0.1,0.1,0.785,0.785])
        plt.xlim(-5,+5)
        plt.ylim(-5,+5)

        # Buttons
        axbutton = plt.axes([0.51, 0.01, 0.15, 0.035])  
        self.buttonP = Button(axbutton, 'Add Rectangle')
        self.buttonP.on_clicked(self.drawRectangle)

        axbutton = plt.axes([0.31, 0.01, 0.15, 0.035])  
        self.buttonC = Button(axbutton, 'Add Circle')
        self.buttonC.on_clicked(self.drawCircle)

        axbutton = plt.axes([0.11, 0.01, 0.15, 0.035])  
        self.buttonR = Button(axbutton, 'Add Polygon')
        self.buttonR.on_clicked(self.drawPolygon)

        axbutton = plt.axes([0.71, 0.01, 0.15, 0.035])  
        self.buttonU = Button(axbutton, 'Show C-Space')
        self.buttonU.on_clicked(self.updateCSpace)

        plt.show()

    def updateCSpace(self, click):
        fig = plt.figure("C-Space")
        ax = fig.add_subplot(1, 1, 1)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        plt.yticks((0, RES/2, RES-1), (r'0', r'180', r'360'), color='k', size=10)
        plt.xticks((0, RES/2, RES-1), (r'0', r'180', r'360'), color='k', size=10)

        plt.imshow(self.image,origin="lower")
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
        self._addPatch(rect)

    def drawCircle(self,click):
        print("Click, hold, and drag to draw circle.\n\n")

        self.rs = EllipseSelector(self.ax, self._drawCircleEvent,
                        lineprops=dict(linewidth=1, alpha=0.6, color='k'),
                        drawtype='box', useblit=False, button=[1])

    def _drawCircleEvent(self,eclick,erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        el = Ellipse( ((x2+x1)/2.0,(y2+y1) /2.0), np.abs(x1-x2), np.abs(y1-y2) , color=np.random.rand(3,))
        self._addPatch(el)

    def drawPolygon(self,click):
        print("Click somewhere on the screen to start drawing the polygon.\n\n")

        self.rs = PolygonSelector(self.ax, self._drawPolygonEvent,markerprops=dict(markersize=1),
                                    lineprops=dict(linewidth=1, alpha=0.6, color='k'))

    def _drawPolygonEvent(self, points):
        polygon = Polygon(np.array(points), color=np.random.rand(3,))
        self._addPatch(polygon)
    
    def _addPatch(self, patch):
        del self.rs

        # In case clicked without hold
        if all(np.linalg.norm(x) == np.linalg.norm(patch.get_verts()[0]) for x in patch.get_verts()):
            return
        self.objects.append(patch)
        self.ax.add_patch(patch)
        print("You currently have {} obstacles.".format(len(self.objects)))

if __name__ == "__main__":
    c = Canvas()