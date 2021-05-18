from Control import Control
import numpy as np


class UpdateGraph:
    def update_plot_data(self):

        # update ate o graph range
        if self.Xm.size < (self.graphRange / self.sampleTimeSec):
            mv_value = self.board.analog[self.analogPort].read()
            self.Xm = np.append(self.Xm, mv_value)
            if self.temp.size == 0:
                self.temp = np.append(self.temp, 0)
            else:
                self.temp = np.append(self.temp, (self.temp[-1] + self.sampleTimeSec))

        # update alem do graph range
        else:

            self.Xm[:-1] = self.Xm[1:]
            mv_value = self.board.analog[self.analogPort].read()
            self.Xm[-1] = float(mv_value)

            self.ptr += self.sampleTimeSec
            self.graphWidget.setRange(padding=0, xRange=[self.ptr, self.ptr + self.graphRange])

            # move graph

            self.temp = np.delete(self.temp, 0)
            self.temp = np.append(self.temp, (self.temp[-1] + self.sampleTimeSec))

        self.label_18.setText("MV: " + str(mv_value))
        self.curve.setData(self.temp, self.Xm)

        # esse if nao esta bom, criar update plotdata especifico para pid
        if self.radioButton_2.isChecked():
            Control.PID_calc(self)
            self.pwmValue = self.output / 100
            self.board.digital[int(self.pwmPort)].write(self.pwmValue)
