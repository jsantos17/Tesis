import thread
from PyQt4 import QtGui
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import SParameters
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import DataFormat
from time import sleep
from lib.SocketExecutor import SocketExecutor

def VnaMeasureThreaded(ui):
    try:
        ip_port = str(ui.vna_ip_field.text()).split(":")
        ip = ip_port[0]
        port = int(ip_port[1])
    except IndexError as e:
        QtGui.QMessageBox.information(ui.centralwidget,"IP", "Se debe especificar un puerto y un IP en formato IP:puerto")
 
    thread.start_new_thread(VnaMeasure, (ui,ip, port))

def VnaMeasure(ui, ip, port):
    # Disable button after click

    ui.measure_vna.setEnabled(False)
    ui.left_button.setEnabled(False)
    ui.right_button.setEnabled(False)

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
    points = str(ui.points_field.text())
    fmat = DataFormat.LOG # By default we use MLOG
    fmat_index = ui.format_combobox.currentIndex()
    formats = [DataFormat.LOG, 
               DataFormat.LIN, 
               DataFormat.LIN_PHASE, 
               DataFormat.PHASE, 
               DataFormat.GDELAY, 
               DataFormat.SMITH_LIN_PHASE, 
               DataFormat.SMITH_LOG_PHASE, 
               DataFormat.SMITH_RE_IM, 
               DataFormat.SMITH_R_JX, 
               DataFormat.SMITH_G_JB]

    fmat = formats[fmat_index]
    
    if ui.center_span_radio.isChecked():
        groupbox = ui.bottom_layout.itemAt(3).widget()
        center_freq = float(groupbox.findChild(QtGui.QLineEdit, "center_field").text())
        span_freq = float(groupbox.findChild(QtGui.QLineEdit, "span_field").text())
        channel.set_center_span(center_freq, span_freq)
        channel.set_traces(1)
        channel.set_points(points)
        channel.set_sparam(1, spar)
        channel.set_format(fmat) # set the selected format
        channel.activate_channel()
        channel.activate_trace(1)
        
    elif ui.start_stop_radio.isChecked():
        groupbox = ui.bottom_layout.itemAt(3).widget()
        freq_start = float(groupbox.findChild(QtGui.QLineEdit, "freqstart_field").text())
        freq_stop = float(groupbox.findChild(QtGui.QLineEdit, "freqstop_field").text())
        channel.set_start_stop(freq_start, freq_stop)
        channel.set_traces(1)
        channel.set_points(points)
        channel.set_sparam(1, spar)
        channel.set_format(fmat) # set the selected format
        channel.activate_channel()
        channel.activate_trace(1)
        channel.set_continuous()

    if ui.autoscale_checkbox.isChecked():
        channel.auto_scale() # Autoscale

    f = str(ui.vna_file_field.text())
    channel.executor.close()
    # Reenable buttons once measure has finished
    ui.measure_vna.setEnabled(True)
    ui.left_button.setEnabled(True)
    ui.right_button.setEnabled(True)

    thread.start_new_thread(retrieve_data, (ip, port, f))

def retrieve_data(ip, port, fname):
    executor = SocketExecutor(ip, port, expect_reply=False, endline="\n")
    executor.execute_command(":FORM:DATA ASC") # Set data to ASCII

    data = executor.ask(":CALC1:DATA:FDAT?")
    with open(fname + "_vna.csv", "w+") as f:
        data = data.split(",")
        data = [float(i) for i in data]
        for line in data:
#           if int(line) == 0:
#               continue
            f.write(str(line)+"\r\n")

    freq_data = executor.ask(":SENS1:FREQ:DATA?")
    with open(fname + "_freqdata.csv", "w+") as f:
        freq_data = freq_data.split(",")
        freq_data = [float(i) for i in freq_data]
        for line in freq_data:
            f.write(str(line)+"\r\n")

    executor.close()

