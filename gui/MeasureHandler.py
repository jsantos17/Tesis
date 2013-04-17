from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep


class MeasureHandler(QtGui.QMainWindow):

    def handle(self, event, ui, params):
        active = list()
        mapping = [{'combo': ui.smu1_combo, 'layout': ui.smu1_layout},
                   {'combo': ui.smu2_combo, 'layout': ui.smu2_layout},
                   {'combo': ui.smu3_combo, 'layout': ui.smu3_layout},
                   {'combo': ui.smu4_combo, 'layout': ui.smu4_layout}]

        for element in mapping:
           if "open" not in element['combo'].currentText().toLower():
               active.append(element)

        for element in active:
            combo = element['combo']
            layout = element['layout']
            groupbox = layout.itemAt(2).widget()
            if "current" in combo.currentText().toLower():
                if "sweep" in combo.currentText().toLower():
                    ch = float(str(combo.objectName())[3:4])
                    stop = float(groupbox.findChild(QtGui.QLineEdit, "val_stop_field").text())
                    start = float(groupbox.findChild(QtGui.QLineEdit, "val_inicio_field").text())
                    step = float(groupbox.findChild(QtGui.QLineEdit, "step_field").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_field").text())
                    smu = SMUSweep('V1','I1',SourceMode.CURRENT, ch, SourceType.CURRENT, start, stop, step, compliance, sweep_type=SweepType.LINEAR)
                    print smu.get_commands()
                    print [ch, stop, start, step, compliance]
            elif "voltage" in combo.currentText().toLower():
                pass
