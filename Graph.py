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
        self.graphWidget.setRange(padding=0, xRange=[0, self.graphRange], yRange=[0, 5])
        self.graphWidget.showGrid(x=True, y=True)
        # define initial setpoint
        self.sp = 0
        self.graph_started=False
        # self.proxy = pg.SignalProxy(self.graphWidget.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_update)

    def graph(self):
        self.graphWidget.enableAutoRange(axis='y', enable=False)
        #pen 1
        pen = pg.mkPen(color=(0, 136, 255), width=2)
        #pen 2
        pen2=pg.mkPen(color='r', width=2)
        #curve 1 response
        self.curve = self.graphWidget.plot(pen=pen)
        #curve 2 disturbance
        self.curve2 = self.graphWidget.plot(pen=pen2)

        self.timer = QtCore.QTimer()
        # sample time
        self.timer.setInterval(self.sampleTime)
        self.timer.timeout.connect(lambda: UpdateGraph.update_plot_data(self))
        self.timer.start()
        self.y = np.array([])
        self.y2=np.array([])
        # tempo
        self.temp = np.array([])

        self.graph_started=True
        # plot position
        self.ptr = 0.0
        if self.radioButton.isChecked():
            self.board.digital[int(self.pwmPort)].write(float(self.pwmValue))

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

    def enable_set_point(self):
        #colours
        #single-character string representing color (b, g, r, c, m, y, k, w)

        if self.enableSetPoint.isChecked():
            pen3 = pg.mkPen(color=(0, 128, 128), width=2)
            self.sp_line = pg.InfiniteLine(angle=0, movable=False, pen=pen3)
            self.graphWidget.addItem(self.sp_line, ignoreBounds=True)
            self.sp_line.setPos(self.sp)

        else:
            self.graphWidget.removeItem(self.sp_line)
