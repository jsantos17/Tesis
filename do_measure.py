from lib.SMUSweep import SMUSweep
from lib.SMUList import SMUList
from lib.SMUStep import SMUStep
from lib.util.SourceMode import SourceMode
from lib.util.SourceType import SourceType
from lib.util.SlaveMaster import SlaveMaster
from lib.util.SweepType import SweepType
from lib.VisaExecutor import VisaExecutor
from pyvisa.visa_exceptions import VisaIOError
import sys


def do_measure(ip, port):
    chan = 1
    start = 10
    stop = 100
    step = 1
    compliance = 0.005
    print ("Channel: %s" % chan)
    print "Start: %s" % start
    print "Stop: %s" % stop
    print "Step: %s" % step
    print "Compliance: %s" % compliance

    smu_sweep = SMUSweep(chan, SourceMode.VOLTAGE, SourceType.VOLTAGE, start, stop, step, compliance, SweepType.LINEAR)
    print "Commands to execute: "
    for command in smu_sweep.get_commands():
        print command
    print ip
    print port
    try:
        executor = VisaExecutor("192.168.0.5","")
        for command in smu_sweep.get_commands():
            executor.execute_command(command)
    except VisaIOError:
        print "Failed to connect"

if __name__ == "__main__":
    try:
        ip = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print "IP and port not passed"
        sys.exit(0)

    do_measure(sys.argv[1], sys.argv[2])
