from lib.VnaChannel import VnaChannel
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import SParameters

def do_measure():
    channel = VnaChannel("","", 1)
    channel.reset()
    channel.set_sweep_type(SweepType.LINEAR)
    channel.set_center_span(1E9, 5E6)
    channel.set_points(21)
    channel.set_traces(2)
    channel.set_sparam_for_chan(SParameters.S11)
    channel.activate_trace(1)

if __name__ == "__main__":
    do_measure()
