#  Name: Group 13 (Dylan Bergschneider, Alex Taylor, Andrew Clos)
#  Assignment: Group Project Step 2
#  Due Date: 8/10/2020
#  Description: task.py implements each of the three functions as outlined in
#               in the project description.
##############################################################################
import math


def conv_num(num_str):
    # convert num_str to list of ASCII characters
    asc_arr = []
    has_dec = 0
    aft_dec = 0
    act_num = 0

    for asc_char in num_str:
        asc_arr.append(ord(asc_char))
        # check to see if charcter is a decimal
        if(ord(asc_char) == 46):
            has_dec += 1

    # return None if number has more than 1 decimal
    if(has_dec > 1):
        return None
    # assemble a number from the array of characters
    for x in range(0, len(asc_arr)):

        # if string contains a decimal, handle a float
        if(has_dec):

            # check to see if current character is a decimal
            if(asc_arr[x] == 46):
                # flag the location of the decimal
                aft_dec = x + 1
                # perform some float math since we can't just cast to float()
                if(aft_dec == len(asc_arr)):
                    act_num /= 9.9
                    act_num *= 9.9
            # digits occurring after decimal
            elif(aft_dec):
                act_num += (1 / (10 ** (x - aft_dec + 1))) * (asc_arr[x] - 48)

            # digits occurring before decimal
            else:
                act_num += 10 ** (len(asc_arr) - x - 3) * (asc_arr[x] - 48)

            # trailing decimal multiplier correction
            if(aft_dec == len(asc_arr)):
                act_num *= 10
        else:
            act_num += 10 ** (len(asc_arr) - x - 1) * (asc_arr[x] - 48)

    return act_num


def my_datetime(num_sec):
    date_string = ''
    return date_string


def conv_endian(num, endian='big'):
    if endian != 'big' and endian != 'little':
        return None

    digits = {}
    endian_string = ''
    if num < 0:
        endian_string = '-'

    remaining = num
    while remaining > 0:
        digit = remaining
        power = 0
        while digit >= 16:
            power += 1
            digit = remaining / (16 ** power)

        digit = math.floor(digit)
        digits[power] = convert_hex(digit)
        remaining = remaining - (16 ** power) * digit

    endian_string += string_from_digits_map(digits, endian == 'big')
    return endian_string


def string_from_digits_map(digits, big_endian):
    """converts map of hex digits to string
    keys should represent digit place (i.e. 16 to what power)
    values should be hex digits (0-9, A-F)
    big_endian is boolean, converts to little-endian if false
    """
    # find most significant digit
    most_sig_digit = 0
    for x in digits:
        if x > most_sig_digit:
            most_sig_digit = x

    # leading 0 when needed
    if most_sig_digit % 2 == 0:
        most_sig_digit += 1
        digits[most_sig_digit] = '0'

    # inner missing 0s
    for y in range(0, most_sig_digit + 1,):
        if y not in digits:
            digits[y] = '0'

    # convert to pairs
    byte_chars = []
    for x in range(most_sig_digit, 0, -2):
        byte_chars.append(digits[x] + digits[x - 1])

    # TODO order based on endianness
    spaced_string = ''
    for x in byte_chars:
        spaced_string += x + ' '

    # remove trailing space
    spaced_string = spaced_string[:-1]

    return spaced_string


def convert_hex(num):
    """converts base 10 number to hex string
    for just one hex digit (0-9, A-F)
    """
    if 0 <= num <= 9:
        return str(num)
    elif 10 <= num <= 15:
        numerics = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        return numerics[num]
    else:
        return None
