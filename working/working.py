import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d+):?(\d+)? ([A-P]M) to (\d+):?(\d+)? ([A-P]M)$", s, re.IGNORECASE)

    if matches:
        if matches.group(2):
            if int(matches.group(2)) >= 60:
                raise ValueError
        if  matches.group(5):
            if int(matches.group(5)) >= 60:
                raise ValueError
        if matches.group(1):
            if 0 >= int(matches.group(1)) or int(matches.group(1)) >= 13:
                raise ValueError
        if matches.group(4):
            if 0 >= int(matches.group(4)) or int(matches.group(4)) >= 13 :
                raise ValueError



        ##### Time 1 #####
        h1  = int(matches.group(1))
        if matches.group(3).upper() == 'AM' and matches.group(1) == '12':

            h1 = h1 - 12

        elif matches.group(3).upper() == 'PM' and matches.group(1) != '12':

            h1 = h1 + 12

        elif matches.group(3).upper() == 'PM' and matches.group(1) == '12':

            h1 = h1


        if matches.group(2) == None:
            t1 = f"{h1:02}:00"
        else:
            t1 = f"{h1:02}:{matches.group(2)}"



        ##### Time 2 #####
        h2  = int(matches.group(4))
        if matches.group(6).upper() == 'AM' and matches.group(4) == '12':
            h2 = h2 - 12

        elif matches.group(6).upper() == 'PM' and matches.group(4) != '12':

            h2 = h2 + 12

        elif matches.group(6).upper() == 'PM' and matches.group(4) == '12':

            h2 = h2


        if matches.group(5) == None:
            t2 = f"{h2:02}:00"
        else:
            t2 = f"{h2:02}:{matches.group(5)}"








    else:
        raise ValueError

    return t1+" "+"to"+" "+t2



if __name__ == "__main__":
    main()
