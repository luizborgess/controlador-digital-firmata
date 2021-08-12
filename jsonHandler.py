import json
from PyQt5.QtWidgets import QFileDialog
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox


## also handle csv

class JsonHandler:

    def json_read_locale(self):
        with open('Settings.json', 'r') as json_file:
            self.data = json.load(json_file)
        json_file.close()
        return self.data['Locale']

    def json_read(self):

        # Read port settings
        self.textBox1.setText(self.data['AnalogPort'])
        self.textBox2.setText(self.data['PwmPort'])
        self.textBox3.setText(self.data['SampleTime'])

        # load graphRange
        self.graphRange = self.data['GraphRange']

        # Read Control settings
        self.textBox4.setText(self.data['OpenLoopGain'])
        self.textBox5.setText(self.data['P'])
        self.textBox6.setText(self.data['I'])
        self.textBox7.setText(self.data['D'])
        self.textBox8.setText(self.data['SP'])

        # read disturbance file path
        self.file_path = self.data['FilePath']

    def update_json(self, Ports=None, Control_1=None, Control_2=None):
        if Ports:
            self.data['AnalogPort'] = str(self.analogPort)
            self.data['PwmPort'] = str(self.pwmPort)
            self.data['SampleTime'] = str(self.sampleTime)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()

        if Control_1:
            self.data['OpenLoopGain'] = str(self.pwmValue)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()

        if Control_2:
            self.data['P'] = str(self.kp)
            self.data['I'] = str(self.ki)
            self.data['D'] = str(self.kd)
            self.data['SP'] = str(self.sp)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()

    def save_csv(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            w = np.column_stack((self.temp, self.y))
            np.savetxt(path[0], w, delimiter=",")

    def load_csv(self):
        if os.path.isfile(self.file_path):
            path = QFileDialog.getOpenFileName(self, 'Load CSV', self.file_path, 'CSV(*.csv)')
        else:
            path = QFileDialog.getOpenFileName(self, 'Load CSV', os.getenv('HOME'), 'CSV(*.csv)')

        if path[0] != '':
            my_data = np.genfromtxt(path[0], delimiter=',')
            self.csv_x = my_data[:, 0]
            self.csv_y = my_data[:, 1]
            self.limite_inf = my_data[0, 2]
            self.limite_sup = my_data[1, 2]
            self.offset = my_data[2, 2]

            self.got_csv = True
            self.selectedCSV.setText(os.path.basename(path[0]))

            if self.sampleTime != my_data[3, 2]:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Tempo de amostragem definido não compatível com o tempo de amostragem do arquivo CSV !!")
                msg.setIcon(QMessageBox.Critical)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()

            # update json
            if self.data['FilePath'] != path[0]:
                self.data['FilePath'] = path[0]
                with open('Settings.json', 'w+') as json_file:
                    json.dump(self.data, json_file, ensure_ascii=False)
                json_file.close()
