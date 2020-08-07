#  Name: Group 13 (Dylan Bergschneider, Alex Taylor, Andrew Clos)
#  Assignment: Group Project Step 2
#  Due Date: 8/10/2020
#  Description: task.py implements each of the three functions as outlined in
#               in the project description.
##############################################################################
import math


# this function checks to see if the number is a hex string
# if it is hex, the alpha characters are converted.
def isHex(chkArr, flagChk):
    # check to see if leading characters are '0x'
    if(len(chkArr) > 1 and chkArr[0] == 48 and
            (chkArr[1] == 120 or chkArr[1] == 88)):
        # remove the 0 and x
        del chkArr[:2]
        flagChk[0] = 16  # set base flag to 16
        # convert alpha characters
        for x in range(0, len(chkArr)):
            # lower case alpha conversion
            if(chkArr[x] >= 97 and chkArr[x] <= 102):
                chkArr[x] -= 39
            # upper case alpha conversion
            elif(chkArr[x] >= 65 and chkArr[x] <= 70):
                chkArr[x] -= 7


# this function checks for valid characters
def isValid(chkArr, flagChk, decChk):
    # check for mutliple decimals
    if(decChk > 1):
        return False
    # check if negative
    if(chkArr[0] == 45):
        flagChk[1] = 1
        del chkArr[:1]

    isHex(chkArr, flagChk)

    # look for invalid characters
    for x in range(0, len(chkArr)):
        # validate the hex range
        if(flagChk[0] == 16 and (chkArr[x] <= 45 or chkArr[x] >= 64)):
            return False
        # validate the decimale range
        elif(flagChk[0] == 10 and (chkArr[x] <= 44 or chkArr[x] >= 58)):
            return False
        # check for negative anywhere else
        if(x > 0 and chkArr[x] == 45):
            return False
        # locate decimal
        if(chkArr[x] == 46):
            flagChk.append(x)
    return True


def conv_num(num_str):
    # convert num_str to list of ASCII characters
    asc_arr = []
    has_dec = 0
    act_num = 0
    flags = []
    flags.append(10)  # base 10
    flags.append(0)  # is negative

    for asc_char in num_str:
        asc_arr.append(ord(asc_char))
        # check to see if charcter is a decimal
        if(ord(asc_char) == 46):
            has_dec += 1

    if(isValid(asc_arr, flags, has_dec)):
        # assemble a number from the array of characters
        for x in range(0, len(asc_arr)):
            # if string contains a decimal, handle a float
            if(has_dec):
                # if decimal occurrs at the end, perform some float math since
                # we can't just cast to float()
                if((flags[2] + 1) == len(asc_arr)):
                    act_num /= 9.9999999999999999999999999999
                    act_num *= 9.9999999999999999999999999999

                # digits occurring after decimal
                if(x > flags[2]):
                    act_num += (1 / (flags[0] ** (
                        x - flags[2]))) * (asc_arr[x] - 48)
                # digits occurring before decimal
                elif(x < flags[2]):
                    act_num += flags[0] ** (
                        flags[2] - x - 1) * (asc_arr[x] - 48)
            else:
                act_num += flags[0] ** (
                    len(asc_arr) - x - 1) * (asc_arr[x] - 48)
        # check for negative
        if(flags[1] == 1):
            act_num *= -1
    else:
        act_num = None

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
