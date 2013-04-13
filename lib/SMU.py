from util.SMUType import SMUType
from util.SourceMode import SourceMode

class SMUBase:

    def __init__(self, voltage_name, current_name, source_mode=SourceMode.VOLTAGE, ch_number):
        
        if source_mode not in (SourceMode.VOLTAGE, SourceMode.CURRENT, SourceMode.COMMON):
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


class SMUConfigError(Exception):
    pass 
