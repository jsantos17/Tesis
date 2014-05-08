from numpy.linalg import inv

def single_z_from_s(data):
    s11 = data[0]
    s12 = data[1]
    s21 = data[2]
    s22 = data[3]

    delta_s = (1-s11)*(1-s22) - s12*s21
    z0 = 50 # characteristing impendance of 50 ohms

    z11 = (((1+s11)*(1-s22)+s12*s21)/delta_s)*z0
    z12 = (2*s12*z0)/delta_s
    z21 = (2*s21*z0)/delta_s
    z22 = (((1-s11)*(1+s22)+s12*s21)/delta_s)*z0

    return [z11, z12, z21, z22]

def single_y_from_s(data):
    # Put data in matrix form for inversion
    matrix_s = [[data[0], data[1]], [data[2], data[3]]]
    matrix_y = inv(single_z_from_s(matrix_s)).tolist()
    # Other parts of the program expect a flat list, not a matrix
    y = [item for sublist in matrix_y for item in sublist] # list flattening magic
    return y

def y_from_s(sdata):
    ydata = []
    y11_list = []
    y12_list = []
    y21_list = []
    y22_list = []


    for idx, d in enumerate(sdata):
        s11 = sdata[idx][0]
        s12 = sdata[idx][1]
        s21 = sdata[idx][2]
        s22 = sdata[idx][3]

        Y = single_y_from_s([s11, s12, s21, s22])
        y11_list.append(Y[0])
        y12_list.append(Y[1])
        y21_list.append(Y[2])
        y22_list.append(Y[3])

    ydata = [y11_list, y12_list, y21_list, y22_list]
    return ydata

def z_from_s(sdata):
    zdata = []
    z11_list = []
    z12_list = []
    z21_list = []
    z22_list = []


    for idx, d in enumerate(sdata):
        s11 = sdata[idx][0]
        s12 = sdata[idx][1]
        s21 = sdata[idx][2]
        s22 = sdata[idx][3]

        Z = single_z_from_s([s11, s12, s21, s22])
        z11_list.append(Z[0])
        z12_list.append(Z[1])
        z21_list.append(Z[2])
        z22_list.append(Z[3])

    zdata = [z11_list, z12_list, z21_list, z22_list]
    return zdata

def cga_from_s(freq_data, sdata):
    ydata = y_from_s(sdata)
    cga = []
    for freq, ydatum in zip(freq_data, ydata):
        cga.append(ydata[0].imag/(freq_data*2*3.141592))

def cgs_from_s(freq_data, sdata):
    ydata = y_from_s(sdata)
    cgs = []
    for freq, ydatum in zip(freq_data, ydata):
        cgs.append(-ydata[1].imag/(freq_data*2*3.141592))
