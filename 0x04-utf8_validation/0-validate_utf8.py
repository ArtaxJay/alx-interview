#!/usr/bin/python3
"""Python Interview Challenge: UTF-8 Validation"""


def validUTF8(data):
    """
    This func determines if a given data set repres a valid UTF-8 encoding
    Args:
        data: a list of ints
    Return:
        True if data is a valid UTF-8 encoding
        return False otherwise
    """
    byte_counter = 0

    for index in data:
        if byte_counter == 0:
            if index >> 5 == 0b110 or index >> 5 == 0b1110:
                byte_counter = 1
            elif index >> 4 == 0b1110:
                byte_counter = 2
            elif index >> 3 == 0b11110:
                byte_counter = 3
            elif index >> 7 == 0b1:
                return False
        else:
            if index >> 6 != 0b10:
                return False
            byte_counter -= 1
    return byte_counter == 0
