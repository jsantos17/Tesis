import thread
from PyQt4 import QtGui
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import SParameters
from lib.util.VnaEnums import SweepType
from time import sleep

def VnaMeasure(ui):
    try:
        ip_port = str(ui.ipField.text()).split(":")
        ip = ip_port[0]
        port = int(ip_port[1])
    except IndexError as e:
        QtGui.QMessageBox.information(ui.centralwidget,"IP", "Se debe especificar un puerto y un IP en formato IP:puerto")
    channel = VnaChannel(ip, port, 1) # One channel
    channel.reset()
    channel.set_sweep_type(SweepType.LINEAR)
    if ui.s11_radio.isChecked():
        spar = SParameters.S11
    elif ui.s12_radio.isChecked():
        spar = SParameters.S12
    elif ui.s21_radio.isChecked():
        spar = SParameters.S21
    elif ui.s22_radio.isChecked():
        spar = SParameters.S22

    if ui.center_span_radio.isChecked():
        groupbox = ui.bottom_layout.itemAt(2).widget()
        center_freq = float(groupbox.findChild(QtGui.QLineEdit, "center_field").text())
        span_freq = float(groupbox.findChild(QtGui.QLineEdit, "span_field").text())
        channel.set_center_span(center_freq, span_freq)
        channel.set_traces(1)
        channel.set_sparam(1, spar)
        channel.activate_channel()
        channel.activate_trace(1)
        channel.trigger()
        
    elif ui.start_stop_radio.isChecked():
        groupbox = ui.bottom_layout.itemAt(2).widget()
        freq_start = float(groupbox.findChild(QtGui.QLineEdit, "freqstart_field").text())
        freq_stop = float(groupbox.findChild(QtGui.QLineEdit, "freqstop_field").text())
        channel.set_start_stop(freq_start, freq_stop)
        channel.set_traces(1)
        channel.set_sparam(1, spar)
        channel.activate_channel()
        channel.activate_trace(1)
        channel.trigger()

    f = str(i.fileField.text())
    thread.start_new_thread(retrieve_data, (ip, port, f))

def retrieve_data(ip, port, fname):
    print "Will wait 5 seconds before retrieving data"
    sleep(5)
    executor = SocketExecutor(ip, port)
    executor.execute_command(":FORM:DATA ASC") # Set data to ASCII
    executor.execute_command(":CALC1:DATA:FDAT?")
    data = executor.get_data()

    with open(fname + "_vna", "w+") as f:
        f.write(data)

    executor.execute_command("SENS1:FREQ:DATA?")
    freq_data = executor.get_data()
    
    with open(fname + "_freqdata", "w+") as f:
        f.write(freq_data)

    executor.close()

