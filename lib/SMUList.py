from SMU import SMUBase
from util.SourceType import SourceType
from util.SlaveMaster import SlaveMaster

class SMUList(SMUBase):
    # Source mode is for channel definition, Source type for VAR1 definition
    def __init__(self, voltage_name, current_name, source_mode, ch_number, source_type, sweep_values, compliance, slave_master):
        super(SMUList, self).__init__(voltage_name, current_name, ch_number, source_mode)
        
        if source_type not in [SourceType.VOLTAGE, SourceType.CURRENT]:
            raise SMUSweepConfigError("source_type must be defined from SourceType enum")

        self.source_type = source_type
        
        if slave_master not in [SlaveMaster.SLAVE, SlaveMaster.MASTER]:
            raise SMUListConfigError("Slave or master mode must be specified from SlaveMaster enum")

        if self.source_type == SourceType.VOLTAGE:
            if compliance < -210 or compliance > 210:
                raise SMUListConfigError("Compliance must be between -210 and 210")
            for value in sweep_values:
                if value < -210:
                    raise SMUListConfigError("Voltages in list must be all above -210V")
                if value > 210:
                    raise SMUListConfigError("Voltages in list must all be below 210V")

        if self.source_type == SourceType.CURRENT:
            if compliance < -0.105 or compliance > 0.105:
                raise SMUListConfigError("Compliance must be between -0.105A and 0.105A")
            for value in sweep_values:
                if value < -0.105:
                    raise SMUListConfigError("Currents in list must be above -0.105A")
                if value > 0.105:
                    raise SMUListConfigError("Currents in list must be below 0.105A")
        


        # Validation passed! Create the object
        
        self.sweep_values = sweep_values
        self.compliance = compliance
        self.slave_master = slave_master

    def _get_sweep_cmd(self):
        sweep_string = ",".join(str(i) for i in self.sweep_values)
        if self.source_type == SourceType.VOLTAGE:
            template = "SS VL{ch},{slave_master},{compliance},{values}"
        elif self.source_type == SourceType.CURRENT:
            template = "SS IL{ch},{slave_master},{compliance},{values}"

        command = template.format(ch = self.ch_number, slave_master=self.slave_master, compliance=self.compliance, values=sweep_string)
        return command

    def _get_chan_cmd(self):
        command = "DE CH{ch_number} '{voltage_name}','{current_name}',{source_mode},1".format(ch_number=self.ch_number,
                                    voltage_name=self.voltage_name, current_name=self.current_name, source_mode=self.source_mode)
        return command

    def get_commands(self):
        return [self._get_chan_cmd(), self._get_sweep_cmd(), "MD ME1", "MD DO'I1'"]


class SMUListConfigError(Exception):
    pass
