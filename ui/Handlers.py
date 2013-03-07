from PyQt4 import QtGui
from PyQt4.QtCore import QObject
import SubUi

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui

    def on_measure_select(self, event):
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), ctext = self.sender().currentText())
        self.ui.verticalLayout.takeAt(2)
        self.ui.verticalLayout.addWidget(self._get_sweep_groupbox())
        #self.ui.smu1_groupbox = self._get_sweep_groupbox()

    def _get_sweep_groupbox(self):
        return SubUi.get_sweep_groupbox() 

