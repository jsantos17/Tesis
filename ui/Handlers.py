from PyQt4 import QtGui
from PyQt4.QtCore import QObject
import SubUi
from MeasureHandler import MeasureHandler

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui

    def selected_start_stop(self, event):
        print "Selected start stop"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(self._get_start_stop_groupbox())

    def selected_center_span(self, event):
        print "Selected center span"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(self._get_center_span_groupbox())
    
    def on_measure(self, event):
        params = self
        handler = MeasureHandler()
        handler.handle(event, self.ui, params)

    def on_measure_select(self, event):
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), ctext = self.sender().currentText())
        senderName = str(self.sender().objectName())
        senderText = str(self.sender().currentText())
        # Map sender name to layout
        mapping = {
            "smu1": self.ui.smu1_layout,
            "smu2": self.ui.smu2_layout,
            "smu3": self.ui.smu3_layout,
            "smu4": self.ui.smu4_layout
        }
        caller_layout = mapping[senderName[0:4]]
        if "open" in self.sender().currentText().toLower():
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            new_groupbox = QtGui.QGroupBox()
            caller_layout.addWidget(new_groupbox)
        if "list" in self.sender().currentText().toLower():
            new_groupbox = self._get_list_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
            new_groupbox.repaint()
            caller_layout.update()
        elif "sweep" in self.sender().currentText().toLower():
            new_groupbox = self._get_sweep_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
            new_groupbox.repaint()
            caller_layout.update()
        elif "step" in self.sender().currentText().toLower():
            new_groupbox = self._get_step_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
            new_groupbox.repaint()
            caller_layout.update()

    def callback(self, event):
        self.ui.smu1_layout.itemAt(0).widget().setParent(None)

    def _get_sweep_groupbox(self):
        return SubUi.get_sweep_groupbox() 

    def _get_step_groupbox(self):
        return SubUi.get_step_groupbox()

    def _get_list_groupbox(self):
        return SubUi.get_list_groupbox()
    
    def _get_center_span_groupbox(self):
        return SubUi.get_center_span_ui()

    def _get_start_stop_groupbox(self):
        return SubUi.get_start_stop_ui()
