##############################################################################
#  Name: Group 13 (Dylan Bergschneider, Alex Taylor, Andrew Clos)
#  Assignment: Group Project Step 2
#  Due Date: 8/10/2020
#  Description: task.py implements each of the three functions as outlined in
#               in the project description.
##############################################################################

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
    endian_string = ''
    return endian_string
