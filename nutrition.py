def main():

    nutrition()


def nutrition():


    fruits = {
        "apple" : 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100}
    

    i = input("Item: ").lower()

    if i in fruits:

       print("Calories: ", fruits[i])

main()