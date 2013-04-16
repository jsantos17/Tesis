from util.SourceMode import SourceMode

class SMUBase(object):

    def __init__(self, voltage_name, current_name, ch_number, source_mode=SourceMode.VOLTAGE):
        
        if source_mode not in [SourceMode.VOLTAGE, SourceMode.CURRENT, SourceMode.COMMON]:
            raise SMUConfigError("Source mode must be defined from SourceMode enum")
        
        if len(voltage_name) > 6:
            raise SMUConfigError("Voltage name too long")
        
        if len(current_name) > 6:
            raise SMUConfigError("Current name too long")

        if ch_number > 8:
            raise SMUConfigError("Channel number too high")
        
        self.ch_number = ch_number
        self.current_name = current_name
        self.voltage_name = voltage_name
        self.source_mode = source_mode

    # In base class as we need to always set up a channel


class SMUConfigError(Exception):
    pass 
