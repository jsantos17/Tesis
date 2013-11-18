import unittest
from lib.SMUSweep import SMUSweep
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SweepType import SweepType

class TestSweep(unittest.TestCase):

    def test_example(self):
        chan_command = "DE CH1 'V1','I1',1,1"
        func_command = "SS VR1,1,5,1,0.01"

        sweep_smu = SMUSweep("V1", "I1",  SourceMode.VOLTAGE, 1, SourceType.VOLTAGE, 1, 5, 1, 0.01, SweepType.LINEAR)

        self.assertEqual(chan_command, sweep_smu._get_chan_cmd())
        self.assertEqual(func_command, sweep_smu._get_var1_cmd())

