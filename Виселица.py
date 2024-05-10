#Игра "Hangman"
import random
def hangman(word):
    wrong = 0
    countLetters = list(word)
    board = ["__"] * len(word) 
    stages = ["", 
              "_________        ", 
              "|                ",
              "|        |       ",
              "|        0       ",
              "|     /  |  \    ",
              "|      /   \     ",
              "|                ",
            ]
    win = False
    print("Добро пожаловать!")
    while wrong < len(stages) - 1:
        print("\n")
        message = "Введите букву: "
        guess = input(message)
        if guess in countLetters:
            guessIndex = countLetters.index(guess)
            board[guessIndex] = guess
            countLetters[guessIndex] = "$"
            print(board)
        else:
            wrong += 1
            print(" ".join(board))
            print("\n".join(stages[0:(wrong + 1)]))
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
       print("\n".join(stages[0:(wrong)]))
       print("Вы проиграли! Было загадано слово: {}".format(word))

arrWords = ['кот', 'машина', 'велосипед', 'динозавр']
hangman(arrWords[random.randint(0,3)])