from Control import Control
import numpy as np

class UpdateGraph:
    def update_plot_data(self):

        #update ate o graph range
        if self.Xm.size < (50*1000/200):
            mv_value = self.board.analog[self.analogPort].read()
            self.Xm = np.append(self.Xm, mv_value)
            if self.temp.size==0:
                self.temp = np.append(self.temp, self.sampleTimeSec)
            else:
                self.temp= np.append(self.temp,(self.temp[-1]+self.sampleTimeSec))

        #update alem do graph range
        else:

            self.Xm[:-1] = self.Xm[1:]
            mv_value = self.board.analog[self.analogPort].read()
            self.Xm[-1] = float(mv_value)

            self.graphWidget.setRange(padding=0,xRange=[self.ptr, self.ptr + 50])

            #move graph
            self.ptr += self.sampleTimeSec

            self.temp = self.temp[1:]
            self.temp= np.append(self.temp,(self.temp[-1]+self.sampleTimeSec))

        print(self.temp)
        self.curve.setData(self.temp,self.Xm)
        self.curve.setPos(self.ptr, 0)
        #print(self.Xm)



        # esse if nao esta bom, criar update plotdata especifico para pid
        if self.radioButton_2.isChecked():
            Control.PID_calc(self)
            self.pwmValue = self.output / 100
            self.board.digital[int(self.pwmPort)].write(self.pwmValue)


    """
            self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]

        # process variable =self.board.analog[self.analogPort].read()
        mv_value = self.board.analog[self.analogPort].read()
        self.y.append(mv_value)

        self.label_18.setText("MV: " + str(mv_value))
        self.data_line.setData(self.x, self.y)
    """
