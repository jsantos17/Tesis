from PyQt4 import QtGui
from PyQt4.QtCore import QObject
import SubUi
import LayoutUtil
from MeasureHandler import MeasureHandler

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui

    def selected_start_stop(self, event):
        print "Selected start stop"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(LayoutUtil.get_start_stop_groupbox())

    def selected_center_span(self, event):
        print "Selected center span"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(LayoutUtil.get_center_span_groupbox())
    
    def on_measure(self, event):
        # We mostly prepare objects for the actual handlers
        
        params = self
        handler = MeasureHandler(self.ui.ipField.text())
        handler.handle(event, self.ui, params)

    def on_measure_select(self, event):
        # Two SMUs can't be in sweep mode or step mode at the same time! 
        # List sweep or constant is fair enough in more than one SMU
       
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), 
                                                ctext = self.sender().currentText())
        # print self.modes_activated
        # Pass the sender to the handling function
                 
        LayoutUtil.layout_update(self.sender(), self.ui)
       
