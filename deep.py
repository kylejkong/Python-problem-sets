deepthought = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

match deepthought:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

# print(deepthought)