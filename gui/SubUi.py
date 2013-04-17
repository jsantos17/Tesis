from PyQt4 import QtGui, QtCore 

def get_step_groupbox():
    step_groupbox = QtGui.QGroupBox()
    step_groupbox.setGeometry(QtCore.QRect(0, 10, 301, 140))
    step_groupbox.setTitle("")
    step_groupbox.setObjectName("step_groupbox")
    val_interval_field = QtGui.QLineEdit(step_groupbox)
    val_interval_field.setGeometry(QtCore.QRect(120, 50, 151, 25))
    val_interval_field.setObjectName("val_interval_field")
    value_interval = QtGui.QLabel(step_groupbox)
    value_interval.setGeometry(QtCore.QRect(10, 50, 91, 16))
    value_interval.setObjectName("value_interval")
    value_init = QtGui.QLabel(step_groupbox)
    value_init.setGeometry(QtCore.QRect(10, 20, 71, 16))
    value_init.setObjectName("value_init")
    val_inicio_field = QtGui.QLineEdit(step_groupbox)
    val_inicio_field.setGeometry(QtCore.QRect(120, 20, 151, 25))
    val_inicio_field.setObjectName("val_inicio_field")
    step_number = QtGui.QLabel(step_groupbox)
    step_number.setGeometry(QtCore.QRect(10, 70, 81, 31))
    step_number.setWordWrap(True)
    step_number.setObjectName("step_number")
    step_number_field = QtGui.QLineEdit(step_groupbox)
    step_number_field.setGeometry(QtCore.QRect(120, 80, 151, 25))
    step_number_field.setObjectName("step_number_field")
    compliance_label = QtGui.QLabel(step_groupbox)
    compliance_label.setGeometry(QtCore.QRect(10, 110, 81, 16))
    compliance_label.setObjectName("compliance_label")
    compliance_field = QtGui.QLineEdit(step_groupbox)
    compliance_field.setGeometry(QtCore.QRect(120, 110, 151, 25))
    compliance_field.setObjectName("compliance_field")
    value_init.setText("Valor inicio: ")
    value_interval.setText("Intervalo: ")
    step_number.setText("Numero de pasos: ")
    compliance_label.setText("Compliance: ")
    return step_groupbox

def get_sweep_groupbox():
    sweep_groupbox = QtGui.QGroupBox()
    sweep_groupbox.setGeometry(QtCore.QRect(30, 20, 271, 140))
    #sweep_groupbox.setGeometry(QtCore.QRect(0, 0, 271, 131))
    sweep_groupbox.setTitle("")
    sweep_groupbox.setObjectName("sweep_groupbox")
    val_stop_field = QtGui.QLineEdit(sweep_groupbox)
    val_stop_field.setGeometry(QtCore.QRect(100, 80, 161, 25))
    val_stop_field.setObjectName("val_stop_field")
    sweep_type_label = QtGui.QLabel(sweep_groupbox)
    sweep_type_label.setGeometry(QtCore.QRect(6, 10, 81, 20))
    sweep_type_label.setObjectName("sweep_type_label")
    combobox = QtGui.QComboBox(sweep_groupbox)
    combobox.setGeometry(QtCore.QRect(100, 10, 161, 25))
    combobox.setObjectName("sweep_type_combobox")
    combobox.addItem("Linear")
    combobox.addItem("Log10")
    combobox.addItem("Log25")
    combobox.addItem("Log50")
    value_stop = QtGui.QLabel(sweep_groupbox)
    value_stop.setGeometry(QtCore.QRect(10, 90, 71, 16))
    value_stop.setObjectName("value_stop")
    value_init = QtGui.QLabel(sweep_groupbox)
    value_init.setGeometry(QtCore.QRect(10, 50, 71, 16))
    value_init.setObjectName("value_init")
    value_init.setText("Valor inicio: ")
    value_stop.setText("Valor final: ")
    val_inicio_field = QtGui.QLineEdit(sweep_groupbox)
    val_inicio_field.setGeometry(QtCore.QRect(100, 50, 161, 25))
    val_inicio_field.setObjectName("val_inicio_field")
    compliance_label = QtGui.QLabel(sweep_groupbox)
    compliance_label.setGeometry(QtCore.QRect(10, 120, 80, 16))
    compliance_label.setObjectName("compliance_label")
    compliance_label.setText("Compliance: ")
    compliance_field = QtGui.QLineEdit(sweep_groupbox)
    compliance_field.setGeometry(QtCore.QRect(100, 110, 161, 25))

    step_label = QtGui.QLabel(sweep_groupbox)
    step_label.setGeometry(QtCore.QRect(10, 150, 80, 16))
    step_label.setObjectName("step_label")
    step_label.setText("Step: ")
    step_field = QtGui.QLineEdit(sweep_groupbox)
    step_field.setGeometry(QtCore.QRect(100, 140, 161, 25))

    return sweep_groupbox

