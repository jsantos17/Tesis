# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/calibration.ui'
#
# Created: Mon Mar 10 11:40:09 2014
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

class Ui_cal_dialog(object):
    def setupUi(self, cal_dialog):
        cal_dialog.setObjectName(_fromUtf8("cal_dialog"))
        cal_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        cal_dialog.resize(293, 286)
        self.open_button = QtGui.QPushButton(cal_dialog)
        self.open_button.setGeometry(QtCore.QRect(10, 120, 271, 41))
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.cal_kit_combo = QtGui.QComboBox(cal_dialog)
        self.cal_kit_combo.setGeometry(QtCore.QRect(130, 30, 151, 31))
        self.cal_kit_combo.setObjectName(_fromUtf8("cal_kit_combo"))
        self.cal_kit_label = QtGui.QLabel(cal_dialog)
        self.cal_kit_label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.cal_kit_label.setObjectName(_fromUtf8("cal_kit_label"))
        self.cal_type_label = QtGui.QLabel(cal_dialog)
        self.cal_type_label.setEnabled(True)
        self.cal_type_label.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.cal_type_label.setObjectName(_fromUtf8("cal_type_label"))
        self.cal_type_combo = QtGui.QComboBox(cal_dialog)
        self.cal_type_combo.setGeometry(QtCore.QRect(130, 72, 151, 31))
        self.cal_type_combo.setObjectName(_fromUtf8("cal_type_combo"))
        self.cal_type_combo.addItem(_fromUtf8(""))
        self.cal_type_combo.addItem(_fromUtf8(""))
        self.cal_type_combo.addItem(_fromUtf8(""))
        self.short_button = QtGui.QPushButton(cal_dialog)
        self.short_button.setGeometry(QtCore.QRect(10, 170, 271, 41))
        self.short_button.setObjectName(_fromUtf8("short_button"))
        self.load_button = QtGui.QPushButton(cal_dialog)
        self.load_button.setGeometry(QtCore.QRect(10, 220, 271, 41))
        self.load_button.setObjectName(_fromUtf8("load_button"))

        self.retranslateUi(cal_dialog)
        QtCore.QMetaObject.connectSlotsByName(cal_dialog)

    def retranslateUi(self, cal_dialog):
        cal_dialog.setWindowTitle(_translate("cal_dialog", "Calibration VNA", None))
        self.open_button.setText(_translate("cal_dialog", "Open", None))
        self.cal_kit_label.setText(_translate("cal_dialog", "Calibration kit:", None))
        self.cal_type_label.setText(_translate("cal_dialog", "Calibration type:", None))
        self.cal_type_combo.setItemText(0, _translate("cal_dialog", "Open", None))
        self.cal_type_combo.setItemText(1, _translate("cal_dialog", "Short", None))
        self.cal_type_combo.setItemText(2, _translate("cal_dialog", "Through", None))
        self.short_button.setText(_translate("cal_dialog", "Short", None))
        self.load_button.setText(_translate("cal_dialog", "Load", None))

