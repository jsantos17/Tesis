from PyQt4 import QtGui
import SubUi


def layout_update(sender, ui):
        sender_name = str(sender.objectName())
        # Map sender name to layout
        mapping = {
            "smu1": ui.smu1_layout,
            "smu2": ui.smu2_layout,
            "smu3": ui.smu3_layout,
            "smu4": ui.smu4_layout
        }
        caller_layout = mapping[sender_name[0:4]]
        if "open" in sender.currentText().toLower():
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            new_groupbox = QtGui.QGroupBox()
            caller_layout.addWidget(new_groupbox)
        if "list" in sender.currentText().toLower():
            new_groupbox = get_list_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
        elif "sweep" in sender.currentText().toLower():
            new_groupbox = get_sweep_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
        elif "step" in sender.currentText().toLower():
            new_groupbox = get_step_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)
        elif "constant" in sender.currentText().toLower():
            new_groupbox = get_constant_groupbox()
            caller_layout.itemAt(2).widget().setParent(None) # Delete widget
            caller_layout.addWidget(new_groupbox)

def get_constant_groupbox():
    return SubUi.get_constant_groupbox()

def get_sweep_groupbox():
    return SubUi.get_sweep_groupbox()

def get_step_groupbox():
    return SubUi.get_step_groupbox()

def get_list_groupbox():
    return SubUi.get_list_groupbox()
    
def get_center_span_groupbox():
    return SubUi.get_center_span_ui()

def get_start_stop_groupbox():
    return SubUi.get_start_stop_ui()
