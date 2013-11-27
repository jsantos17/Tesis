from SMU import SMUBase
from SMU import SMUConfigError
from util.SourceType import SourceType


class SMUConstant(SMUBase):

    def __init__(self, voltage_name, current_name, ch_number, source_mode, source_type, output, compliance):
        super(SMUConstant, self).__init__(voltage_name, current_name, ch_number, source_mode)
        if source_type not in [SourceType.VOLTAGE, SourceType.CURRENT]:
            raise SMUConfigError("source_type must be defined from SourceType enum")

        self.source_type = source_type

        # TODO figure out how to move validation to superclass or at least elsewhere.

        if self.source_type == SourceType.VOLTAGE:
            self._validate_voltage(output)
            self._validate_voltage(compliance)
        if self.source_type == SourceType.CURRENT:
            self._validate_current(output)
            self._validate_voltage(compliance)

        # Create object now that validation has finished

        self.output = output
        self.compliance = compliance

    def _get_chan_cmd(self):
        command = "DE CH{ch_number},'{voltage_name}','{current_name}',{source_mode},3".format(ch_number=self.ch_number,
                          voltage_name=self.voltage_name, current_name=self.current_name, source_mode=self.source_mode)
        return command

    def _get_const_cmd(self):
        if self.source_type == SourceType.VOLTAGE:
            template = "SS VC{ch},{output},{compliance}"
        elif self.source_type == SourceType.CURRENT:
            template = "SS IC{ch},{output},{compliance}"

        return template.format(ch=self.ch_number, output=self.output, compliance=self.compliance)

    def get_commands(self):
        return [self._get_chan_cmd(), self._get_const_cmd()]
