from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject

class MeasureHandler(QtGui.QMainWindow):

    def handle(self, event, ui, params):
        active = list()
        mapping = [{'combo': ui.smu1_combo, 'groupbox': ui.smu1_groupbox},
                   {'combo': ui.smu2_combo, 'groupbox': ui.smu2_groupbox},
                   {'combo': ui.smu3_combo, 'groupbox': ui.smu3_groupbox},
                   {'combo': ui.smu4_combo, 'groupbox': ui.smu4_groupbox}]

        for element in mapping:
           if "open" not in element['combo'].currentText().toLower():
               active.append(element)

        for element in active:
            combo = element['combo']
            groupbox = element['groupbox']
            if "current" in combo.currentText().toLower():
                if "sweep" in combo.currentText().toLower():
                    ch = int(str(combo.objectName())[3:4])
                    print groupbox.findChildren(QtGui.QLineEdit, "*")
            elif "voltage" in combo.currentText().toLower():
                pass
