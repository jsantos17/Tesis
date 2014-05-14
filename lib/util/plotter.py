import matplotlib.pyplot as plt

def plot(x, y, fname):
    plt.plot(x, y)
    plt.xlabel(u"Polarización")
    plt.ylabel(u"Capacitancia")
    plt.savefig(fname + '.png', bbox_inches='tight')
