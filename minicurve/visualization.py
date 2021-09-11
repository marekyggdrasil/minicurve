import numpy as np
import matplotlib.pyplot as plt

from minicurve.curve import MiniCurve


class Visualizer:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

        self.field = []
        self.points = []

    def makeField(self):
        field = MiniCurve(self.a, self.b, self.p)
        self.field = field.getAllNaive()

    def makeArrows(self, Raxs, Rays, P):
        if self.axs is None:
            raise ValueError('First you need to run generatePlot()')
        if None in Raxs and None in Rays:
            Raxs[Raxs.index(None)] = 0
            Rays[Rays.index(None)] = 0
        for k in range(len(Raxs)-1):
            ox, oy = Raxs[k], Rays[k]
            dx, dy = Raxs[k+1], Rays[k+1]
            self.axs.arrow(ox, oy, dx-ox, dy-oy,
                           head_width=P.arrow_thickness*P.arrow_head,
                           length_includes_head=True,
                           color=P.arrow_color,
                           width=P.arrow_thickness)

    def generatePlot(self, title=None, addition=False):
        self.fig, self.axs = plt.subplots(1, 1)
        if len(self.field) > 0:
            sols_x = []
            sols_y = []
            for x, y in self.field:
                if x is None and y is None:
                    sols_x.append(0)
                    sols_y.append(0)
                    continue
                sols_x.append(x)
                sols_y.append(y)
            self.axs.scatter(sols_x, sols_y, zorder=1)
        for P in self.points:
            self.axs.scatter(P.x, P.y, color=P.color)
            if P.label is not None:
                self.axs.annotate(P.label,
                                  (P.x + P.x_delta, P.y + P.y_delta))
            if P.tracing:
                Raxs = list(P.rxs)
                Rays = list(P.rys)
                self.makeArrows(Raxs, Rays, P)
        if addition:
            for P in self.points:
                if P.parent is not None:
                    p1x, p1y, p2x, p2y = P.parent
                    self.makeArrows([p1x, P.x], [p1y, P.y], P)
                    self.makeArrows([p2x, P.x], [p2y, P.y], P)
        self.axs.set_title(title)
        self.axs.set_xticks(range(self.p))
        self.axs.set_yticks(range(self.p))
        self.axs.set_xlim([-1, self.p])
        self.axs.set_ylim([-1, self.p])
        self.axs.set_axisbelow(True)
        self.axs.grid()
        return self.axs

    def plot(self, filename):
        if self.axs is None:
            raise ValueError('First you need to run generatePlot()')
        plt.tight_layout()
        self.fig.savefig(filename)

