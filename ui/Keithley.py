# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Keithley.ui'
#
# Created: Thu Mar  7 16:08:51 2013
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(718, 349)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.connect_button = QtGui.QPushButton(self.centralwidget)
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        self.horizontalLayout.addWidget(self.connect_button)
        self.ip_file_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.ip_file_layout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.ip_file_layout, 0, 0, 1, 1)
        self.mainLayout = QtGui.QHBoxLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.smu1_label = QtGui.QLabel(self.centralwidget)
        self.smu1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu1_label.setObjectName(_fromUtf8("smu1_label"))
        self.verticalLayout.addWidget(self.smu1_label)
        self.smu1_combo = QtGui.QComboBox(self.centralwidget)
        self.smu1_combo.setObjectName(_fromUtf8("smu1_combo"))
        self.verticalLayout.addWidget(self.smu1_combo)
        self.smu1_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu1_groupbox.setMinimumSize(QtCore.QSize(0, 20))
        self.smu1_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu1_groupbox.setTitle(_fromUtf8(""))
        self.smu1_groupbox.setObjectName(_fromUtf8("smu1_groupbox"))
        self.verticalLayout.addWidget(self.smu1_groupbox)
        self.mainLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.smu2_label = QtGui.QLabel(self.centralwidget)
        self.smu2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu2_label.setObjectName(_fromUtf8("smu2_label"))
        self.verticalLayout_2.addWidget(self.smu2_label)
        self.smu2_combo = QtGui.QComboBox(self.centralwidget)
        self.smu2_combo.setObjectName(_fromUtf8("smu2_combo"))
        self.verticalLayout_2.addWidget(self.smu2_combo)
        self.smu2_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu2_groupbox.setMinimumSize(QtCore.QSize(0, 20))
        self.smu2_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu2_groupbox.setTitle(_fromUtf8(""))
        self.smu2_groupbox.setObjectName(_fromUtf8("smu2_groupbox"))
        self.verticalLayout_2.addWidget(self.smu2_groupbox)
        self.mainLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.smu3_label = QtGui.QLabel(self.centralwidget)
        self.smu3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu3_label.setObjectName(_fromUtf8("smu3_label"))
        self.verticalLayout_3.addWidget(self.smu3_label)
        self.smu3_combo = QtGui.QComboBox(self.centralwidget)
        self.smu3_combo.setObjectName(_fromUtf8("smu3_combo"))
        self.verticalLayout_3.addWidget(self.smu3_combo)
        self.smu3_groupbox = QtGui.QGroupBox(self.centralwidget)
        self.smu3_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.smu3_groupbox.setTitle(_fromUtf8(""))
        self.smu3_groupbox.setObjectName(_fromUtf8("smu3_groupbox"))
        self.verticalLayout_3.addWidget(self.smu3_groupbox)
        self.mainLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.smu4_label = QtGui.QLabel(self.centralwidget)
        self.smu4_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.smu4_label.setObjectName(_fromUtf8("smu4_label"))
        self.verticalLayout_4.addWidget(self.smu4_label)
        self.smu4_combo = QtGui.QComboBox(self.centralwidget)
        self.smu4_combo.setObjectName(_fromUtf8("smu4_combo"))
        self.verticalLayout_4.addWidget(self.smu4_combo)
        self.smu3_groupbox_2 = QtGui.QGroupBox(self.centralwidget)
        self.smu3_groupbox_2.setTitle(_fromUtf8(""))
        self.smu3_groupbox_2.setObjectName(_fromUtf8("smu3_groupbox_2"))
        self.verticalLayout_4.addWidget(self.smu3_groupbox_2)
        self.mainLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.mainLayout, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "SMU", None))
        self.ipLabel.setText(_translate("mainWindow", "IP:", None))
        self.connect_button.setText(_translate("mainWindow", "Conectar", None))
        self.label.setText(_translate("mainWindow", "Archivo:", None))
        self.pushButton.setText(_translate("mainWindow", "Examinar", None))
        self.smu1_label.setText(_translate("mainWindow", "SMU 1", None))
        self.smu2_label.setText(_translate("mainWindow", "SMU 2", None))
        self.smu3_label.setText(_translate("mainWindow", "SMU 3", None))
        self.smu4_label.setText(_translate("mainWindow", "SMU 4", None))

