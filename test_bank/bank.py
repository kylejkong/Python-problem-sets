def main():
    seinfeld = input("Greetings: ").strip()

    print(f"${value(seinfeld)}")



def value(n):


    if "hello" in n.lower().strip():
        return 0

    elif n[0].lower().strip() == "h":
        return 20

    else:
        return 100

    # print(seinfeld)


if __name__ == "__main__":
    main()