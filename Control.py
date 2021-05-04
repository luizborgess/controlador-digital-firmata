import pyqtgraph as pg
import random
from PyQt5 import QtCore

from pyfirmata import Arduino as Ard
from pyfirmata import util, INPUT, OUTPUT, PWM
import serial.tools.list_ports


class Control:
    def on_clicked(self):
        if self.radioButton.isChecked():
            self.label_10.setEnabled(True)
            self.textBox4.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.set_3.setEnabled(True)
            self.label_6.setEnabled(False)
            self.label_7.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.label_8.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.label_9.setEnabled(False)
            self.lineEdit_6.setEnabled(False)
            self.set_2.setEnabled(False)
            self.clear_2.setEnabled(False)
        if self.radioButton_2.isChecked():
            self.label_10.setEnabled(False)
            self.lineEdit_7.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.set_3.setEnabled(False)
            self.label_6.setEnabled(True)
            self.label_7.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.label_8.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.label_9.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.set_2.setEnabled(True)
            self.clear_2.setEnabled(True)

    def open_loop(self):
        self.pwmValue=self.textBox4.text()
        self.board.digital[int(self.pwmPort)].write(float(self.pwmValue))
