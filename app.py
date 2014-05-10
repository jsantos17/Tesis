import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QKeySequence
from PyQt4.QtGui import QShortcut
from gui.Keithley import Ui_mainWindow
from gui.Calibration import Ui_cal_dialog
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
    container = SlotContainer(ui) # We use a container to save state between callbacks
    for box in combo_boxes:
        for element in combo_elements:
            box.addItem(element)
        box.currentIndexChanged.connect(container.on_measure_select)
    
    ui.start_stop_radio.toggled.connect(container.selected_start_stop)
    ui.center_span_radio.toggled.connect(container.selected_center_span)
    ui.measure_button.clicked.connect(container.on_measure)
    ui.measure_vna.clicked.connect(container.on_vna_measure)
    ui.browse_button.clicked.connect(container.browse)
    ui.vna_browse_button.clicked.connect(container.browse)

    ui.actionAbrir.triggered.connect(container.open_file)
    ui.actionGuardar.triggered.connect(container.save_file)
    ui.actionGuardar_como.triggered.connect(container.save_as_file)
    ui.actionSalir.triggered.connect(container.close)
    ui.actionCalibration.triggered.connect(container.launch_calibration)
    ui.actionCalibration_Presets.triggered.connect(container.launch_preset_calibration)
    ui.actionRI.triggered.connect(container.launch_ri)
    ui.actionContinuo_Alterno.triggered.connect(container.launch_conalt)

    ui.left_button.clicked.connect(container.move_left)
    left_shortcut = QShortcut(QKeySequence(QtCore.Qt.ControlModifier + QtCore.Qt.Key_Left), 
            ui.centralwidget)
    left_shortcut.setContext(QtCore.Qt.ApplicationShortcut)
    left_shortcut.activated.connect(container.move_left)

    ui.right_button.clicked.connect(container.move_right)
    right_shortcut = QShortcut(QKeySequence(QtCore.Qt.ControlModifier + QtCore.Qt.Key_Right),
            ui.centralwidget)
    right_shortcut.setContext(QtCore.Qt.ApplicationShortcut)
    right_shortcut.activated.connect(container.move_right)

    ui.all_checkbox.stateChanged.connect(container.checked_all)

    app.aboutToQuit.connect(container.save_ui)
    restore_ui(ui)
    window.show()
    sys.exit(app.exec_())