def get_constant_groupbox():
    constant_groupbox = QtGui.QGroupBox()
    constant_groupbox.setGeometry(QtCore.QRect(10, 10, 181, 140))
    constant_groupbox.setTitle("")
    constant_groupbox.setObjectName("constant_groupbox")
    constant_label = QtGui.QLabel(constant_groupbox)
    constant_label.setGeometry(QtCore.QRect(10, 30, 61, 14))
    constant_label.setObjectName("constant_label")
    constant_textbox = QtGui.QLineEdit(constant_groupbox)
    constant_textbox.setGeometry(QtCore.QRect(60, 25, 113, 22))
    constant_textbox.setObjectName("constant_textbox") 
    constant_label.setText("Valor") 
    return constant_groupbox

def get_list_groupbox():
    list_groupbox = QtGui.QGroupBox()
    textEdit = QtGui.QTextEdit(list_groupbox)
    textEdit.setGeometry(QtCore.QRect(0, 20, 250, 140))
    textEdit.setObjectName("list_textedit")
    label = QtGui.QLabel(list_groupbox)
    label.setGeometry(QtCore.QRect(0, 0, 250, 19))
    label.setObjectName("label_description")
    label.setText("Lista de valores separados por comas")
    return list_groupbox

def get_start_stop_ui():
    freq_groupbox = QtGui.QGroupBox()
    freq_groupbox.setGeometry(QtCore.QRect(10, 0, 373, 140))
    freq_groupbox.setObjectName("freq_groupbox")
    verticalLayoutWidget = QtGui.QWidget(freq_groupbox)
    verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 341, 107))
    verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    verticalLayout = QtGui.QVBoxLayout(verticalLayoutWidget)
    verticalLayout.setMargin(0)
    verticalLayout.setObjectName("verticalLayout")
    horizontalLayout_6 = QtGui.QHBoxLayout()
    horizontalLayout_6.setObjectName("horizontalLayout_6")
    freqstart_label = QtGui.QLabel(verticalLayoutWidget)
    freqstart_label.setObjectName("freqstart_label")
    horizontalLayout_6.addWidget(freqstart_label)
    freqstart_field = QtGui.QLineEdit(verticalLayoutWidget)
    freqstart_field.setObjectName("freqstart_field")
    horizontalLayout_6.addWidget(freqstart_field)
    verticalLayout.addLayout(horizontalLayout_6)
    horizontalLayout_4 = QtGui.QHBoxLayout()
    horizontalLayout_4.setObjectName("horizontalLayout_4")
    freqstop_label = QtGui.QLabel(verticalLayoutWidget)
    freqstop_label.setObjectName("freqstop_label")
    horizontalLayout_4.addWidget(freqstop_label)
    freqstop_field = QtGui.QLineEdit(verticalLayoutWidget)
    freqstop_field.setObjectName("freqstop_field")
    horizontalLayout_4.addWidget(freqstop_field)
    verticalLayout.addLayout(horizontalLayout_4)
    horizontalLayout_5 = QtGui.QHBoxLayout()
    horizontalLayout_5.setObjectName("horizontalLayout_5")
    range_label = QtGui.QLabel(verticalLayoutWidget)
    range_label.setObjectName("range_label")
    horizontalLayout_5.addWidget(range_label)
    range_field = QtGui.QLineEdit(verticalLayoutWidget)
    range_field.setObjectName("range_field")
    horizontalLayout_5.addWidget(range_field)
    verticalLayout.addLayout(horizontalLayout_5)
    freq_groupbox.setTitle("Frecuencia")
    freqstart_label.setText("Frecuencia inicial")
    freqstop_label.setText("Frecuencia final")
    range_label.setText("Rango")
    return freq_groupbox

def get_center_span_ui():
    freq_groupbox = QtGui.QGroupBox()
    freq_groupbox.setGeometry(QtCore.QRect(0, 0, 373, 148))
    freq_groupbox.setObjectName("freq_groupbox")
    verticalLayoutWidget = QtGui.QWidget(freq_groupbox)
    verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 341, 107))
    verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    verticalLayout = QtGui.QVBoxLayout(verticalLayoutWidget)
    verticalLayout.setMargin(0)
    verticalLayout.setObjectName("verticalLayout")
    horizontalLayout_6 = QtGui.QHBoxLayout()
    horizontalLayout_6.setObjectName("horizontalLayout_6")
    center_label = QtGui.QLabel(verticalLayoutWidget)
    center_label.setObjectName("center_label")
    horizontalLayout_6.addWidget(center_label)
    center_field = QtGui.QLineEdit(verticalLayoutWidget)
    center_field.setObjectName("center_field")
    horizontalLayout_6.addWidget(center_field)
    verticalLayout.addLayout(horizontalLayout_6)
    horizontalLayout_4 = QtGui.QHBoxLayout()
    horizontalLayout_4.setObjectName("horizontalLayout_4")
    span_label = QtGui.QLabel(verticalLayoutWidget)
    span_label.setObjectName("span_label")
    horizontalLayout_4.addWidget(span_label)
    span_field = QtGui.QLineEdit(verticalLayoutWidget)
    span_field.setObjectName("span_field")
    horizontalLayout_4.addWidget(span_field)
    verticalLayout.addLayout(horizontalLayout_4)
    freq_groupbox.setTitle("Frecuencia")
    center_label.setText("Centro")
    span_label.setText("Span")
    return freq_groupbox
