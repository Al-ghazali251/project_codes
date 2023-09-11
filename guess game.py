def any_no_of_person_guess_game():
    num = input("Type in number of players: ")
    for j in range(3):
        print("Round",j)

        while not num.isdigit():
            num = input("Please type a number here: ")
        players_score = [0] * int(num)
        for i in range(int(num)):
            print("Player ", i+1, "Playing")
            secret = random.randint(0, 9)
            guess = input("Guess the  correct number here: ")
            while not guess.isdigit():
                guess = input("Please type a number here 🙁: ")
            if int(guess) == secret:
                print("Correct")
                print("Guess number is", secret)
                players_score[i] += 1
            else:
                print("Wrong")
                print("Guess number is", secret)


    for i in range(len(players_score)):
        print("Player ", i+1, "Score is ", players_score[i])
    winner = 0
    for i in range(len(players_score)-1):
        if players_score[i] > players_score[i + 1]:
            players_score[i] = players_score[i]
            winner = i
    if players_score[winner] == 0:
        print("No winner")
    else:
        print("The winner is player ", i - 1)