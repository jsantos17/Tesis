import unittest
from lib.SMUSweep import SMUSweep
from lib.SMU import SMUConfigError
from lib.SMUList import SMUList
from lib.SMUStep import SMUStep
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SweepType import SweepType
from lib.util.SlaveMaster import SlaveMaster
from lib.util.CurrentVoltage import CurrentVoltage 
from lib.util.funcs import random_id

class TestSweep(unittest.TestCase):
   

    def test_linear_sweep(self):
        chan_command = "DE CH1 '{voltage_name}','{current_name}',1,1"
        func_command = "SS VR1,1,5,1,0.01"
        voltage_name = random_id(CurrentVoltage.VOLTAGE) 
        current_name = random_id(CurrentVoltage.CURRENT)
        chan_command = chan_command.format(voltage_name = voltage_name, 
                current_name = current_name)
        sweep_smu = SMUSweep(1, SourceMode.VOLTAGE, SourceType.VOLTAGE, 1, 5, 1, 0.01, SweepType.LINEAR, voltage_name,
                             current_name)

        self.assertEqual(chan_command, sweep_smu._get_chan_cmd())
        self.assertEqual(func_command, sweep_smu._get_var1_cmd())

    def test_list_sweep(self):
        chan_command = "DE CH2 '{voltage_name}','{current_name}',1,1"
        func_command = "SS VL2,1,0.01,1,5,2,1,3,2,3,4,2"
        voltage_name = random_id(CurrentVoltage.VOLTAGE) 
        current_name = random_id(CurrentVoltage.CURRENT)
        chan_command = chan_command.format(voltage_name = voltage_name, 
                current_name = current_name)

        sweep_values = [1,5,2,1,3,2,3,4,2] # List of values to sweep
        compliance = 0.01 # Compliance

        list_smu = SMUList(2, SourceMode.VOLTAGE, SourceType.VOLTAGE, sweep_values, compliance, SlaveMaster.MASTER,
                           voltage_name, current_name)
        self.assertEqual(chan_command, list_smu._get_chan_cmd())
        self.assertEqual(func_command, list_smu._get_sweep_cmd())

    def test_step_sweep(self):
        chan_command = "DE CH{ch_number},'{volt_name}','{curr_name}',2,2"
        func_command = "SS IP {start},{step},{steps},{compliance}"

        ch_number = 3
        curr_name = random_id(CurrentVoltage.CURRENT)
        volt_name = random_id(CurrentVoltage.VOLTAGE)
        start = 0.01
        step = 0.02
        steps = 15
        compliance = 0.01

        chan_command = chan_command.format(ch_number=ch_number, curr_name=curr_name, volt_name=volt_name)
        func_command = func_command.format(ch_number=ch_number, start=start, step=step, steps=steps, compliance=compliance)

        step_smu = SMUStep(ch_number, SourceMode.CURRENT, SourceType.CURRENT, start, step, steps, compliance, volt_name,
                           curr_name)
        
        self.assertEqual(chan_command, step_smu._get_chan_cmd())
        self.assertEqual(func_command, step_smu._get_var2_cmd())

    def test_validation(self):
#       Validation should fail with SMUConfigError
        with self.assertRaises(SMUConfigError):
            sweep_smu = SMUSweep(1, SourceMode.VOLTAGE, SourceType.VOLTAGE, 1, 5000, 1, 0.01, SweepType.LINEAR, "V1",
                                 "I1")

        with self.assertRaises(SMUConfigError):
            step_smu = SMUStep(1, SourceMode.CURRENT, SourceType.CURRENT, 0.01, 0.05, 0.4, 1000, "V4", "I4")

        with self.assertRaises(SMUConfigError):
            list_smu = SMUList(2, SourceMode.VOLTAGE, SourceType.VOLTAGE, [1000, 1000, 1000], -100, SlaveMaster.MASTER,
                               "V1", "I1")
