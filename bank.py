seinfeld = input("Greetings: ").strip()

match seinfeld:
    case "What's happening?" | "What's up?":
        print("$100")
    case "How you doing?":
        print("$20")
    case _:
        print("$0")

# print(seinfeld)