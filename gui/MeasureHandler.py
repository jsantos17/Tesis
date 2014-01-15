from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep
from lib.SMUStep import SMUStep
from lib.SMUConstant import SMUConstant
from lib.SMU import SMUConfigError
from lib.K4200 import K4200

class MeasureHandler(QtGui.QMainWindow):

    def __init__(self, ip=None, port=None):
        pass


    def handle(self, event, ui, params):
        self.device = K4200(self.ip, self.port)
        ip = ui.ipField.text()
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

        try:
            for element in active:
                combo = element['combo']
                layout = element['layout']
                groupbox = layout.itemAt(2).widget()
                ch = int(str(combo.objectName())[3:4])
                source_mode = SourceMode.CURRENT if "current" in combo.currentText().toLower() else SourceMode.VOLTAGE
                source_type = SourceType.CURRENT if "current" in combo.currentText().toLower() else SourceType.VOLTAGE

                    
                if "constant" in combo.currentText().toLower():
                    value = float(groupbox.findChild(QtGui.QLineEdit, "constant_textbox").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_textbox").text())
                    smu = SMUConstant(ch, source_mode, source_type, value, compliance, "V%s"%ch, "I%s"%ch)
                    self.device.attach(smu)

                elif "list" in combo.currentText().toLower():
                    # Current list sweep configuration for SMU
                    # Channel don't have a list sourcing function (!)
                    pass
                
                elif "sweep" in combo.currentText().toLower():
                    # Current sweep configuration for SMU
                    stop = float(groupbox.findChild(QtGui.QLineEdit, "val_stop_field").text())
                    start = float(groupbox.findChild(QtGui.QLineEdit, "val_inicio_field").text())
                    step = float(groupbox.findChild(QtGui.QLineEdit, "step_field").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_field").text())
                    st = str(groupbox.findChild(QtGui.QComboBox, "sweep_type_combobox").currentText())
                    if st == "Linear":
                        sweep_type = SweepType.LINEAR
                    elif st == "Log10":
                        sweep_type = SweepType.LOG10
                    elif st == "Log25":
                        sweep_type = SweepType.LOG25
                    elif st == "Log50":
                        sweep_type = SweepType.LOG50

                    smu = SMUSweep(ch, source_mode, source_type, start, stop, step, compliance,
                                   sweep_type, 'V%s' % ch, "I%s"%ch)
                    self.device.attach(smu)

                elif "step" in combo.currentText().toLower():
                    # Current step configuration for SMU
                    start = float(groupbox.findChild(QtGui.QLineEdit, "start_lineedit").text())
                    step = float(groupbox.findChild(QtGui.QLineEdit, "step_lineedit").text())
                    steps = int(groupbox.findChild(QtGui.QLineEdit, "steps_lineedit").text())
                    compliance = float(groupbox.findChild(QtGui.QLineEdit, "compliance_lineedit").text())

                    smu = SMUStep(ch, source_mode, source_type, start, step, steps, compliance,
                                  voltage_name='V%s'%ch, current_name='I%s'%ch)
                    self.device.attach(smu)


            print "Attached SMUs: %s" % len(self.device.smus)
            self.device.configure() # Configure for measure
            self.device.measure() # Measure
            ui.save_button.setEnabled(True)

        except SMUConfigError as e:
            QtGui.QMessageBox.information(ui.centralwidget, "Revisar valores", e.message)

