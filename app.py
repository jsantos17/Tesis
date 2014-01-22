import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtGui
from gui.Keithley import Ui_mainWindow
from gui.Handlers import SlotContainer
from gui.utils import restore_ui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(window)
    combo_boxes = [ui.smu1_combo, ui.smu2_combo, ui.smu3_combo, ui.smu4_combo]
    combo_groupboxes = [ui.smu1_groupbox, ui.smu2_groupbox, ui.smu3_groupbox, ui.smu4_groupbox]
    combo_elements = ["Open","Current Constant","Current Sweep",
                      "Current List Sweep", "Current Step",
                      "Voltage Constant", "Voltage Sweep",
                      "Voltage List Sweep", "Voltage Step",]
    container = SlotContainer(ui)
    for box in combo_boxes:
        for element in combo_elements:
            box.addItem(element)
        box.currentIndexChanged.connect(container.on_measure_select)
    
    ui.start_stop_radio.clicked.connect(container.selected_start_stop)
    ui.center_span_radio.clicked.connect(container.selected_center_span)
    ui.measure_button.clicked.connect(container.on_measure)
    ui.browse_button.clicked.connect(container.browse)
    ui.save_button.clicked.connect(container.save_data)
    app.aboutToQuit.connect(container.save_ui)
    window.show()
    sys.exit(app.exec_())
