import pyqtgraph as pg
import random
from PyQt5 import QtCore
from UpdateGraph import UpdateGraph


class DrawGraph:
    def initial_graph(self):
        # Configuraçoes iniciais do grafico
        self.graphWidget.setBackground('#ececec')
        # self.graphWidget.setConfigOption(background='None')
        # self.graphWidget.viewRect()
        # self.graphWidget.setConfigOption('foreground', 'k')

    def graph(self):
        self.x = list(range(50))
        # self.y = [random.random() for _ in range(50)]
        self.y = list(range(50))
        self.graphWidget.setLimits(xMin=0, yMin=0, yMax=1)
        self.graphWidget.enableAutoRange(axis='y', enable=False)
        # self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 136, 255), width=2)
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        # sample time
        self.timer.setInterval(self.sampleTime)
        # self.timer.timeout.connect(update_plot_data(self))
        self.timer.timeout.connect(lambda: UpdateGraph.update_plot_data(self))
        self.timer.start()

