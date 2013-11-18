from SMU import SMUBase
from util.SourceType import SourceType

def SMUConstant(SMUBase):
    def __init__(self, voltage_name, current_name, source_mode, ch_number, source_type):
        super(SMUStep, self).__init__(voltage_name, current_name, ch_number, source_mode)
        if source_type not in [SourceType.VOLTAGE, SourceType.CURRENT]:
            raise SMUStepConfigError("source_type must be defined from SourceType enum")
