import unittest
from lib.SMUConstant import SMUConstant
from lib.SMU import SMUConfigError
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SlaveMaster import SlaveMaster
from lib.util.CurrentVoltage import CurrentVoltage 
from lib.util.funcs import random_id

class TestConstant(unittest.TestCase):
   
    def test_constant(self):
        chan_command = "DE CH2,'{voltage_name}','{current_name}',2,3"
        func_command = "SS IC2,0.1,0.04"

        current_name = random_id(CurrentVoltage.CURRENT)
        voltage_name = random_id(CurrentVoltage.VOLTAGE)

        chan_command = chan_command.format(voltage_name = voltage_name,
                current_name = current_name)

        ch = 2
        output = 0.1
        compliance = 0.04

        constant_smu = SMUConstant(ch, SourceMode.CURRENT, SourceType.CURRENT, output, compliance, voltage_name,
                                   current_name)

        self.assertEqual(chan_command, constant_smu._get_chan_cmd())
        self.assertEqual(func_command, constant_smu._get_const_cmd())
    
    def test_constant_validation(self):
        with self.assertRaises(SMUConfigError):
            constant_smu = SMUConstant(1, SourceMode.CURRENT, SourceType.CURRENT, 100, 0.01, "V1", "I1")

