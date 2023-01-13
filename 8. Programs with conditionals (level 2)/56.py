import random

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissors below:" )

items = ["Rock", "Paper", "Scissors"]
place = [1,2,3]

if player in items:
    i = items.index(player)

player_place = place[i]

computer = random.randint(1,3)

if player_place == computer:
    print("It's a tie! Try again.")
else:
    if player_place == 1 and computer == 2:
        print("You lose! Your opponent chose 'Paper'")
    elif player_place == 1 and computer == 3:
        print("You win! Your opponent chose 'Scissors'")
    elif player_place == 2 and computer == 1:
        print("You win! Your opponent chose 'Rock'")
    elif player_place == 2 and computer == 3:
        print("You lose! Your opponent chose 'Scissors'")
    elif player_place == 3 and computer == 1:
        print("You lose! Your opponent chose 'Rock'")
    elif player_place == 3 and computer == 2:
        print("You win! Your opponent chose 'Paper'")