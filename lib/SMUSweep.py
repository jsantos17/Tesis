from SMU import SMUBase
from util.SweepType import SweepType
from util.SourceType import SourceType

class SMUSweep(SMUBase):
    # Source mode is for channel definition, Source type for VAR1 definition
    def __init__(self, voltage_name, current_name, source_mode, ch_number, source_type, start, stop, step, compliance, sweep_type=SweepType.LINEAR):
        super(SMUSweep, self).__init__(voltage_name, current_name, source_mode, ch_number)
        
        if source_type not in [SourceType.VOLTAGE, SourceType.CURRENT]:
            raise SMUSweepConfigError("source_type must be defined from SourceType enum")

        if sweep_type not in [SweepType.LINEAR, SweepType.LOG10, SweepType.LOG25, SweepType.LOG50]:
            raise SMUSweepConfigError("sweep_type must be defined from SweepType enum")

        self.source_type = source_type
        
        if self.source_type == SourceType.VOLTAGE:
            if start < -210 or stop < -210 or step < -210 or compliance < -210:
                raise SMUSweepConfigError("Voltage must be above -210V")
            if start > 210 or stop > 210 or step > 210 or compliance > 210:
                raise SMUSweepConfigError("Voltage must be below 210V")

        if self.source_type == SourceType.CURRENT:
            if start < -0.105 or stop < -0.105 or step < -0.105 or compliance < -0.105:
                raise SMUSweepConfigError("Current must be above -0.105A")
            if start > 0.105 or stop > 0.105 or step > 0.105 or compliance > 0.105:
                raise SMUSweepConfigError("Voltage must be below 0.105A")
        
        # Validation passed! Create the object

        self.start = start
        self.stop = stop
        self.step = step
        self.compliance = compliance
        self.sweep_type = sweep_type


    def _get_chan_cmd(self):
        command = "CH{ch_number},'{voltage_name}','{current_name}',{source_mode},1".format(ch_number=self.ch_number,
                            voltage_name=self.voltage_name, current_name=self.current_name, source_mode=self.source_mode)
        return command

    def _get_var1_cmd(self):
        if self.source_type == SourceType.VOLTAGE:
            template = "VR{sweep_type},{start},{stop},{step},{compliance}"
        elif self.source_type == SourceType.CURRENT:
            template = "IR{sweep_type},{start},{stop},{step},{compliance}"

        command = template.format(sweep_type=self.sweep_type, start=self.start, stop=self.stop, 
                                 step=self.step, compliance=self.compliance)
        return command

    def get_commands(self):

        return [self._get_chan_cmd(), self._get_var1_cmd()]


class SMUSweepConfigError(Exception):
    pass