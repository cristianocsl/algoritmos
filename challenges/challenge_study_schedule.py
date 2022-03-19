def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for register in permanence_period:
        if not isinstance(register[0], int) or not isinstance(register[1], int):
            return None
        elif register[0] <= target_time <= register[1]:
            counter += 1
    return counter
