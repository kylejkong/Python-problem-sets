#version 1
# try:
#     x = int(input("What's x?"))

# # try input except valueerror if there is nothing else to handle print f x is {x}

# except ValueError:

    
#     print("x is not an integer")


# else:
#     print(f"x is {x}")



# version 2
#loop to reprompt user to provide an int to input

# while True:
#     try:
#         x = int(input("What's x?"))
        
#     # try input except valueerror if there is nothing else to handle print f x is {x}

#     except ValueError:

#         print("x is not an integer")

#     else:
#         break
          

# print(f"x is {x}")


# # version 3
# #loop to reprompt user to provide an int to input
# def main():
#     x = get_in()
#     print(f"x is {x}")


# def get_in():
#     while True:
#         try:
#             x = int(input("What's x?"))
#             # return x can be placed here instead of in else statement
#         # try input except valueerror if there is nothing else to handle print f x is {x}

#         except ValueError:

#             # print("x is not an integer")
#             pass
#         else:
#             return x
            

    
# main()

# version 4
#loop to reprompt user to provide an int to input
def main():
    x = get_in("What's x?")
    print(f"x is {x}")


def get_in(prompt):
    while True:
        try:
            return int(input(prompt))
            # return x can be placed here instead of in else statement
            # try input except valueerror if there is nothing else to handle print f x is {x}

        except ValueError:

            # print("x is not an integer")
            pass
        
main()