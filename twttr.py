def main():
    twttr()


def twttr():
    userInput = input("Input: ")
    userOutput = ""
    vowels = ["a", "e", "i","o","u"]

    for i in range(len(userInput)):
        if userInput[i].lower() not in vowels:
            userOutput = userOutput + userInput[i]
    
    print(f"Output: {userOutput}")

main()