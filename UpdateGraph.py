from Control import Control


class UpdateGraph:
    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]

        # process variable =self.board.analog[self.analogPort].read()

        self.y.append(self.board.analog[self.analogPort].read())

        self.data_line.setData(self.x, self.y)

        if self.radioButton_2.isChecked():
            Control.PID_calc(self)
            self.pwmValue = self.output / 100
            self.board.digital[int(self.pwmPort)].write(self.pwmValue)
