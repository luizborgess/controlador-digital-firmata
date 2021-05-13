from PyQt5 import QtWidgets, QtCore, uic
import sys
import os
from Graph import DrawGraph
from Arduino import Arduino
from Control import Control
import json

# define main path for pyinstaller
try:
    os.chdir(sys._MEIPASS)
except:
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('GUI_en.ui', self)

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
        self.clear.clicked.connect(lambda: Arduino.clear_1(self))
        self.pause.clicked.connect(lambda: DrawGraph.graph_pause(self))
        # load software config
        with open('Settings.json', 'r') as json_file:
            self.data = json.load(json_file)
        self.textBox1.setText(self.data['AnalogPort'])
        self.textBox2.setText(self.data['PwmPort'])
        self.textBox3.setText(self.data['SampleTime'])
        json_file.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
