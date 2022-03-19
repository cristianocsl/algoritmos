def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for register in permanence_period:
            if register[0] <= target_time <= register[1]:
                counter += 1
        return counter
    except TypeError:
        return


# TypeError Exceptions may occur while performing
# operations between two incompatible data types. Exemplo: 'str' e 'int'
# fonte: https://www.pythonforbeginners.com/basics/
# typeerror-in-python#:~:text=What%20is%20TypeError%20in%20Python,
# object%20will%20not%20be%20compatible.
