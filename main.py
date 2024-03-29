from PyQt5 import QtWidgets, uic
import sys
import os
from Graph import DrawGraph
from Arduino import Arduino
from Control import Control
from jsonHandler import JsonHandler
from UpdateGraph import UpdateGraph

# define main path for pyinstaller
try:
    os.chdir(sys._MEIPASS)
except:
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        Locale=JsonHandler.json_read_locale(self)
        uic.loadUi(Locale, self)

        # Load software config
        JsonHandler.json_read(self)
        # Load current ports
        Arduino.get_ports(self)
        # Draw initial graph
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
        self.pause.clicked.connect(lambda: DrawGraph.graph_pause(self))
        self.updateSetPoint.clicked.connect(lambda: Control.update_setpoint(self))

        # enable cursor
        self.enableCursor.stateChanged.connect(lambda: DrawGraph.cursor(self))
        # enable grid
        self.enableGrid.stateChanged.connect(lambda: DrawGraph.grid(self))
        # clear graph
        self.clear_3.clicked.connect(lambda: DrawGraph.graph_clear(self))
        # show setpoint
        self.enableSetPoint.stateChanged.connect(lambda: DrawGraph.enable_set_point(self))
        # save csv
        self.saveCsv.clicked.connect(lambda: JsonHandler.save_csv(self))
        # load csv
        self.loadCSV.clicked.connect(lambda: JsonHandler.load_csv(self))
        # clear pid params
        self.clear_2.clicked.connect(lambda: Control.clear_PIDparams(self))

        # set tooltip
        self.label_17.setToolTip("SetPoint")
        self.label_18.setToolTip("Variável de Processo")
        self.label_14.setToolTip("Proporcional")
        self.label_15.setToolTip("Integrador")
        self.label_16.setToolTip("Derivativo")

        self.got_csv = False

    # define call mouse update from update graph
    mouse_update = UpdateGraph.mouse_update


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
