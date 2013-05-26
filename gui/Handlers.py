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
        self.combo_lists = {self.ui.smu1_combo, self.ui.smu2_combo, self.ui.smu3_combo, self.ui.smu4_combo}
        self.all_combo_lists = {self.ui.smu1_combo, self.ui.smu2_combo, self.ui.smu3_combo, self.ui.smu4_combo}

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
        handler = MeasureHandler()
        handler.handle(event, self.ui, params)

    def on_measure_select(self, event):
        # Two SMUs can't be in sweep mode or step mode at the same time! 
        # List sweep or constant is fair enough in more than one SMU
       
        print "ComboBox: {cbox}, Text = {ctext}".format(cbox=self.sender().objectName(), 
                                                ctext = self.sender().currentText())
        # print self.modes_activated
        # Pass the sender to the handling function
                 
        LayoutUtil.layout_update(self.sender(), self.ui)
        
        if "sweep" in self.sender().currentText().toLower() and "list" not in self.sender().currentText().toLower():
            self.modes_activated.add("sweep")
        if "step" in self.sender().currentText().toLower():
            self.modes_activated.add("step")
        if "open" in self.sender().currentText().toLower():
            self.combo_lists.add(self.sender())

        # We need to check what modes are not active anymore 
        # and restore the options for them on the combobox
        
        sweep_count = 0
        step_count = 0

        for combo in self.all_combo_lists:
            if "sweep" in combo.currentText().toLower() and "list" not in combo.currentText().toLower():
                sweep_count += 1
            if "step" in combo.currentText().toLower():
                step_count += 1

        if sweep_count == 0 and "sweep" in self.modes_activated:
            self.modes_activated.remove("sweep")
        if step_count == 0 and "step" in self.modes_activated:
            self.modes_activated.remove("step")

        print "Combo boxes in step mode: {step_count}".format(step_count = step_count)
        print "Combo boxes in sweep mode: {sweep_count}".format(sweep_count = sweep_count)
        
        for combo in self.combo_lists:
            combo.blockSignals(True)
            combo.clear()
            if "sweep" in self.modes_activated and "step" in self.modes_activated \
                and not ("sweep" in combo.currentText().toLower() or "step" in combo.currentText().toLower()) :
                new_items = ["Open", "Current Constant", "Current List Sweep", 
                            "Voltage Constant", "Voltage List Sweep"]
                for item in new_items:
                    combo.addItem(item)

            elif "sweep" in self.modes_activated and ("sweep" not in combo.currentText().toLower() and "list" not in combo.currentText().toLower()):
                new_items = ["Open", "Current Constant", "Current List Sweep", 
                            "Current Step", "Voltage Constant", "Voltage List Sweep", "Voltage Step"]
                for item in new_items:
                    combo.addItem(item)

            elif "step" in self.modes_activated:
                new_items = ["Open", "Current Constant", "Current Sweep", 
                            "Current List Sweep", "Voltage Constant", 
                            "Voltage Sweep", "Voltage List Sweep"]
                for item in new_items:
                    combo.addItem(item)

            else:
                new_items = ["Open","Current Constant","Current Sweep",
                            "Current List Sweep", "Current Step",
                            "Voltage Constant", "Voltage Sweep",
                            "Voltage List Sweep", "Voltage Step"]
                for item in new_items:
                    combo.addItem(item)
            combo.blockSignals(False)
        #    combo_contents = [combo.itemText(i) for i in range(combo.count())]
        #    j = 0
        #    for item in combo_contents:
        #        if "sweep" in item.toLower() and "sweep" in self.modes_activated and "list" not in item.toLower():
        #            new_items = []
        #            combo.removeItem(j)
        #        if "step" in item.toLower() and "step" in self.modes_activated:
        #            combo.removeItem(j)
        #        j = j + 1

