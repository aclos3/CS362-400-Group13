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
    actual_num = 0
    
    for asc_char in num_str:
        asc_arr.append(ord(asc_char))
        # check to see if charcter is a decimal
        if(ord(asc_char) == 46):
            has_dec += 1

    #print(asc_arr[0])
    #print(asc_arr[1])
    #print(asc_arr[2])
    # assemble a number from the array of characters
    for x in range(0, len(asc_arr)):
        multiplier = len(asc_arr) - x - 1
        # check to see if decimal is present, set flag
        if(asc_arr[x] == 46):
            aft_dec = x + 1
        
        # digits occurring after decimal
        elif(aft_dec):
            actual_num += (1 / (10 ** (x - aft_dec + 1)))  * (asc_arr[x] - 48)
            #print("adding: " + str((1 / (10 ** (x - aft_dec + 1)))  * (asc_arr[x] - 48)))
        # digits occurring before decimal
        else:
            actual_num += 10 ** (multiplier - (has_dec * 2)) * (asc_arr[x] - 48)

    
    return actual_num


def my_datetime(num_sec):
    date_string = ''
    return date_string


def conv_endian(num, endian='big'):
    endian_string = ''
    return endian_string
