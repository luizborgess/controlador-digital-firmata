import json


class JsonHandler:
    def JsonRead(self):
        with open('Settings.json', 'r') as json_file:
            self.data = json.load(json_file)
        self.textBox1.setText(self.data['AnalogPort'])
        self.textBox2.setText(self.data['PwmPort'])
        self.textBox3.setText(self.data['SampleTime'])
        self.graphRange = self.data['GraphRange']
        json_file.close()
