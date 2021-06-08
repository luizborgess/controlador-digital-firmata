import pyqtgraph as pg
from PyQt5 import QtCore
from UpdateGraph import UpdateGraph
import numpy as np


class DrawGraph:

    def __init__(self):
        self.proxy = None

    def initial_graph(self):
        # Configuraçoes iniciais do grafico
        self.graphWidget.setBackground('#ececec')
        # self.graphWidget.setConfigOption(background='None')
        # self.graphWidget.viewRect()
        # self.graphWidget.setConfigOption('foreground', 'k')
        self.graphWidget.setRange(padding=0, xRange=[0, self.graphRange])
        self.graphWidget.showGrid(x=True, y=True)
        # self.proxy = pg.SignalProxy(self.graphWidget.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_update)

    def graph(self):
        self.graphWidget.enableAutoRange(axis='y', enable=False)
        pen = pg.mkPen(color=(0, 136, 255), width=2)
        self.curve = self.graphWidget.plot(pen=pen)

        self.timer = QtCore.QTimer()
        # sample time
        self.timer.setInterval(self.sampleTime)
        self.timer.timeout.connect(lambda: UpdateGraph.update_plot_data(self))
        self.timer.start()
        self.y = np.array([])
        # tempo
        self.temp = np.array([])

        # plot position
        self.ptr = 0.0

    def graph_pause(self):
        self.timer.stop()

    def graph_clear(self):
        # clear previous curve
        self.curve.clear()

    def cursor(self):

        if self.enableCursor.isChecked():
            self.y_line = pg.InfiniteLine(angle=90, movable=False, pen='k')
            self.x_line = pg.InfiniteLine(angle=0, movable=False, pen='k')
            self.graphWidget.addItem(self.y_line, ignoreBounds=True)
            self.graphWidget.addItem(self.x_line, ignoreBounds=True)
            self.proxy = pg.SignalProxy(self.graphWidget.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_update)

        else:
            self.graphWidget.removeItem(self.y_line)
            self.graphWidget.removeItem(self.x_line)
            # possible bug
            self.proxy.disconnect()
            # self.proxy=None

    def grid(self):
        if self.enableGrid.isChecked():
            self.graphWidget.showGrid(x=True, y=True)
        else:
            self.graphWidget.showGrid(x=False, y=False)
