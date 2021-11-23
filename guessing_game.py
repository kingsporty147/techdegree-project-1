import random


def start_game():

    gameover = 0
    counter = 0
    randNumberStart = 1
    randNumberEnd = 10
    answer = random.randint(randNumberStart, randNumberEnd)
    highScore = 0

    print("Number Guessing Game")

    playerName = input("What is your name?  ")

    print("Welcome to Number Guessing Game, {}".format(playerName))

    while gameover == 0:
        counter += 1

        print("Current high score: {}".format(highScore))
        magicNumber = input("Guess the magic number from 1-10?  ")

        try:
            magicNumber = int(magicNumber)

            if magicNumber > randNumberEnd or magicNumber < randNumberStart:
                raise ValueError(
                    "Please try again with number between {} and {}".format(
                        randNumberStart, randNumberEnd
                    )
                )

            if magicNumber > answer:
                raise ValueError("It's lower")
            if magicNumber < answer:
                raise ValueError("It's higher")

        except ValueError as err:
            print("Error: {}".format(err))

        else:
            if magicNumber == answer:
                print("Got it, it took you {} attempts ".format(counter))
                print("Game Over")

                checkIfplayAgain = input("Do you want to play again?  ")

                if checkIfplayAgain == "y":

                    if counter < highScore:
                        highScore = counter
                    elif highScore == 0:
                        highScore = counter

                    gameover = 0
                    counter = 0
                    answer = random.randint(randNumberStart, randNumberEnd)

                else:
                    print("Goodbye")
                    gameover = 1


start_game()
