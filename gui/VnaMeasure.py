import thread
from PyQt4 import QtGui
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import SParameters
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import DataFormat
from lib.util.DataTransformers import z_from_s, y_from_s
from time import sleep
from lib.SocketExecutor import SocketExecutor

sdata = []

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
    # channel.reset()
    for spar in [SParameters.S11, SParameters.S12, SParameters.S21, SParameters.S22]:
        
        channel.set_sweep_type(SweepType.LINEAR)
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

        retrieve_data(ip, port, f)

def write_vectors(lvectors, fname):
    with open("{fname}.csv".format(fname=fname), "w+") as f:
        for idx, d in enumerate(lvectors):
            f.write(str(d[idx][0])+","+str(d[idx][1])+","+str(d[idx][2])+","+str(d[idx][3])+"\r\n"

def retrieve_data(ip, port, fname):
    executor = SocketExecutor(ip, port, expect_reply=False, endline="\n")
    executor.execute_command(":FORM:DATA ASC") # Set data to ASCII

    data = executor.ask(":CALC1:DATA:FDAT?")

    data = data.split(",")
    data = [float(i) for i in data]
    sdata.append(data)

    if len(sdata) == 4: # Everything measured
        
        write_vectors(sdata, fname+"_vna_s") 
        write_vectors(y_from_s(sdata), fname+"_vna_y") 
        write_vectors(z_from_s(sdata), fname+"_vna_z")

        freq_data = executor.ask(":SENS1:FREQ:DATA?")
        with open(fname + "_freqdata.csv", "w+") as f:
            freq_data = freq_data.split(",")
            freq_data = [float(i) for i in freq_data]
            for line in freq_data:
                f.write(str(line)+"\r\n")

    executor.close()


