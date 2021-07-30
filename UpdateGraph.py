from Control import Control
import numpy as np


class UpdateGraph:
    def update_plot_data(self):
        # update ate o graph range
        if self.y.size < (self.graphRange / self.sampleTimeSec):
            mv_value = self.board.analog[self.analogPort].read()
            self.y = np.append(self.y, mv_value)
            if self.temp.size == 0:
                self.temp = np.append(self.temp, 0)
            else:
                self.temp = np.append(self.temp, (self.temp[-1] + self.sampleTimeSec))


            #self.y2[-1] = self.input_disturbance


        # update alem do graph range
        else:

            self.y[:-1] = self.y[1:]
            mv_value = self.board.analog[self.analogPort].read()
            self.y[-1] = float(mv_value)

            self.ptr += self.sampleTimeSec
            self.graphWidget.setRange(padding=0, xRange=[self.ptr, self.ptr + self.graphRange])

            # move graph

            self.temp = np.delete(self.temp, 0)
            self.temp = np.append(self.temp, (self.temp[-1] + self.sampleTimeSec))

        self.label_18.setText("MV: " + str(mv_value))

        self.curve.setData(self.temp, self.y)

        #if not good placed
        #IF for only PID uses
        if self.radioButton_2.isChecked():
            Control.PID_calc(self)
            self.pwmValue = self.output / 100
            self.board.digital[int(self.pwmPort)].write(self.pwmValue)

            if self.got_csv:
                #draw disturbance only when using PID

                self.y2 = np.append(self.y2, self.input_disturbance)
                self.curve2.setData(self.temp, self.y2)

    def mouse_update(self, e):
        pos = e[0]
        if self.graphWidget.sceneBoundingRect().contains(pos):
            mousePoint = self.graphWidget.getPlotItem().vb.mapSceneToView(pos)
            self.y_line.setPos(mousePoint.x())
            self.x_line.setPos(mousePoint.y())
            self.coordinates.setText(f'Coordenadas X: {str(round(mousePoint.x(), 4))} Y: {str(round(mousePoint.y(), 4))}' )