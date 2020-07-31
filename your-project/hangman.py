import random

def players():
    player_one = input("What's up player 1 --> what's your name? ")
    player_two = input("What's up player 2? Ready to beat up "+player_one+" --> what's your name? ")

    print("\n ********** Now we gonna choose the Hangman **********\n")
    possible_hangman = [player_one, player_two]
    hangman = random.choice(possible_hangman)
    print(hangman+" you are the hangman, please keep a word in mind \n")
    scoreboard_player_one = 0 
    scoreboard_player_two = 0

def start_game_hangman (): 
    players()
    
    while True:
        difficulty = input("Choose your difficulty: \n Easy \n Medium \n Hard \n Enter here: ")
        if difficulty == "Easy" or difficulty == "easy" or difficulty == "EASY": 
            while True: 
                word = input("\nEnter a word that has 4 letters\nEnter here...... ")
                word = word.lower()
                if len(word) == 4 and word.isalpha() == True: 
                    print("Good job you 've choosen for the EASY level")
                    break
                else: 
                    print("We only accept letters (ABCDE....) and with a lenght of 4!")
            break
        elif difficulty == "Medium" or difficulty == "medium" or difficulty == "MEDIUM": 
            while True: 
                word = input("\nEnter a word that has 6 letters\nEnter here...... ")
                word = word.lower()
                if len(word) == 6 and word.isalpha() == True: 
                    print("Good job, you 've choosen for the MEDIUM level")
                    break
                else: 
                    print("We only accept letters (ABCDE....) and with a lenght of 6!")
            break
        elif difficulty == "Hard" or difficulty == "hard" or difficulty == "HARD": 
            while True: 
                word = input("\nEnter a word that has 8 letters\nEnter here...... ")
                word = word.lower()
                if len(word) == 8 and word.isalpha() == True: 
                    print("Good job, you 've choosen for the HARD level")
                    break
                else: 
                    print("We only accept letters (ABCDE....) and with a lenght of 8!")
            break
        else: 
            print("\nYou can only pick Easy, Medium or Hard")
    
    guess = ""
    correct_guesses = []
    wrong_guesses = []
    hint = "help"
    rounds = 8
    turn = 1
    while rounds > 0:
        pattern = "_ "*len(word)
        print("---> word to guess == "+pattern) 
        guess = input("\n\nThis is round "+str(turn)+"\nPlease give us a letter a letter of the alphabet or the right answer: ")
        guess = guess.lower()
        cor_guess = ' '.join(correct_guesses)
        wro_guess = ' '.join(wrong_guesses)
        print("\n***CORRECT GUESSES ----> "+cor_guess+" <----***")

        if len(guess) == 1 and guess not in cor_guess and guess not in wro_guess and guess in word: 
            correct_guesses.append(guess)
            appears = word.count(guess)
            print("\nWow you've found a correct letter!\n it appears "+str(appears)+" time(s).")
            turn += 1
        elif len(guess) == 1 and guess not in word and guess not in wro_guess and rounds == 1: 
            wrong_guesses.append(guess)
            print("\n*** WRONG ANSWER *** YOU LOOSE A LIFE *** ")
            print("\n**** YOU LOSE AND DON'T GET THE $$$$$ --> PLEASE TRY AGAIN")
            rounds = rounds -1
        elif len(guess) == 1 and guess not in word and guess not in wro_guess: 
            wrong_guesses.append(guess)
            print("\n*** WRONG ANSWER *** YOU LOOSE A LIFE *** ")
            rounds = rounds -1
            print("*** YOU STILL HAVE "+str(rounds)+" LEFT***")
            turn += 1
        elif len(guess) != 1 and guess == "help":
            print(""" 
            Rule 1 --> give a letter from the alphabeth
            Rule 2 --> Try to guess the word 
            Rule 3 --> If you guess a wrong answer you lose a live!
            Rule 4 --> If you guess the word before the end of your lives you win!
            """)
        elif guess in cor_guess or guess in wro_guess: 
            print("\nYou have already give this letter.")
        elif len(guess) != 1 and guess != word and guess.isalpha() == True: 
            print("\nYou have entered more than one character!")
        elif guess == word :
            print("\nCongratz you've won the game in "+str(turn)+" turns!")
            break
        else: 
            print("\nPlease give a letter of the alphabet (ABCDEFGHILMNOPQRSTUVWXYZ) or the right answer")
    while True :
        again = input("\n ---> If you want to start over press '1' if you want to quit press 'q' : ") 
        if again == '1': 
            start_game_hangman()
        elif again == 'q' or again == 'Quit' or again == 'Q' or again == 'QUIT': 
            end = "\n *** SEE YOU NEXT TIME thanks for playing with BVS GAMES ***"
            break
        else: 
            print("\nPlease put in the number 1 or 'Q' :) ---> for help call Ironhack ")
    return end







    
print(start_game_hangman())