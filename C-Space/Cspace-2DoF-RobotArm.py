import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, RectangleSelector, PolygonSelector, EllipseSelector
from matplotlib.patches import Rectangle, Polygon, Ellipse

"""
Draws the C-Space of a 2 link robotic manipulator.

Assumes the the robot doesn't collide with it's self
and that the base of the robot is at (0,0)

Positive angles are counter clockwise.
"""
# Robot Arm Params
L1 = 2
L2 = 1.5

# Resolution
RES = 360


LIMIT = 1.5 * (L1 + L2) 
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
        plt.xlim(-LIMIT,+LIMIT)
        plt.ylim(-LIMIT,+LIMIT)

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

        c2 = plt.Circle((0,0),self.l1+self.l2,fill = 'grey', alpha=0.05)
        c1 = plt.Circle((0,0),self.l1,fill = 'grey', alpha=0.1)
        self.ax.add_artist(c1)
        self.ax.add_artist(c2)
        
        plt.show()

    def updateCSpace(self,click):
        for patch in self.objects:
            for i in range(RES):
                a1 = i * 2 * np.pi / RES
                x1 =  np.cos(a1) * self.l1;
                y1 =  np.sin(a1) * self.l1;
                pt1 = self.ax.transData.transform((x1,y1))
                if patch.contains_point(pt1):
                    self.image[:,i,0]= patch._facecolor[0]*255
                    self.image[:,i,1]= patch._facecolor[1]*255
                    self.image[:,i,2]= patch._facecolor[2]*255
                else:
                    for j in range(RES):
                        a2 = (i+j) * 2 * np.pi / RES
                        x2 =  x1 + np.cos(a2) * self.l2;
                        y2 =  y1 + np.sin(a2) * self.l2;
                        pt2 = self.ax.transData.transform((x2,y2))
                        if patch.contains_point(pt2):
                            self.image[j,i,0]= patch._facecolor[0]*255
                            self.image[j,i,1]= patch._facecolor[1]*255
                            self.image[j,i,2]= patch._facecolor[2]*255

        self._drawCSPace()

    def _drawCSPace(self):
        fig = plt.figure("C-Space")
        ax = fig.add_subplot(1, 1, 1)
        
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        plt.yticks((0, RES/2, RES-1), (r'0', r'180', r'360'), color='k', size=10)
        plt.xticks((0, RES/2, RES-1), (r'0', r'180', r'360'), color='k', size=10)
        plt.xlabel("theta 1")
        plt.ylabel("theta 2")

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