from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep
from lib.SMUStep import SMUStep
import socket
import time

class MeasureHandler(QtGui.QMainWindow):

    def handle(self, event, ui, params):
        ip = ui.ipField.text()
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((ip,1225))
        active = list()
        inactive = list()
        mapping = [{'combo': ui.smu1_combo, 'layout': ui.smu1_layout},
                   {'combo': ui.smu2_combo, 'layout': ui.smu2_layout},
                   {'combo': ui.smu3_combo, 'layout': ui.smu3_layout},
                   {'combo': ui.smu4_combo, 'layout': ui.smu4_layout}]

        for element in mapping:
           if "open" not in element['combo'].currentText().toLower():
               active.append(element)
           else:
               inactive.append(element)


        for element in active:
            combo = element['combo']
            layout = element['layout']
            groupbox = layout.itemAt(2).widget()
            ch = int(str(combo.objectName())[3:4])
            if "current" in combo.currentText().toLower():
                
                if "constant" in combo.currentText.toLower():
                    # Constant current configuration for SMU
                    pass
                
                elif "list" in combo.currentText().toLower():
                    # Current list sweep configuration for SMU
                    pass
                
                elif "sweep" in combo.currentText().toLower():
                    # Current sweep configuration for SMU
                    stop = float(groupbox.findChild(QtGui.QLineEdit, "val_stop_field").text())
                    start = float(groupbox.findChild(QtGui.QLineEdit, "val_inicio_field").text())
                    step = float(groupbox.findChild(QtGui.QLineEdit, "step_field").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_field").text())
                    smu = SMUSweep(ch, SourceMode.CURRENT, SourceType.CURRENT, start, stop, step, compliance,
                                   sweep_type=SweepType.LINEAR, 'V%s' % ch)
                    for command in smu.get_commands():
                        pass
                
                elif "step" in combo.currentText().toLower():
                    # Current step configuration for SMU
                    start = float(groupbox.findChild(QtGui.QLineEdit, "start_lineedit").text())
                    step = float(groupbox.findChild(QtGui.QLineEdit, "step_lineedit").text())
                    steps = int(groupbox.findChild(QtGui.QLineEdit, "steps_lineedit").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_lineedit").text())

                    smu = SMUStep(ch, SourceMode.CURRENT, SourceType.CURRENT, start, step, steps, compliance,
                                  'V%s' % ch, 'I%s' % ch)

                    for command in smu.get_commands():
                        pass

            elif "voltage" in combo.currentText().toLower():
                pass
