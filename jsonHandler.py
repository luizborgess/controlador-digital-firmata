import json


class JsonHandler:

    def json_read(self):
        with open('Settings.json', 'r') as json_file:
            self.data = json.load(json_file)
        self.textBox1.setText(self.data['AnalogPort'])
        self.textBox2.setText(self.data['PwmPort'])
        self.textBox3.setText(self.data['SampleTime'])
        self.graphRange = self.data['GraphRange']
        json_file.close()

    def update_json(self):
        self.data['AnalogPort'] = str(self.analogPort)
        self.data['PwmPort'] = str(self.pwmPort)
        self.data['SampleTime'] = str(self.sampleTime)
        with open('Settings.json', 'w+') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False)
        json_file.close()