import unittest
from lib.SMUConstant import SMUConstant
from lib.SMU import SMUConfigError
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SlaveMaster import SlaveMaster

class TestConstant(unittest.TestCase):
   
    def test_constant(self):
        chan_command = "DE CH2,'V1','I1',2,3"
        func_command = "SS IC2,0.1,0.04"

        ch = 2
        volt_name = "V1"
        curr_name = "I1"
        output = 0.1
        compliance = 0.04

        constant_smu = SMUConstant(volt_name, curr_name, ch, SourceMode.CURRENT, SourceType.CURRENT, output, compliance)

        self.assertEqual(chan_command, constant_smu._get_chan_cmd())
        self.assertEqual(func_command, constant_smu._get_const_cmd())
    
    def test_constant_validation(self):
        with self.assertRaises(SMUConfigError):
            constant_smu = SMUConstant("V1", "I1", 1, SourceMode.CURRENT, SourceType.CURRENT, 100, 0.01)

