# def main():
#     fuel()


# def fuel():
#     while True:

#         try:
#             fuel = input("Fractions: ").strip()
#             x, y = fuel.split("/")
#             x = int(x)
#             y = int(y)
#             e = (x/y)*100
#             # if y > x:
#             #     z = round(x / y*100)
#             #     print (f"{z}%")
#             if x > y:
#                 continue

#             elif x == y or e >= 99:
#                 print("F")

#             elif x == 0 or e <= 1:
#                 print("E")
#             elif y > x and x!=0:
#                 print(f"{x / y*100:.0f}%")

#         except(ValueError, ZeroDivisionError):
#             pass

#         else:
#             break

# main()




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

            continue



def gauge(percentage):

    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return str(percentage) + "%"




if __name__ == "__main__":
    main()