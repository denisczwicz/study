#the winning play needs to win two out of three rounds
#the players can choose between scissor, paper or rock


for x in range(3):
    player_one = input("Rock paper scissor: ")
    player_two = input("Rock paper scissor: ")

    if player_one == "rock" and player_two == "rock":
        print("Tie!")

    elif player_one == "scissor" and player_two == "scissor":
        print("Tie!")

    elif player_one == "paper" and player_two == "paper":
        print("Tie!")

    elif player_one == "scissor" and player_two == "paper":
        print("Player one get a point!")

    elif player_one == "scissor" and player_two == "rock":
        print("Player two get a point!")

    elif player_one == "paper" and player_two == "scissor":
        print("Player two get a point!")

    elif player_one == "paper" and player_two == "rock":
        print("Player one get a point!")

    elif player_one == "rock" and player_two == "scissor":
        print("Player one get a point!")

    elif player_one == "rock" and player_two == "paper":
        print("Player two get a point!")