import re

def main():
    convert()



def convert():

    month = {
    "January" : 1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }


    while True:

        try:
            date=input("Date: ").strip()

            if "/" in date:
                date = date.replace("/", " ")
                m,d,y = date.split(" ")
                m = int(m)
                d = int(d)
                y = int(y)

                if 1 <= m <= 12 or 1 <= d <= 31:
                    continue
                else:
                    print(f"{y}-{m:02}-{d:02}")

            elif "," in date:
                date = date.replace(",", "")
                m,d,y = date.split(" ")
                d = int(d)
                y = int(y)

                if 1 <= m <= 12 or m not in month:
                    continue

                else:
                    n = month[m]
                    print(f"{y}-{n:02}-{d:02}")

            else:
                continue



        except(ValueError):
            pass


        else:
            break





main()