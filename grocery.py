def main():
    grocery()


def grocery():
    groceryList = {}

    while True:
        try:
            item = input().upper()

            #if item not in groceryList create a groceryList and make that item 1, else add it to existing list
            if item not in groceryList:
                groceryList[item] = 1

            else:
                groceryList[item] = groceryList[item] + 1


        except EOFError:
            break

    for i in sorted(groceryList.keys()):
        print(groceryList[i], i, sep=" ")











main()