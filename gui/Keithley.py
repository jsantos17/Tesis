# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/Keithley.ui'
#
# Created: Tue Jan 28 13:27:40 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1150, 641)
        mainWindow.setMinimumSize(QtCore.QSize(1150, 500))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mainLayout = QtGui.QHBoxLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.smu1_layout = QtGui.QVBoxLayout()
        self.smu1_layout.setObjectName(_fromUtf8("smu1_layout"))
        self.smu1_label = QtGui.QLabel(self.centralwidget)
        self.smu1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu1_label.setObjectName(_fromUtf8("smu1_label"))
        self.smu1_layout.addWidget(self.smu1_label)
        self.smu1_combo = QtGui.QComboBox(self.centralwidget)
        self.smu1_combo.setObjectName(_fromUtf8("smu1_combo"))
        self.smu1_layout.addWidget(self.smu1_combo)
        self.smu1_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu1_groupbox.setMinimumSize(QtCore.QSize(0, 200))
        self.smu1_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu1_groupbox.setTitle(_fromUtf8(""))
        self.smu1_groupbox.setObjectName(_fromUtf8("smu1_groupbox"))
        self.smu1_layout.addWidget(self.smu1_groupbox)
        self.mainLayout.addLayout(self.smu1_layout)
        self.smu2_layout = QtGui.QVBoxLayout()
        self.smu2_layout.setObjectName(_fromUtf8("smu2_layout"))
        self.smu2_label = QtGui.QLabel(self.centralwidget)
        self.smu2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu2_label.setObjectName(_fromUtf8("smu2_label"))
        self.smu2_layout.addWidget(self.smu2_label)
        self.smu2_combo = QtGui.QComboBox(self.centralwidget)
        self.smu2_combo.setObjectName(_fromUtf8("smu2_combo"))
        self.smu2_layout.addWidget(self.smu2_combo)
        self.smu2_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu2_groupbox.setMinimumSize(QtCore.QSize(0, 200))
        self.smu2_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu2_groupbox.setTitle(_fromUtf8(""))
        self.smu2_groupbox.setObjectName(_fromUtf8("smu2_groupbox"))
        self.smu2_layout.addWidget(self.smu2_groupbox)
        self.mainLayout.addLayout(self.smu2_layout)
        self.smu3_layout = QtGui.QVBoxLayout()
        self.smu3_layout.setObjectName(_fromUtf8("smu3_layout"))
        self.smu3_label = QtGui.QLabel(self.centralwidget)
        self.smu3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu3_label.setObjectName(_fromUtf8("smu3_label"))
        self.smu3_layout.addWidget(self.smu3_label)
        self.smu3_combo = QtGui.QComboBox(self.centralwidget)
        self.smu3_combo.setObjectName(_fromUtf8("smu3_combo"))
        self.smu3_layout.addWidget(self.smu3_combo)
        self.smu3_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu3_groupbox.setMinimumSize(QtCore.QSize(0, 200))
        self.smu3_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu3_groupbox.setTitle(_fromUtf8(""))
        self.smu3_groupbox.setObjectName(_fromUtf8("smu3_groupbox"))
        self.smu3_layout.addWidget(self.smu3_groupbox)
        self.mainLayout.addLayout(self.smu3_layout)
        self.smu4_layout = QtGui.QVBoxLayout()
        self.smu4_layout.setObjectName(_fromUtf8("smu4_layout"))
        self.smu4_label = QtGui.QLabel(self.centralwidget)
        self.smu4_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu4_label.setObjectName(_fromUtf8("smu4_label"))
        self.smu4_layout.addWidget(self.smu4_label)
        self.smu4_combo = QtGui.QComboBox(self.centralwidget)
        self.smu4_combo.setObjectName(_fromUtf8("smu4_combo"))
        self.smu4_layout.addWidget(self.smu4_combo)
        self.smu4_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu4_groupbox.setEnabled(True)
        self.smu4_groupbox.setMinimumSize(QtCore.QSize(0, 200))
        self.smu4_groupbox.setTitle(_fromUtf8(""))
        self.smu4_groupbox.setObjectName(_fromUtf8("smu4_groupbox"))
        self.smu4_layout.addWidget(self.smu4_groupbox)
        self.mainLayout.addLayout(self.smu4_layout)
        self.gridLayout.addLayout(self.mainLayout, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.ip_file_layout = QtGui.QVBoxLayout()
        self.ip_file_layout.setObjectName(_fromUtf8("ip_file_layout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ipLabel = QtGui.QLabel(self.centralwidget)
        self.ipLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ipLabel.setScaledContents(True)
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.horizontalLayout.addWidget(self.ipLabel)
        self.ipField = QtGui.QLineEdit(self.centralwidget)
        self.ipField.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ipField.setObjectName(_fromUtf8("ipField"))
        self.horizontalLayout.addWidget(self.ipField)
        self.ip_file_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.fileField = QtGui.QLineEdit(self.centralwidget)
        self.fileField.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fileField.setObjectName(_fromUtf8("fileField"))
        self.horizontalLayout_2.addWidget(self.fileField)
        self.browse_button = QtGui.QPushButton(self.centralwidget)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout_2.addWidget(self.browse_button)
        self.ip_file_layout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.ip_file_layout, 0, 0, 1, 1)
        self.bottom_layout = QtGui.QHBoxLayout()
        self.bottom_layout.setObjectName(_fromUtf8("bottom_layout"))
        self.s_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.s_groupbox.setObjectName(_fromUtf8("s_groupbox"))
        self.s11_radio = QtGui.QRadioButton(self.s_groupbox)
        self.s11_radio.setGeometry(QtCore.QRect(40, 30, 61, 24))
        self.s11_radio.setChecked(True)
        self.s11_radio.setObjectName(_fromUtf8("s11_radio"))
        self.s12_radio = QtGui.QRadioButton(self.s_groupbox)
        self.s12_radio.setGeometry(QtCore.QRect(40, 50, 61, 24))
        self.s12_radio.setObjectName(_fromUtf8("s12_radio"))
        self.s21_radio = QtGui.QRadioButton(self.s_groupbox)
        self.s21_radio.setGeometry(QtCore.QRect(40, 70, 61, 24))
        self.s21_radio.setObjectName(_fromUtf8("s21_radio"))
        self.s22_radio = QtGui.QRadioButton(self.s_groupbox)
        self.s22_radio.setGeometry(QtCore.QRect(40, 90, 61, 24))
        self.s22_radio.setObjectName(_fromUtf8("s22_radio"))
        self.bottom_layout.addWidget(self.s_groupbox)
        self.format_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.format_groupbox.setObjectName(_fromUtf8("format_groupbox"))
        self.format_combobox = QtGui.QComboBox(self.format_groupbox)
        self.format_combobox.setGeometry(QtCore.QRect(30, 40, 231, 31))
        self.format_combobox.setObjectName(_fromUtf8("format_combobox"))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.format_combobox.addItem(_fromUtf8(""))
        self.bottom_layout.addWidget(self.format_groupbox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.measuretype_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.measuretype_groupbox.setObjectName(_fromUtf8("measuretype_groupbox"))
        self.start_stop_radio = QtGui.QRadioButton(self.measuretype_groupbox)
        self.start_stop_radio.setGeometry(QtCore.QRect(80, 40, 104, 24))
        self.start_stop_radio.setChecked(True)
        self.start_stop_radio.setObjectName(_fromUtf8("start_stop_radio"))
        self.center_span_radio = QtGui.QRadioButton(self.measuretype_groupbox)
        self.center_span_radio.setGeometry(QtCore.QRect(80, 70, 104, 24))
        self.center_span_radio.setObjectName(_fromUtf8("center_span_radio"))
        self.verticalLayout_2.addWidget(self.measuretype_groupbox)
        self.bottom_layout.addLayout(self.verticalLayout_2)
        self.freq_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.freq_groupbox.setObjectName(_fromUtf8("freq_groupbox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.freq_groupbox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 341, 107))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.freqstart_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.freqstart_label.setObjectName(_fromUtf8("freqstart_label"))
        self.horizontalLayout_6.addWidget(self.freqstart_label)
        self.freqstart_field = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.freqstart_field.setObjectName(_fromUtf8("freqstart_field"))
        self.horizontalLayout_6.addWidget(self.freqstart_field)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.freqstop_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.freqstop_label.setObjectName(_fromUtf8("freqstop_label"))
        self.horizontalLayout_4.addWidget(self.freqstop_label)
        self.freqstop_field = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.freqstop_field.setObjectName(_fromUtf8("freqstop_field"))
        self.horizontalLayout_4.addWidget(self.freqstop_field)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.range_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.range_label.setObjectName(_fromUtf8("range_label"))
        self.horizontalLayout_5.addWidget(self.range_label)
        self.range_field = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.range_field.setObjectName(_fromUtf8("range_field"))
        self.horizontalLayout_5.addWidget(self.range_field)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.bottom_layout.addWidget(self.freq_groupbox)
        self.gridLayout.addLayout(self.bottom_layout, 5, 0, 1, 1)
        self.measure_button = QtGui.QPushButton(self.centralwidget)
        self.measure_button.setObjectName(_fromUtf8("measure_button"))
        self.gridLayout.addWidget(self.measure_button, 1, 0, 1, 1)
        self.measure_vna = QtGui.QPushButton(self.centralwidget)
        self.measure_vna.setObjectName(_fromUtf8("measure_vna"))
        self.gridLayout.addWidget(self.measure_vna, 4, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "SMU", None))
        self.smu1_label.setText(_translate("mainWindow", "SMU 1", None))
        self.smu2_label.setText(_translate("mainWindow", "SMU 2", None))
        self.smu3_label.setText(_translate("mainWindow", "SMU 3", None))
        self.smu4_label.setText(_translate("mainWindow", "SMU 4", None))
        self.ipLabel.setText(_translate("mainWindow", "IP:", None))
        self.label.setText(_translate("mainWindow", "Archivo:", None))
        self.browse_button.setText(_translate("mainWindow", "Examinar", None))
        self.s_groupbox.setTitle(_translate("mainWindow", "Parámetros S a medir", None))
        self.s11_radio.setText(_translate("mainWindow", "S11", None))
        self.s12_radio.setText(_translate("mainWindow", "S12", None))
        self.s21_radio.setText(_translate("mainWindow", "S21", None))
        self.s22_radio.setText(_translate("mainWindow", "S22", None))
        self.format_groupbox.setTitle(_translate("mainWindow", "Formato de Datos", None))
        self.format_combobox.setItemText(0, _translate("mainWindow", "Log", None))
        self.format_combobox.setItemText(1, _translate("mainWindow", "Lin", None))
        self.format_combobox.setItemText(2, _translate("mainWindow", "Lin/Phase", None))
        self.format_combobox.setItemText(3, _translate("mainWindow", "Log/Phase", None))
        self.format_combobox.setItemText(4, _translate("mainWindow", "Phase", None))
        self.format_combobox.setItemText(5, _translate("mainWindow", "Group Delay", None))
        self.format_combobox.setItemText(6, _translate("mainWindow", "Smith Chart (Lin/Phase)", None))
        self.format_combobox.setItemText(7, _translate("mainWindow", "Smith Chart (Log/Phase)", None))
        self.format_combobox.setItemText(8, _translate("mainWindow", "Smith (Re/Im)", None))
        self.format_combobox.setItemText(9, _translate("mainWindow", "Smith (R+jX)", None))
        self.format_combobox.setItemText(10, _translate("mainWindow", "Smith (G+jB)", None))
        self.measuretype_groupbox.setTitle(_translate("mainWindow", "Tipo de medición", None))
        self.start_stop_radio.setText(_translate("mainWindow", "Inicio-final", None))
        self.center_span_radio.setText(_translate("mainWindow", "Centro-span", None))
        self.freq_groupbox.setTitle(_translate("mainWindow", "Frecuencia", None))
        self.freqstart_label.setText(_translate("mainWindow", "Frecuencia inicial", None))
        self.freqstop_label.setText(_translate("mainWindow", "Frecuencia final", None))
        self.range_label.setText(_translate("mainWindow", "Rango", None))
        self.measure_button.setText(_translate("mainWindow", "Medir K4200", None))
        self.measure_vna.setText(_translate("mainWindow", "Medir E5071C", None))

