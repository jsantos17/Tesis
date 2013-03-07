from util.SMUType import SMUType
from util.SourceMode import SourceMode

class SMU:
  def __init__(self, output, source_mode=SourceMode.VOLTAGE, smu_type=SMUType.SMU1):
    self.source_mode = source_mode
    self.smu_type = smu_type
    self.set_output(output)
    self.ranges = None
    self.channel = None
    self.compliance = None

  def set_source_mode(self, source_mode):
    self.source_mode = source_mode
    if source_mode == SourceMode.VOLTAGE:
      self._source_mode_command = "DV"
    else:
      self._source_mode_command = "DI"

  def set_channel(self, channel):
    if channel > 8:
      raise SMUConfigError
    self.channel = channel

  def set_ranges(self, ranges=0):
    self.ranges = self.ranges;

  def set_output(self, output):
    self._validate_range(output)
    self.output = output

  def set_compliance(self, compliance):
    self._validate_range(compliance)
    self.compliance = compliance

  def execute(self, connection):
    if self.channel == None or self.output == None or self.compliance == None:
      raise SMUConfigError
    print "{source_mode}{channel},{ranges},{output},{compliance}".format(
      source_mode=self.source_mode,
      channel = self.channel,
      ranges = self.ranges,
      output = self.output,
      compliance = self.compliance)

  def _validate_range(self, value):
    if self.source_mode == SourceMode.VOLTAGE and value < -210 or value > 210:
      raise SMUConfigError
    if self.source_mode == SourceMode.CURRENT:
      if self.smu_type == SMUType.SMU1 and value < -0.1050 or value > 0.1050:
        raise SMUConfigError
      elif self.smu_type == SMUType.SMU2 and value < -1.05 or value > 1.05:
        raise SMUConfigError

class SMUConfigError(Exception):
  pass
