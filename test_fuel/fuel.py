def main():
    userInput = input("Fractions: ").strip()
    n =convert(userInput)
    print(gauge(n))



def convert(fraction):
    while True:
        x, y = fraction.split("/")
        try:

            x = int(x)
            y = int(y)

            z = x / y

            if z <= 1:
                percentage = int(z*100)
                return percentage
            else:
                fraction = input("Fractions: ")
                pass
        except(ValueError, ZeroDivisionError):

            break






def gauge(percentage):

    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return str(percentage) + "%"




if __name__ == "__main__":
    main()