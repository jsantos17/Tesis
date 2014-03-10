from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import CalType
from PyQt4 import QtGui

class CalHandler(object):

    def __init__(self, ui):
        self.ui = ui
        self.ui.cal_ui.open_button.clicked.connect(self.calibrate_open)
        self.ui.cal_ui.short_button.clicked.connect(self.calibrate_short)
        self.ui.cal_ui.load_button.clicked.connect(self.calibrate_load)
        self.channel = None

    def _connect_to_vna(self):
        if self.channel is not None:
            return self.channel # Reuse previously opened object (and socket)
        try:
            ip_port = str(self.ui.vna_ip_field.text()).split(":")
            ip = ip_port[0]
            port = int(ip_port[1])
            self.channel = VnaChannel(ip, port, 1) # Do connection
        except IndexError:
            QtGui.QMessageBox.information(self.ui.centralwidget,
                    "IP no especificado", 
                    "Es necesario especificar un IP y puerto en el formato IP:puerto")


    def _get_cal_data(self):
        if self.ui.cal_ui.cal_type_combo.currentIndex() == 0:
            cal_type = CalType.OPEN
        elif self.ui.cal_ui.cal_type_combo.currentIndex() == 1:
            cal_type = CalType.SHORT
        elif self.ui.cal_ui.cal_type_combo.currentIndex() == 2:
            cal_type = CalType.THRU
        
        if self.ui.cal_ui.cal_kit_combo.currentIndex() == 0:
            cal_kit = 1 # For 85033E
        
        return {"cal_type": cal_type, "cal_kit": cal_kit} 

    def calibrate_open(self):
        self._connect_to_vna()
        cal_data = self._get_cal_data()
        self.channel.set_cal_kit(cal_data["cal_kit"])
        self.channel.set_cal_type(cal_data["cal_type"])
        self.channel.cal_measure_open()
        print "Calibrate open"

    def calibrate_short(self):
        self._connect_to_vna()
        cal_data = self._get_cal_data()
        self.channel.set_cal_kit(cal_data["cal_kit"])
        self.channel.set_cal_type(cal_data["cal_type"])
        self.channel.cal_measure_short()
        print "Calibrate short"

    def calibrate_load(self):
        self._connect_to_vna()
        cal_data = self._get_cal_data()
        self.channel.set_cal_kit(cal_data["cal_kit"])
        self.channel.set_cal_type(cal_data["cal_type"])
        self.channel.cal_measure_load()
        print "Calibrate load"
