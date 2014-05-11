import thread
from PyQt4 import QtGui
from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import SParameters
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import DataFormat
from lib.util.DataTransformers import z_from_s, y_from_s, cga_from_s, cgs_from_s
from lib.SocketExecutor import SocketExecutor

sdata = []

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def VnaMeasureThreaded(ui):
    try:
        ip_port = str(ui.vna_ip_field.text()).split(":")
        ip = ip_port[0]
        port = int(ip_port[1])
    except IndexError as e:
        QtGui.QMessageBox.information(ui.centralwidget,"IP", "Se debe especificar un puerto y un IP en formato IP:puerto")
    
    if ui.all_checkbox.isChecked(): 
        thread.start_new_thread(VnaMeasure, (ui,ip, port))
    else:
        thread.start_new_thread(VnaMeasureSingle, (ui,ip, port))


def VnaMeasureSingle(ui, ip, port):
    ui.measure_vna.setEnabled(False)
    ui.left_button.setEnabled(False)
    ui.right_button.setEnabled(False)

    channel = VnaChannel(ip, port, 1) # One channel
    # channel.reset()
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
        channel.set_continuous(True)
        
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
        channel.set_continuous(True)

    if ui.autoscale_checkbox.isChecked():
        channel.auto_scale() # Autoscale

    f = str(ui.vna_file_field.text())
    channel.executor.close()
    # Reenable buttons once measure has finished
    ui.measure_vna.setEnabled(True)
    ui.left_button.setEnabled(True)
    ui.right_button.setEnabled(True)

    thread.start_new_thread(retrieve_data_single, (ip, port, f))

def VnaMeasure(ui, ip, port):
    # Disable button after click

    ui.measure_vna.setEnabled(False)
    ui.left_button.setEnabled(False)
    ui.right_button.setEnabled(False)

    channel = VnaChannel(ip, port, 1) # One channel
    # channel.reset()
    sdata = [] # Clean sdata for each measure
    for spar in [SParameters.S11, SParameters.S12, SParameters.S21, SParameters.S22]:
        print "Now measuring: " + str(spar)
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
            channel.set_continuous(True)
            
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
            channel.set_continuous(True)

        if ui.autoscale_checkbox.isChecked():
            channel.auto_scale() # Autoscale

        f = str(ui.vna_file_field.text())
        
        retrieve_data(ip, port, f, fmat, channel.executor)
    

    channel.executor.close()
    
    # Reenable buttons once measure has finished

    ui.measure_vna.setEnabled(True)
    ui.left_button.setEnabled(True)
    ui.right_button.setEnabled(True)


def write_4vectors(lvectors, fname):

    def ctos(cmx):
        if cmx.imag == 0: # float comparison. This might be bad
            return str(cmx.real) # Avoid writing 0j
        else:
            # write complex to number to a string
            return str(cmx.real) + "+" + str(cmx.imag) + "j"

    with open("{fname}.csv".format(fname=fname), "w+") as f:
        for idx, d in enumerate(lvectors[0]):
            f.write(ctos(lvectors[0][idx])+","+ctos(lvectors[1][idx])+","+ctos(lvectors[2][idx])+","+ctos(lvectors[3][idx])+"\r\n")

def write_2vectors(lvectors, fname):

    def ctos(cmx):
        if cmx.imag == 0: # float comparison. This might be bad
            return str(cmx.real) # Avoid writing 0j
        else:
            # write complex to number to a string
            return str(cmx.real) + "+" + str(cmx.imag) + "j"

    with open("{fname}.csv".format(fname=fname), "w+") as f:
        for idx, d in enumerate(lvectors[0]):
            f.write(ctos(lvectors[0][idx])+","+ctos(lvectors[1][idx])+"\r\n")

def write_vector(vector, fname)
    with open(fname + "_freqdata.csv", "w+") as f:
        for line in vector:
            f.write(str(line)+"\r\n")


def retrieve_data_single(ip, port, fname):
    executor = SocketExecutor(ip, port, expect_reply=False, endline="\n")
    executor.execute_command(":FORM:DATA ASC") # Set data to ASCII

    data = executor.ask(":CALC1:DATA:FDAT?")
    data = data.split(",")
    data = [float(i) for i in data]
    write_vector(data, fname + "_freqdata.csv")

    freq_data = executor.ask(":SENS1:FREQ:DATA?")
    freq_data = freq_data.split(",")
    freq_data = [float(i) for i in freq_data]
    write_vector(freq_data, fname + "_freqdata.csv")

    executor.close()

def retrieve_data(ip, port, fname, fmat, executor):
    executor.execute_command(":FORM:DATA ASC") # Set data to ASCII

    data = executor.ask(":CALC1:DATA:FDAT?")

    data = data.split(",")
    # Dealing with complex values, convert pairs into complex numbers
    data = [complex(float(pair[0]), float(pair[1])) for pair in chunker(data, 2)] 

    sdata.append(data)

    if len(sdata) == 4: # Everything measured
        
        write_4vectors(sdata, fname+"_vna_s") 
        write_4vectors(z_from_s(sdata), fname+"_vna_z")
        write_4vectors(y_from_s(sdata), fname+"_vna_y") 
        freq_data = executor.ask(":SENS1:FREQ:DATA?")
        freq_data = freq_data.split(",")
        freq_data = [float(i) for i in freq_data]
        write_2vectors([cga_from_s(freq_data, sdata),cgs_from_s(freq_data, sdata)], fname+"_cap")
        with open(fname + "_freqdata.csv", "w+") as f:
            for line in freq_data:
                f.write(str(line)+"\r\n")


