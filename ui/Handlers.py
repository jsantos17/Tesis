from PyQt4 import QtGui
from PyQt4.QtCore import QObject
import SubUi
import LayoutUtil
from MeasureHandler import MeasureHandler

class SlotContainer(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui
        self.modes_activated = set()

    def selected_start_stop(self, event):
        print "Selected start stop"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(self._get_start_stop_groupbox())

    def selected_center_span(self, event):
        print "Selected center span"
        self.ui.bottom_layout.itemAt(2).widget().setParent(None)
        self.ui.bottom_layout.addWidget(self._get_center_span_groupbox())
    
    def on_measure(self, event):
        # We mostly prepare objects for the actual handlers
        
        params = self
        handler = MeasureHandler()
        handler.handle(event, self.ui, params)

    def on_measure_select(self, event):
        # Two SMUs can't be in sweep mode or step mode at the same time! 
        # List sweep or constant is fair enough in more than one SMU
        
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), 
                                                ctext = self.sender().currentText())
        print self.modes_activated
         
        LayoutUtil.layout_update(self.sender(), self.ui) # Pass the sender to the handling function
        
        if "sweep" in self.sender().currentText().toLower() and "list" not in self.sender().currentText().toLower():
            self.modes_activated.add("sweep")
        if "step" in self.sender().currentText().toLower():
            self.modes_activated.add("step")
        combo_lists = [self.ui.smu1_combo, self.ui.smu2_combo, self.ui.smu3_combo, self.ui.smu4_combo]
        combo_lists.remove(self.sender())
        for combo in combo_lists:
            combo_contents = [combo.itemText(i) for i in range(combo.count())]
            j = 0
            for item in combo_contents:
                if "sweep" in item.toLower() and "sweep" in self.modes_activated and "list" not in item.toLower():
                    combo.removeItem(j)
                if "step" in item.toLower() and "step" in self.modes_activated:
                    combo.removeItem(j)
                j = j + 1

