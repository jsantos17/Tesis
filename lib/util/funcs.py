from CurrentVoltage import CurrentVoltage
import random
import string

def random_id(current_voltage):
        idf = ''.join(random.choice(string.lowercase + string.uppercase + "1234567890") for i in range(4))
        if current_voltage == CurrentVoltage.VOLTAGE:
            return "V-" + idf

        if current_voltage == CurrentVoltage.CURRENT:
            return "I-" + idf
