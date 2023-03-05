import random


def main():
    lv = get_level()
    generate_integer(lv)




def get_level():


    while True:
        m = input("Level: ")
        if m not in ["1", "2", "3"]:
            continue

        return m



def generate_integer(level):
    userScore = 0

    for _ in range(10):
        attempts = 1
        if level == "1":
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == "2":
            x = random.randint(10,99)
            y = random.randint(10,99)
        elif level == "3":
            x = random.randint(100,999)
            y = random.randint(100,999)

        while True:
            try:
                print(f"{x} + {y} =" , end="")
                userInput = input()
                m = str(x + y)
                if userInput == m:
                    userScore = userScore + 1
                    break
                elif userInput != m and attempts !=3:
                    attempts = attempts + 1
                    print("EEE")
                    continue

                elif userInput != m and attempts == 3:
                    print("EEE")
                    print(f"{x} + {y} ={x + y}")
                    break

            except ValueError:
                continue



    print("Score:", userScore)










if __name__ == "__main__":
    main()