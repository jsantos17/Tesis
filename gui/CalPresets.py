# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/cal_presets.ui'
#
# Created: Tue Apr 15 16:03:44 2014
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
        self.cal_kit_combo = QtGui.QComboBox(cal_presets)
        self.cal_kit_combo.setGeometry(QtCore.QRect(130, 20, 151, 31))
        self.cal_kit_combo.setObjectName(_fromUtf8("cal_kit_combo"))
        self.cal_kit_combo.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(cal_presets)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.full_2port_button = QtGui.QPushButton(cal_presets)
        self.full_2port_button.setGeometry(QtCore.QRect(20, 70, 131, 31))
        self.full_2port_button.setObjectName(_fromUtf8("full_2port_button"))
        self.trl_2port_button = QtGui.QPushButton(cal_presets)
        self.trl_2port_button.setGeometry(QtCore.QRect(160, 70, 121, 31))
        self.trl_2port_button.setObjectName(_fromUtf8("trl_2port_button"))

        self.retranslateUi(cal_presets)
        QtCore.QMetaObject.connectSlotsByName(cal_presets)

    def retranslateUi(self, cal_presets):
        cal_presets.setWindowTitle(_translate("cal_presets", "Calibration presets", None))
        self.cal_kit_combo.setItemText(0, _translate("cal_presets", "85033E", None))
        self.label.setText(_translate("cal_presets", "Calibration kit", None))
        self.full_2port_button.setText(_translate("cal_presets", "Full 2-Port", None))
        self.trl_2port_button.setText(_translate("cal_presets", "2-Port TRL", None))

