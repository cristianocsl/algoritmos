def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for register in permanence_period:
        if (register[0] and register[1]) is None or isinstance(
            register[0] or register[1], str
        ):
            return None
        if register[0] <= target_time <= register[1]:
            counter += 1
    return counter
