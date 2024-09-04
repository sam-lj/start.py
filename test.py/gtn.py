while True:
    import random
    print("Welcome to gusess the number game.")
    print("Would you like to start a new game?")
    print("Type in (y) for YES or (n) for NO.")

    if input().lower() == 'y':
        secretNumber = random.randint(1, 1000)
        print('I am thinking of a number between 1 and 1000.')
        print("Please note you only have 10 tries!")

        for guessesTaken in range(1, 11):
            print('Take a guess.')
            guess = int(input())

            if guess < secretNumber:
                print('Your guess is too low.')
            elif guess > secretNumber:
                print('Your guess is too high.')
            else:
                break    # This condition is the correct guess!

        if guess == secretNumber:
            print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!') 
        else:
            print('Nope. The number I was thinking of was ' + str(secretNumber))
            print("Better luck next time!")
    else:
        print("Ok see you next time!")
        print("Have a nice day!")
        print("Crdits:")
        print("Sam(Dev)")
        print("Liza(Tester)")
        break

