import pyqtgraph as pg
from PyQt5 import QtCore
from UpdateGraph import UpdateGraph
import numpy as np


class DrawGraph:
    def initial_graph(self):
        # Configuraçoes iniciais do grafico
        self.graphWidget.setBackground('#ececec')
        # self.graphWidget.setConfigOption(background='None')
        # self.graphWidget.viewRect()
        # self.graphWidget.setConfigOption('foreground', 'k')
        self.graphWidget.setRange(padding=0, xRange=[0, self.graphRange])

    def graph(self):
        self.graphWidget.enableAutoRange(axis='y', enable=False)
        pen = pg.mkPen(color=(0, 136, 255), width=2)
        self.curve = self.graphWidget.plot(pen=pen)

        self.timer = QtCore.QTimer()
        # sample time
        self.timer.setInterval(self.sampleTime)
        self.timer.timeout.connect(lambda: UpdateGraph.update_plot_data(self))
        self.timer.start()
        self.Xm = np.array([])
        self.temp = np.array([])
        self.ptr = 0.0

    def graph_pause(self):
        self.timer.stop()
        #clear previous curve
        # self.curve.clear()
