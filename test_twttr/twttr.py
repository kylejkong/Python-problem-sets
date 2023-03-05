def main():

    userInput = input("Input: ")

    print(shorten(userInput))


def shorten(n):

    userOutput = ""


    for i in range(len(n)):
        if n[i].lower() not in ["a","e","i","o","u"]:
            userOutput = userOutput + n[i]

    return userOutput



if __name__ == "__main__":
    main()