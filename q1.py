#WARS
import random

suits = ("❤️", "♦️", "♣️", "♠️")
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

player_score=0
computer_score=0

while player_score<10 and computer_score<10:
 player_card = random.choice(cards)
 computer_card = random.choice(cards)

 player_suit = random.choice(suits)
 computer_suit = random.choice(suits)

 print(f"player_card: {player_card} {player_suit}")
 print(f"computer_card: {computer_card} {computer_suit}")

 if cards.index(player_card) > cards.index(computer_card):
    player_score+=1
    print("player wins this round!")
 elif cards.index(player_card) < cards.index(computer_card):
    computer_score+=1
    print("computer wins this round!")
 elif cards.index(player_card) == cards.index(computer_card):
    print("drew! 0 points")

print(f"player_score: {player_score}")
print(f"computer_score: {computer_score}")

print("----------------------------")
if player_score==10:
    print("Player wins the game!🎉")
else:
    print("Computer wins the game! 💻")


