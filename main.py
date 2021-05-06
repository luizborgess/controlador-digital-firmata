# utilizar pyinstaller
from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
import random
from Graph import DrawGraph
from Arduino import Arduino
from Control import Control


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.setStyleSheet("background-color: white;")
        uic.loadUi('GUI_en.ui', self)
        # self.graphWidget = pg.PlotWidget()
        # self.setCentralWidget(self.graphWidget)

        # button connect pointer
        # self.connect = self.findChild(QtWidgets.QPushButton, 'connect')

        Arduino.get_ports(self)
        DrawGraph.initial_graph(self)
        # actions
        self.connect.clicked.connect(lambda: Arduino.define_board(self))
        self.start.clicked.connect(lambda: DrawGraph.graph(self))
        self.refresh.clicked.connect(lambda: Arduino.get_ports(self))
        self.set_1.clicked.connect(lambda: Arduino.define_ports(self))
        self.radioButton.toggled.connect(lambda: Control.on_clicked(self))
        self.radioButton_2.toggled.connect(lambda: Control.on_clicked_2(self))
        self.set_3.clicked.connect(lambda: Control.open_loop(self))
        self.set_2.clicked.connect(lambda: Control.set_PIDparams(self))


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
