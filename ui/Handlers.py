from PyQt4 import QtGui
from PyQt4.QtCore import QObject

class SlotContainer(QtGui.QMainWindow):
    #def __init__(self, ui):
    #    self.ui = ui

    def set_ui(self, ui):
        self.ui = ui

    def on_measure_select(self, event):
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), ctext = self.sender().currentText())
        self.ui.smu1_label.hide()

