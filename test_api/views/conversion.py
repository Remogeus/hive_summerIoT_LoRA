from .config_api import calibration_index, zero_offset, beta0


def temp_compensation(weight, temperature):
    """ temp_compensation(weight, temperature)

        Returns a compensated weight of the hive, according to
        https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf

        Parameters: @weight - float, uncompensated weight of the hive_name
                    @temperature - float, hive temperature aquired from sensor
        Returns:    float - compensated weight
    """
    return weight - (temperature * beta0)


def uncomp_weight(adc_readout):
    """ uncomp_weight(adc_readout)

        Returns a uncompensated weight of the hive from the readings of the ADC,
        according to https://pripoj.me/wp-content/uploads/2017/08/Payload.pdf

        Parameters: @adc_readout - int, raw uncalibrated load cell ADC readout
        Returns:    float - uncompensated weight
    """
    return (adc_readout / calibration_index) - zero_offset
