#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
 a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer

"""


def validUTF8(data):
    """
    utf-8 rules:
    1 byte:  0xxxxxxx (7 bits)
    2 bytes: 110xxxxx 10xxxxxx (11 bits)
    3 bytes: 1110xxxx 10xxxxxx 10xxxxxx (16 bits)
    4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx (21 bits)
    """
    valid = []
    for i in data:
        if 0 in valid:  # Check for any invalid to avoid going further the list
            return False

        if i >> 7 == 0b0:
            valid.append(1)  # 1 means this is valid
        elif (i >> 13 == 0b110) and (i >> 6) & 2 == 0b10:
            valid.append(1)
        elif i >> 20 == 0b1110 and (i >> 14) & 2 == 0b10 \
                and (i >> 6) & 2 == 0b10:
            valid.append(1)
        elif i >> 27 == 0b11110 and (i >> 22) & 2 == 0b10 \
                and (i >> 14) & 2 == 0b10 and (i >> 6) & 2 == 0b10:
            valid.append(1)
        else:
            valid.append(0)  # 0 means invalid
    return all(valid)  # all returns true if all items in a list is true or 1


if __name__ == "__main__":

    data = [65]
    print(validUTF8(data))
    5
    data = [80, 121, 116, 104, 111, 110, 32, 105, 115,
            32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
