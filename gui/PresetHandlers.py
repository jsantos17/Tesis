from lib.VnaChannel import VnaChannel
from gui.VnaMeasure import VnaMeasure
from lib.util.VnaEnums import CalType
from PyQt4 import QtGui

class PresetHandler(object):

    def __init__(self, ui):
        self.ui = ui
        self.ui.cal_presets_ui.full_2port_button.clicked.connect(self.full_2port_cal)
        self.ui.cal_presets_ui.trl_2port_button.clicked.connect(self.trl_2port_cal)
        self.ui.cal_presets_ui.cal_kit_combo.currentIndexChanged.connect(self.toggle_buttons)
        self.executor = None

    def toggle_buttons(self):
        if self.ui.cal_presets_ui.cal_kit_combo.currentIndex() == 0:
            self.ui.cal_presets_ui.trl_2port_button.setEnabled(True)
        if self.ui.cal_presets_ui.cal_kit_combo.currentIndex() == 1:
            self.ui.cal_presets_ui.trl_2port_button.setEnabled(False)

    def _set_cal_kit(self):
        if self.ui.cal_presets_ui.cal_kit_combo.currentIndex() == 0:
            self.channel.set_cal_kit(1)
        elif self.ui.cal_presets_ui.cal_kit_combo.currentIndex() == 1:
            self.channel.set_cs5()
            self.channel.set_cal_kit(30)

    def _connect(self):
        if self.executor is not None:
            return self.channel # Reuse previously opened object (and socket)
        try:
            chan_number = int(self.ui.cal_presets_ui.channel_combo.currentText())
            self.channels = range(1,chan_number+1)
            ip_port = str(self.ui.vna_ip_field.text()).split(":")
            ip = ip_port[0]
            port = int(ip_port[1])
            self.channel = VnaChannel(ip, port, 1) # Do connection
        except IndexError:
            QtGui.QMessageBox.information(self.ui.centralwidget,
                    "IP no especificado",
                    "Es necesario especificar un IP y puerto en el formato IP:puerto")

    def full_2port_cal(self):
        self._connect()
        def assign_channels(vna):
            for ch in self.channels:
                vna.channel = ch
                vna.set_sparam(1, ch)

        self.channel.channel = 1
        if len(self.channels) == 4:
            self.channel.set_four_channels()
        else:
            self.channel.set_one_channel()
        
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.set_sparam(1, ch)

        for ch in self.channels:
            self.channel.channel = ch
            self._set_cal_kit() # Find and set cal kit
            
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.set_cal_type(CalType.FULL_2PORT)
        
        QtGui.QMessageBox.information(self.ui.centralwidget,"Open", "Conectar open")
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.is_ready()
            self.channel.cal_measure_open(1)
            self.channel.is_ready()
            self.channel.cal_measure_open(2)
            self.channel.is_ready()
        assign_channels(self.channel)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Short", "Conectar short")
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.is_ready()
            self.channel.cal_measure_short(1)
            self.channel.is_ready()
            self.channel.cal_measure_short(2)
            self.channel.is_ready()
        assign_channels(self.channel)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Load", "Conectar load")
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.is_ready()
            self.channel.cal_measure_load(1)
            self.channel.is_ready()
            self.channel.cal_measure_load(2)
            self.channel.is_ready()
        assign_channels(self.channel)
   
        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Conectar thru")
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.is_ready()
            self.channel.cal_measure_thru(1, 2)
            self.channel.is_ready()
            self.channel.cal_measure_thru(2, 1)
            self.channel.is_ready()
        assign_channels(self.channel)


        isolation = QtGui.QMessageBox.question(self.ui.centralwidget,"Isolation", "Calibrar isolation? (opcional)", 
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if isolation == QtGui.QMessageBox.Yes:
            QtGui.QMessageBox.information(self.ui.centralwidget,"Isolation", "Conectar load en 1 y 2")
            for ch in self.channels:
                self.channel.channel = ch
                self.channel.is_ready()
                self.channel.cal_measure_isol(1, 2)
                self.channel.is_ready()

            assign_channels(self.channel)

        self.channel.is_ready()
        should_save = QtGui.QMessageBox.question(self.ui.centralwidget, "Guardar?", "Guardar calibracion?",
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if should_save == QtGui.QMessageBox.Yes:
            for ch in self.channels:
                self.channel.channel = ch
                self.channel.save_cal()
            
        
    def trl_2port_cal(self):
        self._connect()
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.set_cal_kit(1) # Calkit 85033E
            self.channel.set_cal_type(CalType.TRL_2PORT)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Conectar THRU")
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.trl_thru_line(1, 2)
            self.channel.is_ready()
            self.channel.trl_thru_line(2, 1)
            self.channel.is_ready()
        QtGui.QMessageBox.information(self.ui.centralwidget,"Reflect", "Conectar REFLECT")
        
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.trl_reflect(1)
            self.channel.is_ready()
            self.channel.trl_reflect(2)
            self.channel.is_ready()

        QtGui.QMessageBox.information(self.ui.centralwidget,"Line/Match", "Conectar Line Match")
        
        for ch in self.channels:
            self.channel.channel = ch
            self.channel.trl_line_match(1,2)
            self.channel.is_ready()
            self.channel.trl_line_match(2,1)
            self.channel.is_ready()

        should_save = QtGui.QMessageBox.question(self.ui.centralwidget, "Guardar?", "Guardar calibracion?",
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if should_save == QtGui.QMessageBox.Yes:
            for ch in self.channels:
                self.channel.channel = ch
                self.channel.save_cal()
 

