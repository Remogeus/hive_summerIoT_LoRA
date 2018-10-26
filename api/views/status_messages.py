def char_status(status):
    """ char_status(status)

        Returs charging status of the device

        Parameters: @status - integer, device status aquired from sensor
        Returns:    string - charging status
    """
    possible_status = {
        0: 'invalid status',
        1: 'charged',
        2: 'charging',
        3: 'discharged'
    }
    return possible_status.get(int(status, 2) & 0x03)


def net_status(status):
    """ net_status(status)

        Returs network join status of the device

        Parameters: @status - integer, device status aquired from sensor
        Returns:    string - network join status
    """
    possible_status = {
        0: 'initialized',
        4: 'joining',
        8: 'joined',
        12: 'join failed'
    }
    return possible_status.get(int(status, 2) & 0x0c)
