from PyQt4 import QtGui
from PyQt4.QtCore import QObject

class MeasureHandler(QtGui.QMainWindow):

    def handle(self, event, ui, params):
        active_combo = list()
        for combo in [ui.smu1_combo, ui.smu2_combo, ui.smu3_combo, ui.smu4_combo]:
            if "open" not in combo.currentText().toLower():
                active_combo.append(combo)
        
        print [str(x.objectName()) for x in active_combo]

        # Now we have the usable combo_boxes, do something with them!

