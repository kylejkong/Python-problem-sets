def main():
    theTime = input("What time is it?")

    n = convert(theTime)


    if 7.0 <= n <= 8.0:
        print("breakfast time")

    elif 12.0 <= n <= 13.0:
        print("lunch time")

    elif 18.0 <= n <= 19.0:
        print("dinner time")



def convert(time):

    hours, minutes = time.split(":")

    fh = float(hours)
    fm = float(minutes)

    con = fh + fm/60

    return con



    # print (hours,":", minutes)
    # print (fh + fm/60) #9:30 gives you 9.5





if __name__ == "__main__":
    main()