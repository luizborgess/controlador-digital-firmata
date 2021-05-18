from pyfirmata import Arduino as Ard
from pyfirmata import util, INPUT, OUTPUT, PWM
import serial.tools.list_ports
import json


class Arduino:

    def get_ports(self):
        self.COMports = []
        ports = list(serial.tools.list_ports.comports())
        # Clear existente durante refresh
        self.listport.clear()
        self.COMports.clear()
        for i, p in enumerate(ports):
            self.listport.addItem(p[1])
            self.COMports.append(p[0])
            if "Arduino" in p[1]:
                self.listport.setCurrentIndex(i)

    def define_board(self):
        self.connect.setEnabled(False)
        self.board = Ard(self.COMports[self.listport.currentIndex()])  # change com port
        print("Communication Successfully started")
        self.checkBox.setStyleSheet("QCheckBox::indicator"
                                    "{"
                                    "background-color : lightgreen;"
                                    "}")
        self.checkBox.setEnabled(True)

        self.it = util.Iterator(self.board)
        self.it.start()

    # set_1 define ports
    def define_ports(self):
        self.analogPort = int(self.textBox1.text())
        self.pwmPort = int(self.textBox2.text())
        # time in mili seconds
        self.sampleTime = float(self.textBox3.text())
        #Time in seconds
        self.sampleTimeSec=self.sampleTime/1000

        print("analog port:", self.analogPort)
        print("Pwm port", self.pwmPort)
        print("Sample Time", self.sampleTime)

        self.board.analog[self.analogPort].mode = INPUT
        self.board.digital[self.pwmPort].mode = PWM

        # update config
        self.data['AnalogPort'] = str(self.analogPort)
        self.data['PwmPort'] = str(self.pwmPort)
        self.data['SampleTime'] = str(self.sampleTime)
        with open('Settings.json', 'w+') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False)
        json_file.close()

    def clear_1(self):
        self.textBox1.setText('')
        self.textBox2.setText('')
        self.textBox3.setText('')