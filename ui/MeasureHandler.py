from PyQt4 import QtGui
from PyQt4.QtCore import QObject

class MeasureHandler(QtGui.QMainWindow):

    def handle(self, event, ui, params):
        print ui.fileField.text() 
