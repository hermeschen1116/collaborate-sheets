from enum import Enum


class Existence:
    """
    formate:
        Each type occupies 2 bits
            signinific bit makes function cares about it
            another bit is this type should exist
        usage (in function):
            Always use & (AND bit operator) to do mask
            if result after masked is not 0, do corresponding operation
            e.g.
                if option & CARE != 0:
                    if option & SHOULD != 0:
                        # detect [option exist]
                    else:
                        # detect [option don't exist]
    usage (calling function):
    Use TRUE or FALSE as args
    e.g. checkExist(TRUE) if you wish this option exists
    """
    CARE   = 0
    TRUE   = 0
    FALSE  = 0
    SHOULD = 0


class USER(Existence):
    CARE   = 0b10
    TRUE   = 0b11
    FALSE  = 0b10
    SHOULD = 0b01


class SHEET(Existence):
    CARE   = 0b10 * 4
    TRUE   = 0b11 * 4
    FALSE  = 0b10 * 4
    SHOULD = 0b01 * 4

# not used
class ACCESS(Existence):
    CARE   = 0b10 * 16
    TRUE   = 0b11 * 16
    FALSE  = 0b10 * 16
    SHOULD = 0b01 * 16
