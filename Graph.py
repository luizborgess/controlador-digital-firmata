from PyQt5 import QtCore
import pyqtgraph as pg
import random


class DrawGraph():
    def initialGraph(self):
        print('placeholder')
    def graph(self):
        self.x = list(range(50))
        self.y = [random.random() for _ in range(50)]
        self.graphWidget.setLimits(xMin=0, yMin=0, yMax=1)
        self.graphWidget.enableAutoRange(axis='y', enable=False)
        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append(self.board.analog[0].read())
        #self.y.append(randint(0, 100))

        self.data_line.setData(self.x, self.y)
