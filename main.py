from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os
import random
from pyfirmata import Arduino, util, INPUT,OUTPUT
import serial.tools.list_ports

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)



        #self.setStyleSheet("background-color: white;")
        uic.loadUi('basic.ui', self)
        #self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)

        # button connect pointer
        #self.connect = self.findChild(QtWidgets.QPushButton, 'connect')  # Find the button
        # combobox pointer
        #self.listport = self.findChild(QtWidgets.QComboBox, 'listport')

        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.listport.addItem(p[1])


        # actions
        self.connect.clicked.connect(self.arduino)
        self.start.clicked.connect(self.graph)


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



    def arduino(self):
        self.connect.setEnabled(False)
        self.board = Arduino("COM3")  # change com port
        print("Communication Successfully started")
        self.board.analog[0].mode = INPUT
        self.board.digital[2].mode=OUTPUT
        self.board.digital[2].write(1)

        self.it = util.Iterator(self.board)
        self.it.start()

    def update_plot_data(self):
        self.x = self.x[1:] 
        self.x.append(self.x[-1] + 1)  

        self.y = self.y[1:] 
        self.y.append(self.board.analog[0].read())
        #self.y.append(randint(0, 100))  

        self.data_line.setData(self.x, self.y)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())