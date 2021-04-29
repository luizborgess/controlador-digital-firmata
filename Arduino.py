from pyfirmata import Arduino as Ard
from pyfirmata import util, INPUT, OUTPUT
import serial.tools.list_ports


class Arduino:

    def get_ports(self):
        ports = list(serial.tools.list_ports.comports())

        for i, p in enumerate(ports):
            self.listport.addItem(p[1])
            self.COMports.append(p[0])
            if "Arduino" in p[1]:
                self.listport.setCurrentIndex(i)



    def update_ports(self):
        ports = list(serial.tools.list_ports.comports())
        self.listport.clear()
        self.COMports.clear()
        for i, p in enumerate(ports):
            self.listport.addItem(p[1])
            self.COMports.append(p[0])
            if "Arduino" in p[1]:
                self.listport.setCurrentIndex(i)

    def defineBoard(self):

        self.connect.setEnabled(False)
        self.board = Ard(self.COMports[self.listport.currentIndex()])  # change com port
        print("Communication Successfully started")
        self.checkBox.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "background-color : lightgreen;"
                               "}")
        self.checkBox.setEnabled(True)
        #define ports
        self.board.analog[0].mode = INPUT
        self.board.digital[13].mode = OUTPUT
        self.board.digital[2].mode = OUTPUT

        self.board.digital[2].write(1)

        self.it = util.Iterator(self.board)
        self.it.start()

"""

    def ledTest(self):
        if self.checkBox.isChecked():
            self.board.digital[13].write(1)
        else:
            self.board.digital[13].write(0)
"""
