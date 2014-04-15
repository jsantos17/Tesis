from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import CalType
from PyQt4 import QtGui

class PresetHandler(object):

    def __init__(self, ui):
        self.ui = ui
        self.ui.cal_presets_ui.full_2port_button.clicked.connect(self.full_2port_cal)
        self.ui.cal_presets_ui.trl_2port_button.clicked.connect(self.trl_2port_cal)
        self.executor = None

    def _get_cal_kit(self):
        if self.ui.cal_presets_ui.cal_kit_combo.currentIndex() == 0:
            return 1# Corresponds to 85033E cal kit

    def _connect(self):
        if self.executor is not None:
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

    def full_2port_cal(self):
        self._connect()
        self.channel.set_cal_type(CalType.FULL_2PORT)
        self.channel.set_cal_kit(1) # Calkit 85033E
        QtGui.QMessageBox.information(self.ui.centralwidget,"Open", "Conectar open en 1")
        self.channel.cal_measure_open(1)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Short", "Conectar short en 1")
        self.channel.cal_measure_short(1)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Load", "Conectar load en 1")
        self.channel.cal_measure_load(1)

        QtGui.QMessageBox.information(self.ui.centralwidget,"Open", "Conectar open en 2")
        self.channel.cal_measure_open(2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Short", "Conectar short en 2")
        self.channel.cal_measure_short(2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Load", "Conectar load en 2")
        self.channel.cal_measure_load(2)


        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Conectar thru entre 1 y 2")
        self.channel.cal_measure_thru(1, 2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Conectar thru backwards")
        self.channel.cal_measure_thru(2, 1)

        isolation = QtGui.QMessageBox.question(self.ui.centralwidget,"Isolation", "Calibrar isolation? (opcional)", 
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if isolation == QtGui.QMessageBox.Yes:
            QtGui.QMessageBox.information(self.ui.centralwidget,"Isolation", "Conectar load en 1 y 2")
            self.channel.cal_measure_isol(1, 2)

        should_save = QtGui.QMessageBox.question(self.ui.centralwidget, "Guardar?", "Guardar calibracion?",
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if should_save == QtGui.QMessageBox.Yes:
            self.channel.save_cal()
            
        
    def trl_2port_cal(self):
        self._connect()
        self.channel.set_cal_kit(1) # Calkit 85033E
        self.channel.set_cal_type(CalType.TRL_2PORT)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Thru de 1 a 2")
        self.channel.trl_thru_line(1, 2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Thru", "Thru de 2 a 1")
        self.channel.trl_thru_line(2, 1)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Reflect", "Reflect puerto 1")
        self.channel.trl_reflect(1)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Reflect", "Reflect puerto 2")
        self.channel.trl_reflect(2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Line/Match", "Line/Match de 1 a 2")
        self.channel.trl_line_match(1,2)
        QtGui.QMessageBox.information(self.ui.centralwidget,"Line/Match", "Line/Match de 2 a 1")
        self.channel.trl_line_match(2,1)

        should_save = QtGui.QMessageBox.question(self.ui.centralwidget, "Guardar?", "Guardar calibracion?",
                QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if should_save == QtGui.QMessageBox.Yes:
            self.channel.save_cal()
 

