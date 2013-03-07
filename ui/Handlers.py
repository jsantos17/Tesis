from PyQt4 import QtGui


class SlotContainer(QtGui.QMainWindow):
    def on_measure_select(event):
        print event.sender().currentText()

