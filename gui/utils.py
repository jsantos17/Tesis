import yaml
import pprint
from PyQt4 import QtGui

def save_ui(ui):
    state = dict()
    ip = str(ui.ipField.text())
    f = str(ui.fileField.text())
    state["ip"] = ip
    state["f"] = f
    state["combos"] = list()

    for index, combo in enumerate(
            [(ui.smu1_combo, ui.smu1_layout), 
             (ui.smu2_combo, ui.smu2_layout), 
             (ui.smu3_combo, ui.smu3_layout), 
             (ui.smu4_combo, ui.smu4_layout)]):
        combo_text = combo[0].currentText().toLower()
        layout = combo[1]
        groupbox = layout.itemAt(2).widget()
        if "open" in combo_text:
            # Combobox empty, don't save anything
            continue
        hdict = dict()
        hdict["num"] = str(index+1)
        if "voltage" in combo_text:
            hdict["type"] = "voltage"
        if "current" in combo_text:
            hdict["type"] = "current"
        if "constant" in combo_text:
            hdict["value"] = str(groupbox.findChild(QtGui.QLineEdit, "constant_textbox").text())
            hdict["compliance"] = str(groupbox.findChild(QtGui.QLineEdit, "compliance_textbox").text())
            hdict["sfun"] = "constant"
        if "step" in combo_text:
            hdict["start"] = str(groupbox.findChild(QtGui.QLineEdit, "start_lineedit").text())
            hdict["step"] = str(groupbox.findChild(QtGui.QLineEdit, "step_lineedit").text())
            hdict["steps"] = str(groupbox.findChild(QtGui.QLineEdit, "steps_lineedit").text())
            hdict["compliance"] = str(groupbox.findChild(QtGui.QLineEdit, "compliance_lineedit").text())
            hdict["sfun"] = "step"
        if "sweep" in combo_text and "list" not in combo_text:
            hdict["stop"]  = str(groupbox.findChild(QtGui.QLineEdit, "val_stop_field").text())
            hdict["start"] = str(groupbox.findChild(QtGui.QLineEdit, "val_inicio_field").text())
            hdict["step"]  = str(groupbox.findChild(QtGui.QLineEdit, "step_field").text())
            hdict["compliance"] = str(groupbox.findChild(QtGui.QLineEdit, "compliance_field").text())
            hdict["sweep_type"] = str(groupbox.findChild(QtGui.QComboBox, "sweep_type_combobox").currentText())
            hdict["sfun"] = "sweep"
        if "list" in combo_text:
            hdict["value_list"] = str(groupbox.findChild(QtGui.QTextEdit, "list_textedit").toPlainText())
            hdict["sfun"] = "list"

        state["combos"].append(hdict)


    # Serialize dict to disk
    with open("ui_state.yml", "w+") as stream:
        yaml.dump(state, stream)
            
def restore_ui(ui):
    pass
