# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/cal_presets.ui'
#
# Created: Tue Apr 15 14:43:54 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_cal_presets(object):
    def setupUi(self, cal_presets):
        cal_presets.setObjectName(_fromUtf8("cal_presets"))
        cal_presets.resize(294, 121)
        self.comboBox = QtGui.QComboBox(cal_presets)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 151, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(cal_presets)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(cal_presets)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 131, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(cal_presets)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 70, 121, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(cal_presets)
        QtCore.QMetaObject.connectSlotsByName(cal_presets)

    def retranslateUi(self, cal_presets):
        cal_presets.setWindowTitle(_translate("cal_presets", "Calibration presets", None))
        self.comboBox.setItemText(0, _translate("cal_presets", "85033E", None))
        self.label.setText(_translate("cal_presets", "Calibration kit", None))
        self.pushButton.setText(_translate("cal_presets", "Full 2-Port", None))
        self.pushButton_2.setText(_translate("cal_presets", "2-Port TRL", None))

