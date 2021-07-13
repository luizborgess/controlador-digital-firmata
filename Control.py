from jsonHandler import JsonHandler


class Control:
    def on_clicked(self):
        if self.radioButton.isChecked():
            self.label_10.setEnabled(True)
            self.textBox4.setEnabled(True)
            self.set_3.setEnabled(True)
            self.label_6.setEnabled(False)
            self.label_7.setEnabled(False)
            self.textBox5.setEnabled(False)
            self.label_8.setEnabled(False)
            self.textBox6.setEnabled(False)
            self.label_9.setEnabled(False)
            self.textBox7.setEnabled(False)
            self.set_2.setEnabled(False)
            self.clear_2.setEnabled(False)
            self.label_11.setEnabled(False)
            self.textBox8.setEnabled(False)
            self.updateSetPoint.setEnabled(False)

    def on_clicked_2(self):
        if self.radioButton_2.isChecked():
            self.label_10.setEnabled(False)
            self.textBox4.setEnabled(False)
            self.set_3.setEnabled(False)
            self.label_6.setEnabled(True)
            self.label_7.setEnabled(True)
            self.textBox5.setEnabled(True)
            self.label_8.setEnabled(True)
            self.textBox6.setEnabled(True)
            self.label_9.setEnabled(True)
            self.textBox7.setEnabled(True)
            self.set_2.setEnabled(True)
            self.clear_2.setEnabled(True)
            self.label_11.setEnabled(True)
            self.textBox8.setEnabled(True)
            self.updateSetPoint.setEnabled(True)

    def open_loop(self):
        self.pwmValue = self.textBox4.text()
        self.board.digital[int(self.pwmPort)].write(float(self.pwmValue))
        self.label_13.setText('Gain: ' + str(self.pwmValue))
        JsonHandler.update_json(self, Control_1=True)

    def update_setpoint(self):
        self.sp = float(self.textBox8.text())
        self.label_17.setText("SP: " + str(self.sp))
        # update sp line
        if self.enableSetPoint.isChecked():
            self.sp_line.setPos(self.sp)

        ##Adicionar Jsonhandler?

    def set_PIDparams(self):
        self.kp = float(self.textBox5.text())
        self.ki = float(self.textBox6.text())
        self.kd = float(self.textBox7.text())
        Control.update_setpoint(self)
        # self.sp = float(self.textBox8.text())
        self.p = 0.0
        self.i = 0.0
        self.d = 0.0
        self.error_anterior = 0.0

        JsonHandler.update_json(self, Control_2=True)

        self.label_17.setText("SP: " + str(self.sp))

    def PID_calc(self):
        pv = self.board.analog[self.analogPort].read()
        self.error = (self.sp - pv)
        print('error:', self.error)
        # proportional calc
        self.p = self.kp * self.error

        # Integrative calc
        self.i = self.i + (self.ki * (self.sampleTime / 2) * (self.error + self.error_anterior))

        # Derivative calc
        self.d = ((self.error - self.error_anterior) * self.kd) / self.sampleTime

        # integrative max value
        if self.i > 100: self.i = 100
        if self.i < 0: self.i = 0

        # output max value
        pidsum = self.p + self.i + self.d
        if (pidsum) > 100:
            self.output = 100

        elif (pidsum) < 0:
            self.output = 0

        else:
            self.output = pidsum

        self.label_13.setText('Gain: ' + str(round(self.output, 5)))
        self.label_14.setText('P: ' + str(round(self.p, 5)))
        self.label_15.setText('I: ' + str(round(self.i, 5)))
        self.label_16.setText('D: ' + str(round(self.d, 5)))

        self.error_anterior = self.error
