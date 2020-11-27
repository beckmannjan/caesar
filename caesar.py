import argparse
import string

def caesar(text, shiftRight):
    processed_string = ""

    # shiftRight is only None when -a is specified, so we do all combos
    if shiftRight == None:
        for r in range(25):
            processed_string += "\n"
            for c in range(len(text)):
                processed_string +=shiftChar(text[c], r + 1)
    else:
        for c in range(len(text)):
            processed_string += shiftChar(text[c], shiftRight)
    
    return processed_string

# This functions uses the values of the Characters to shift them n times
def shiftChar(char, shift_right):
    if shift_right > 26 or shift_right < -26:
        raise Exception("Why shift more than 26 times?")

    if len(char) > 1:
        raise Exception("Cannot shift more than one character")

    if not(char in string.ascii_letters 
        or char in string.punctuation 
        or char == " "):
        raise Exception("Only use non-special letters and punctation")


    # Check if character is a letter, if not skip shifting
    if char.isalpha() == False:
        return char

    lower_limit = None
    upper_limit = None
    val_shifted_char = None
    val_char = ord(char)

    # Set the boundaries for lower-/uppercase letters
    if(char.isupper()):
        lower_limit = ord("A")
        upper_limit = ord("Z")
    elif(char.islower()):
        lower_limit = ord("a")
        upper_limit = ord("z")
    

    # Do the shifting (and wrapping around, if necessary)
    if val_char + shift_right < lower_limit:
        shift_upper_left = val_char + shift_right - lower_limit
        val_shifted_char = upper_limit + shift_upper_left + 1
    elif val_char + shift_right > upper_limit:
        shift_lower_right = val_char + shift_right - upper_limit
        val_shifted_char = lower_limit + shift_lower_right - 1
    else:
        val_shifted_char = val_char + shift_right

    return chr(val_shifted_char)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap._optionals.description = "Simple program for the Caesar cipher.\n\
        To decrypt you can use the -a option to print out all possibilities."
    # Add the arguments to the parser
    ap.add_argument("-s", "--string", 
                    required=True, 
                    help="String to be encrypted")
    ap.add_argument("-n", "--nrightshift",
                    required=False, 
                    type=int, 
                    help="Number of times to shift right. \
                        Use negative numbers for leftshift")
    ap.add_argument("-a", "--all",
                    required=False, 
                    action='store_true',  
                    help="Print all possibilities")

    args = vars(ap.parse_args())

    if not(bool(args["nrightshift"]) ^ bool(args["all"])):
        raise Exception("Please use either -n or -a")

    text = args["string"]
    n = args["nrightshift"]

    print(caesar(text, n))