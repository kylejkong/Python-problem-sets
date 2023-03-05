import string

def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #check if the first two characters from position 0 are not letters
    if s[0:2].isalpha()==False:
        return False

    #check if punutuation exists in s string input
    for i in s:
        if i in string.punctuation:
            return False

    #check in length of s string for zero using while loop.
    z = 1
    while z < len(s):
        #when the 1st value in string found isnt a letter and it is a zero return False
        # and the break the loop
        if s[z].isalpha()==False:
            if s[z] == "0":
                return False
            break


        z = z + 1

    #check if last position and 3rd last position are numbers ,
    # if yes that makes2nd last postion must be a letter
    if s[-1].isnumeric() and s[-3].isnumeric():

        return False

    #check if there are more than 6 characters and less than 2 characters
    if 6< len(s) or len(s)<2:
        return False
    else:
        return True






if __name__ == "__main__":
    main()