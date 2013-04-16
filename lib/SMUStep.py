from SMU import SMUBase
from util.SourceType import SourceType

class SMUStep(SMUBase):
    # Source mode is for channel definition, Source type for VAR2 definition
    def __init__(self, voltage_name, current_name, source_mode, ch_number, source_type, start, step, steps, compliance):
        super(SMUStep, self).__init__(voltage_name, current_name, ch_number, source_mode)
        
        if source_type not in [SourceType.VOLTAGE, SourceType.CURRENT]:
            raise SMUStepConfigError("source_type must be defined from SourceType enum")

        self.source_type = source_type
        
        # TODO move validation to superclass
         
        if self.source_type == SourceType.VOLTAGE:
            if start < -210  or step < -210 or compliance < -210:
                raise SMUStepConfigError("Voltage must be above -210V")
            if start > 210 or  step > 210 or compliance > 210:
                raise SMUStepConfigError("Voltage must be below 210V")

        if self.source_type == SourceType.CURRENT:
            if start < -0.105  or step < -0.105 or compliance < -0.105:
                raise SMUStepConfigError("Current must be above -0.105A")
            if start > 0.105  or step > 0.105 or compliance > 0.105:
                raise SMUStepConfigError("Current must be below 0.105A")

        if steps > 32:
            raise SMUStepConfigError("The max number of steps is 32")


        # Validation passed! Create the object

        self.start = start
        self.steps = steps
        self.step = step
        self.compliance = compliance


    def _get_var2_cmd(self):
        if self.source_type == SourceType.VOLTAGE:
            template = "VP{start},{step},{steps},{compliance}"
        elif self.source_type == SourceType.CURRENT:
            template = "IP{start},{step},{steps},{compliance}"

        command = template.format(start=self.start, step=self.step, steps=self.steps, 
                                 compliance=self.compliance)
        return command

    def _get_chan_cmd(self):
        command = "CH{ch_number},'{voltage_name}','{current_name}',{source_mode},2".format(ch_number=self.ch_number,
                                        voltage_name=self.voltage_name, current_name=self.current_name, source_mode=self.source_mode)
        return command

    def get_commands(self):
        return [self._get_chan_cmd(), self._get_var2_cmd()]


class SMUStepConfigError(Exception):
    pass
