import re
from itertools import groupby

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def val_rep(num):
    """ If it has 4 or more consecutive repeated digits, return False, If not, then return True.
    """
    res = "".join(num.split("-"))
    for i in range(len(res)):
        try:
            if (res[i] == res[i+1]):
                if (res[i+1] == res[i+2]):
                    if (res[i+2] == res[i+3]):
                        return False
        except IndexError:
           pass
    return True

def is_valid_card_number(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    """

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

#    for group in match.groups:
#        if group[0] * 4 == group:
#            return False
    else:
        return True


with open ("data.txt", "r") as fileHandler:
    # Read each line in loop
    for line in fileHandler:
        # As each line (except last one) will contain new line character, so strip that
#        is_valid = is_valid_card_number(line)
#        if is_valid:
        if val_rep(line) and is_valid_card_number(line):
            print("Valid")
        else:
            print("Invalid")


