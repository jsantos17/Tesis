import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtGui
from Keithley import Ui_mainWindow
from Handlers import SlotContainer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(window)
    combo_boxes = [ui.smu1_combo, ui.smu2_combo, ui.smu3_combo, ui.smu4_combo]
    combo_elements = ["Open","Current Bias","Current Sweep",
                      "Current List Sweep", "Current Step",
                      "Voltage Bias", "Voltage Sweep",
                      "Voltage List Sweep", "Voltage Step"]
    container = SlotContainer(ui)
    for box in combo_boxes:
        for element in combo_elements:
            box.addItem(element)
        box.currentIndexChanged.connect(container.on_measure_select)
    
    ui.pushButton.clicked.connect(container.callback)
    ui.start_stop_radio.clicked.connect(container.selected_start_stop)
    ui.center_span_radio.clicked.connect(container.selected_center_span)
    ui.measure_button.clicked.connect(container.on_measure)
    window.show()
    sys.exit(app.exec_())
