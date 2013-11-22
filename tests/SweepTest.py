import unittest
from lib.SMUSweep import SMUSweep
from lib.SMUList import SMUList
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SweepType import SweepType
from lib.util.SlaveMaster import SlaveMaster

class TestSweep(unittest.TestCase):
   

    def test_linear_sweep(self):
        chan_command = "DE CH1 'V1','I1',1,1"
        func_command = "SS VR1,1,5,1,0.01"

        sweep_smu = SMUSweep("V1", "I1",  SourceMode.VOLTAGE, 1, SourceType.VOLTAGE, 1, 5, 1, 0.01, SweepType.LINEAR)

        self.assertEqual(chan_command, sweep_smu._get_chan_cmd())
        self.assertEqual(func_command, sweep_smu._get_var1_cmd())

    def test_list_sweep(self):
        chan_command = "DE CH2 'V1','I1',1,1"
        func_command = "SS VL2,1,0.01,1,5,2"

        sweep_values = [1,5,2] # List of values to sweep
        compliance = 0.01 # Compliance

        list_smu = SMUList("V1", "I1", SourceMode.VOLTAGE, 2, SourceType.VOLTAGE, sweep_values, compliance, SlaveMaster.MASTER)
        self.assertEqual(chan_command, list_smu._get_chan_cmd())
        self.assertEqual(func_command, list_smu._get_sweep_cmd())
