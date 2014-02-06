from utils import save_ui_file
from utils import restore_ui_file
from PyQt4.QtGui import QFileDialog

def handle_save(ui):
    pass
    
def handle_save_as(ui):
    file_name = QFileDialog.getSaveFileName(ui.centralwidget, "Nombre del archivo", "~/untitled.yml", "YAML files (*.yaml, *.yml)")
    save_ui_file(ui, file_name)

def handle_open(ui):
    file_name = QFileDialog.getOpenFileName(ui.centralwidget, "Nombre del archivo", "~", "YAML files (*.yaml, *.yml)")
    restore_ui_file(ui, file_name)

def handle_close(ui):
    pass
