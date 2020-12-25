import random as rnd

def game(wordDict):

    print("Welcome Bora!\n")
    print("Guessing a correct letter")
    print("won't take away your tries")
    # Define the dictionary for the type print
    dictTypes = {
    0: "Animals",
    1: "Objects",
    2: "Food",
    3: "Fruit"
    }

    # Declare the list for the word display
    display = list()

    # 10 tries
    tries = 0

    # Declare a set for the found keys
    foundKeys = set()
    
    # We define this to print the type of the word later
    wordRandom = rnd.randint(0, 3)

    wordType = dictTypes[wordRandom] 

    # Randomly choosing word from the wordDictionary
    word = wordDict[wordRandom][rnd.randint(0, 4)]

    # Populate the display list with underscores
    for i in range(len(word)):
        display.append('_')        

    # DEBUG
    # print(word) 

    # Print the word with it's type with its letter count
    print("Type of the word: " + wordType)
    print("\n\t\t" + ' '.join(display))

    
    while tries < 10:

        keyFound = 0
        inputKey = input("Input a key\n")

        for i in range(len(word)):
            if word[i] == inputKey:
                keyFound = 1

        if keyFound:
            print("Key was found")
            foundKeys.add(inputKey)
        else:
            print("Key was not found")
            tries += 1

        print("\n" + str(10 - tries) + " tries left")

        if display.count(inputKey):
            print("You have entered a known key")

        # Search for the found character in the set and
        # if found change the character with the same index
        # in the display list to it 
        if keyFound:
            for key in foundKeys:
                for i in range(len(word)):
                    if key == word[i]:
                        display[i] = key


        print("\n\t\t" + ' '.join(display))

        # End game and print when count
        # of '_' characters on display are zero
        if not display.count('_'):
            print("\n\t\t!!!YOU WON!!!\n")
            return 0
        # End game when you run out of tries
        if tries == 10:
            print("\n\t\t!!!YOU LOSE!!!\n")
            print("The word was " + word)
            return 1

# A dictionary with lists as values
# 0: Animals
# 1: Objects
# 2: Food
# 3: Fruit
wordDictionary = {
0:["cat", "parrot", "dog", "cockatiel", "gecko"],
1:["box", "brush", "calendar", "comb", "pencil"],
2:["pasta", "cake", "soup", "salad", "chips"],
3:["apple", "orange", "kiwi", "tangerine", "grape"]
}

game(wordDictionary)