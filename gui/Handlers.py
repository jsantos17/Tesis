from PyQt4 import QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog
import SubUi
import LayoutUtil
import os
from MeasureHandler import MeasureHandler
from utils import restore_ui
from utils import save_ui 

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui
        self.handler = MeasureHandler()

    def browse(self, event):
        directory = QFileDialog.getExistingDirectory(self, 
                "Donde guardar?", "~", options=QFileDialog.ShowDirsOnly)
        data_file = os.path.join(str(directory), str(self.ui.fileField.text()))
        self.ui.fileField.setText(data_file)

    def save_data(self, event):
        print "Save data"

    def selected_start_stop(self, event):
        print "Selected start stop"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(LayoutUtil.get_start_stop_groupbox())

    def selected_center_span(self, event):
        print "Selected center span"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(LayoutUtil.get_center_span_groupbox())
    
    def on_measure(self, event):
        try:
            ip_port = str(self.ui.ipField.text()).split(":")
            ip = ip_port[0]
            port = int(ip_port[1])
            self.handler.ip = ip
            self.handler.port = port
            params = self
            self.handler.handle(event, self.ui, params)
        except IndexError:
            QtGui.QMessageBox.information(self.ui.centralwidget, 
                    "IP no especificado", "Es necesario especifcar un IP y puerto en el formato IP:puerto")

    def on_measure_select(self, event):
        # Two SMUs can't be in sweep mode or step mode at the same time! 
        # List sweep or constant is fair enough in more than one SMU
       
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), 
                                                ctext = self.sender().currentText())
        # print self.modes_activated
        # Pass the sender to the handling function
                 
        LayoutUtil.layout_update(self.sender(), self.ui)
       
    def restore_ui(self):
        restore_ui(self.ui)

    def save_ui(self):
        save_ui(self.ui)
