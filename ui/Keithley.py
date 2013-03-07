# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Keithley.ui'
#
# Created: Thu Mar  7 12:12:37 2013
#      by: PyQt4 UI code generator 4.9.6
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

#class Ui_mainWindow(object):
class Ui_mainWindow(QtGui.QMainWindow):

    def callback(self, event):
        print self.sender().currentText() 

    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(731, 326)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.smu1_label = QtGui.QLabel(self.centralwidget)
        self.smu1_label.setGeometry(QtCore.QRect(30, 70, 62, 16))
        self.smu1_label.setObjectName(_fromUtf8("smu1_label"))
        self.smu1_combo = QtGui.QComboBox(self.centralwidget)
        self.smu1_combo.setGeometry(QtCore.QRect(30, 90, 141, 24))
        self.smu1_combo.setObjectName(_fromUtf8("smu1_combo"))
        self.smu2_label = QtGui.QLabel(self.centralwidget)
        self.smu2_label.setGeometry(QtCore.QRect(200, 70, 62, 16))
        self.smu2_label.setObjectName(_fromUtf8("smu2_label"))
        self.smu2_combo = QtGui.QComboBox(self.centralwidget)
        self.smu2_combo.setGeometry(QtCore.QRect(200, 90, 141, 24))
        self.smu2_combo.setObjectName(_fromUtf8("smu2_combo"))
        self.smu3_label = QtGui.QLabel(self.centralwidget)
        self.smu3_label.setGeometry(QtCore.QRect(370, 70, 62, 16))
        self.smu3_label.setObjectName(_fromUtf8("smu3_label"))
        self.smu3_combo = QtGui.QComboBox(self.centralwidget)
        self.smu3_combo.setGeometry(QtCore.QRect(370, 90, 151, 24))
        self.smu3_combo.setObjectName(_fromUtf8("smu3_combo"))
        self.smu4_combo = QtGui.QComboBox(self.centralwidget)
        self.smu4_combo.setGeometry(QtCore.QRect(550, 90, 151, 24))
        self.smu4_combo.setObjectName(_fromUtf8("smu4_combo"))
        self.smu4_label = QtGui.QLabel(self.centralwidget)
        self.smu4_label.setGeometry(QtCore.QRect(550, 70, 62, 16))
        self.smu4_label.setObjectName(_fromUtf8("smu4_label"))
        self.ipField = QtGui.QLineEdit(self.centralwidget)
        self.ipField.setGeometry(QtCore.QRect(60, 20, 201, 31))
        self.ipField.setObjectName(_fromUtf8("ipField"))
        self.ipLabel = QtGui.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.ipLabel.setScaledContents(True)
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.connect_button = QtGui.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(270, 20, 92, 31))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        # Connection
        self.smu1_combo.currentIndexChanged.connect(self.callback)
        self.SMU1_GroupBox = QtGui.QGroupBox(self.centralwidget)
        self.SMU1_GroupBox.setGeometry(QtCore.QRect(30, 130, 151, 151))
        self.SMU1_GroupBox.setObjectName(_fromUtf8("SMU1_GroupBox"))
        self.SMU2_GroupBox = QtGui.QGroupBox(self.centralwidget)
        self.SMU2_GroupBox.setGeometry(QtCore.QRect(200, 130, 151, 151))
        self.SMU2_GroupBox.setObjectName(_fromUtf8("SMU2_GroupBox"))
        self.SMU3_GroupBox = QtGui.QGroupBox(self.centralwidget)
        self.SMU3_GroupBox.setGeometry(QtCore.QRect(370, 130, 151, 151))
        self.SMU3_GroupBox.setObjectName(_fromUtf8("SMU3_GroupBox"))
        self.SMU4_GroupBox = QtGui.QGroupBox(self.centralwidget)
        self.SMU4_GroupBox.setGeometry(QtCore.QRect(550, 130, 141, 151))
        self.SMU4_GroupBox.setObjectName(_fromUtf8("SMU4_GroupBox"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "SMU", None))
        self.smu1_label.setText(_translate("mainWindow", "SMU 1", None))
        self.smu1_combo.setItemText(0, _translate("mainWindow", "Open", None))
        self.smu1_combo.setItemText(1, _translate("mainWindow", "Current Bias", None))
        self.smu1_combo.setItemText(2, _translate("mainWindow", "Current Sweep", None))
        self.smu1_combo.setItemText(3, _translate("mainWindow", "Current List Sweep", None))
        self.smu1_combo.setItemText(4, _translate("mainWindow", "Current Step", None))
        self.smu1_combo.setItemText(5, _translate("mainWindow", "Voltage Bias", None))
        self.smu1_combo.setItemText(6, _translate("mainWindow", "Voltage Sweep", None))
        self.smu1_combo.setItemText(7, _translate("mainWindow", "Voltage List Sweep", None))
        self.smu1_combo.setItemText(8, _translate("mainWindow", "Voltage Step", None))
        self.smu2_label.setText(_translate("mainWindow", "SMU 2", None))
        self.smu3_label.setText(_translate("mainWindow", "SMU 3", None))
        self.smu4_label.setText(_translate("mainWindow", "SMU 4", None))
        self.ipLabel.setText(_translate("mainWindow", "IP:", None))
        self.connect_button.setText(_translate("mainWindow", "Conectar", None))
        self.SMU1_GroupBox.setTitle(_translate("mainWindow", "SMU1", None))
        self.SMU2_GroupBox.setTitle(_translate("mainWindow", "SMU2", None))
        self.SMU3_GroupBox.setTitle(_translate("mainWindow", "SMU3", None))
        self.SMU4_GroupBox.setTitle(_translate("mainWindow", "SMU4", None))

