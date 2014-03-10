class CalHandler(object):

    def __init__(self, ui):
        self.ui = ui

    def connect_signals(self):
        self.ui.cal_ui.open_button.clicked.connect(self.calibrate_open)
        self.ui.cal_ui.short_button.clicked.connect(self.calibrate_short)
        self.ui.cal_ui.load_button.clicked.connect(self.calibrate_load)

    def calibrate_open(self):
        print "Calibrate open"

    def calibrate_short(self):
        print "Calibrate short"

    def calibrate_load(self):
        print "Calibrate load"
