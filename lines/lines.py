import sys



if sys.argv[1].endswith(".py")==False:
    sys.exit("Not a Python File")

elif len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
            lines = 0
            for line in file:
                # if line with empty space removed and not starts with # AND line is not empty , add 1 to lines
                if line.lstrip().startswith('#') == False and line.isspace() == False:
                    lines = lines + 1

            print(lines)
    except FileNotFoundError:
        sys.exit('File does not exist')


elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")



