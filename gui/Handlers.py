from PyQt4 import QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog
import SubUi
import LayoutUtil
import os
from MeasureHandler import MeasureHandler
from VnaMeasure import VnaMeasureThreaded
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import Direction
from utils import restore_ui
from utils import save_ui 

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui
        self.handler = MeasureHandler()
        self.curr_x = 0

    def browse(self, event):
        directory = QFileDialog.getExistingDirectory(self, 
                "Donde guardar?", "~", options=QFileDialog.ShowDirsOnly)
        data_file = os.path.join(str(directory), str(self.ui.fileField.text()))
        self.ui.fileField.setText(data_file)

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
                    "IP no especificado", "Es necesario especifcar un IP y puerto en el formato IP:puerto")

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
        VnaMeasureThreaded(self.ui)

    def restore_ui(self):
        restore_ui(self.ui)

    def save_ui(self):
        save_ui(self.ui)

    def move(self, direction):
        (port, ip) = self.get_port_ip()
        channel = VnaChannel(port, ip, 1)
        channel.add_marker(1)
        start_x = channel.get_start_x()
        stop_x = channel.get_stop_x()
        bandwidth = stop_x - start_x
        gran = bandwidth/100 # By default 1/100th bandwidth granularity
        if self.curr_x == 0:
            self.curr_x = start_x
        if direction == Direction.LEFT:
            self.curr_x = self.curr_x - gran # Save curr_x in container for future use
        elif direction == Direction.RIGHT:
            self.curr_x = self.curr_x + gran # Save curr_x in container for future use
        channel.set_x(self.curr_x)
        y = channel.get_y()

        self.ui.y_re_label.setText(str(y[0]))
        self.ui.y_im_label.setText(str(y[1]))
        self.ui.x_label.setText(str(self.curr_x))

    def move_left(self):
        self.move(Direction.LEFT)  

    def move_right(self):
        self.move(Direction.RIGHT)

