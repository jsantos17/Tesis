from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog, QDialog
import SubUi
import LayoutUtil
import os
from MeasureHandler import MeasureHandler
from VnaMeasure import VnaMeasureThreaded
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import Direction
from utils import restore_ui
from utils import save_ui
from gui import MenuHandlers
from Calibration import Ui_cal_dialog
from Ri import Ui_RI_dialog
from CalPresets import Ui_cal_presets
from RiHandlers import RiHandler
from CalHandlers import CalHandler 
from PresetHandlers import PresetHandler

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui
        self.handler = MeasureHandler()
        self.curr_x = 0
        self.channel = None

    def browse(self, event):
        directory = QFileDialog.getExistingDirectory(self, 
                "Donde guardar?", "~", options=QFileDialog.ShowDirsOnly)
        if self.sender().objectName() == "browse_button":
            data_file = os.path.join(str(directory), str(self.ui.fileField.text()))
            self.ui.fileField.setText(data_file)
        elif self.sender().objectName() == "vna_browse_button":
            data_file = os.path.join(str(directory), str(self.ui.vna_file_field.text()))
            self.ui.vna_file_field.setText(data_file)

    def selected_start_stop(self, event):
        if self.ui.start_stop_radio.isChecked():
            print "Selected start stop"
            self.ui.bottom_layout.itemAt(3).widget().setParent(None)
            self.ui.bottom_layout.addWidget(LayoutUtil.get_start_stop_groupbox())

    def selected_center_span(self, event):
        if self.ui.center_span_radio.isChecked():
            print "Selected center span"
            self.ui.bottom_layout.itemAt(3).widget().setParent(None)
            self.ui.bottom_layout.addWidget(LayoutUtil.get_center_span_groupbox())
    
    def get_port_ip(self):
        try:
            ip_port = str(self.ui.ipField.text()).split(":")
            ip = ip_port[0]
            port = int(ip_port[1])
            self.handler.ip = ip
            self.handler.port = port
            return (ip, port)
        except IndexError:
            QtGui.QMessageBox.information(self.ui.centralwidget, 
                    "IP no especificado", "Es necesario especificar un IP y puerto en el formato IP:puerto")

    def on_measure(self, event):
            # WARNING: MAGIC AHEAD
            # Handler expects ip and port as members of the self.handler object. 
            # get_port_ip() makes sure to put them there
            self.get_port_ip()
            params = self
            self.handler.handle(event, self.ui, params)

    def on_measure_select(self, event):
        # Two SMUs can't be in sweep mode or step mode at the same time! 
        # List sweep or constant is fair enough in more than one SMU
       
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), 
                                                ctext = self.sender().currentText())
        # print self.modes_activated
        # Pass the sender to the handling function
                 
        LayoutUtil.layout_update(self.sender(), self.ui)
   
    def on_vna_measure(self):
        if self.channel is not None:
            self.channel.executor.close()
            self.channel = None # Makes sure move recreates its executor
        VnaMeasureThreaded(self.ui)

    def restore_ui(self):
        restore_ui(self.ui)

    def save_ui(self):
        save_ui(self.ui)

    def launch_calibration(self):
        self.ui.cal_ui = Ui_cal_dialog() # Make the calibration dialog available app-wise
        dialog = QDialog()
        dialog.ui = self.ui.cal_ui
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        handler = CalHandler(self.ui)
        dialog.exec_()

    def launch_ri(self):
        self.ui.ri_ui = Ui_RI_dialog() 
        dialog = QDialog()
        dialog.ui = self.ui.ri_ui
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        handler = RiHandler(self.ui)
        dialog.exec_()
        

    def launch_preset_calibration(self):
        self.ui.cal_presets_ui = Ui_cal_presets()
        dialog = QDialog()
        dialog.ui = self.ui.cal_presets_ui
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        handler = PresetHandler(self.ui)
        dialog.exec_()

    # TODO Move this elsewhere
    def move(self, direction):
        ip_port = str(self.ui.vna_ip_field.text()).split(":")
        ip = ip_port[0]
        port = int(ip_port[1])
        if self.channel is None:
            self.channel = VnaChannel(ip, port, 1)
        self.channel.add_marker(1)
        start_x = self.channel.get_start_x()
        stop_x = self.channel.get_stop_x()
        bandwidth = stop_x - start_x
        gran = bandwidth/100 # By default 1/100th bandwidth granularity
        self.curr_x = self.channel.get_x()
        if direction == Direction.LEFT:
            self.curr_x = self.curr_x - gran # Save curr_x in container for future use
        elif direction == Direction.RIGHT:
            self.curr_x = self.curr_x + gran # Save curr_x in container for future use
        self.channel.set_x(self.curr_x)
        y = self.channel.get_y()

        self.ui.y_re_label.setText(str(y[0]))
        self.ui.y_im_label.setText(str(y[1]))
        self.ui.x_label.setText(str(self.curr_x))

    def move_left(self):
        self.move(Direction.LEFT)  

    def move_right(self):
        self.move(Direction.RIGHT)

    
    def open_file(self):
        MenuHandlers.handle_open(self.ui)

    def save_file(self):
        MenuHandlers.handle_save(self.ui)

    def save_as_file(self):
        MenuHandlers.handle_save_as(self.ui)

    def close(self):
        MenuHandlers.handle_close(self.ui)
