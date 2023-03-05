#version 1

def main():
    emojize()



# def emojize():
#     emojiDict = {
#     ':thumbsup:':'👍',
#     ':thumbs_up:':'👍',
#     ':1st_place_medal:':'🥇',
#     ':money_bag:':'💰',
#     ':smile_cat:':'😸',
#     ':candy:':'🍬'

# }

#     userInput = input("Input: ")

#     if userInput in emojiDict:

#         print("Output: ", emojiDict[userInput])




#version 2
import emoji



# def emojize():

#     userInput = input("Input: ")

#     if userInput == ':thumbsup:' or userInput == ':thumbs_up:':
#         print(emoji.emojize('Output :thumbs_up:'))

#     elif userInput == ':1st_place_medal:':
#         print(emoji.emojize('Output :1st_place_medal:'))

#     elif userInput == ':smile_cat:':
#         print(emoji.emojize('Output :smile_cat:'))

#     elif userInput == ':money_bag:':
#         print(emoji.emojize('Output :money_bag:'))

#     elif userInput == ':candy:':
#         print(emoji.emojize('Output :candy:'))



#version 3

def emojize():

    userInput = input("Input: ")

    sysOutput = emoji.emojize(userInput, language='alias')

    print('Output:', sysOutput)



main()