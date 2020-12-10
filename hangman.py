import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while(1):
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print("\nYou are right, The word is:",main)
            print("Congratulations! You win...")
            break

        print("Guess the word:" , main,end=" ")
        guess = input()

        while (guess not in validLetters):
            guess = input("Enter a valid character: ")
        else:
            guessmade = guessmade + guess
            
        if ((guess not in word) or (guess in main)):
            turns = turns - 1
            if turns == 9:
                print("\n9 turns left")
                print("------------")
            if turns == 8:
                print("\n8 turns left")
                print("------------")
                print("     O      ")
            if turns == 7:
                print("\n7 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("\n6 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("\n5 turns left")
                print("------------")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("\n4 turns left")
                print("-----------")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("\n3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("\n2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("\n1 turns left...")
                print("Last breaths counting, Take care!")
                print("------------")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("\nYou loose!")
                print("You let a kind man die!")
                print("------------")
                print("     O_|    ")
                print("    /|\     ")
                print("    / \     ")
                break

if __name__ == "__main__":
    print("\n---------------------Hangman Game-------------------------")
    name = input("\nPlease Enter your name: ")
    print("Welcome" , name,"!")
    print("\nDo you want to play Hangman game?")
    x = input("Press 'Y' for yes and 'N' for No: ").lower()
    while x != 'n':
        if x == 'y':
            print("\nTry to guess the word in less than 10 attempts: ")
            hangman()
            print("----------------------------------------------------------")
            print("\nDo you want to play Hangman game again?")
            x = input("Press 'Y' for yes and 'N' for No: ").lower()
        else:
            x = input("\nPlease Press only 'Y' for yes and 'N' for No: ").lower()
        
    else:
        print("\nThanks for giving your time to me...")
        print("have a nice day!")
