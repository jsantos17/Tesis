from util.SourceMode import SourceMode
from util.CurrentVoltage import CurrentVoltage

# Abstract class that should NEVER be used by itself
# Class hierarchy needs work to increase code re-use

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

    def _validate_voltage(self, voltage):
        if abs(voltage) > 210:
            raise SMUConfigError("Voltage must be above -210V and below 210V")

    def _validate_current(self, current):
        if abs(current) > 0.105:
            raise SMUConfigError("Current must be above -0.105A and below 0.105A")

    def _validate_list(self, to_validate, current_or_voltage = CurrentVoltage.CURRENT):
        if current_or_voltage == CurrentVoltage.CURRENT:
            for current in to_validate:
                self._validate_current(current)
        elif current_or_voltage == CurrentVoltage.VOLTAGE:
            for voltage in to_validate:
                self._validate_voltage(voltage)


class SMUConfigError(Exception):
    pass 
