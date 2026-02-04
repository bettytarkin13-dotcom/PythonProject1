# 21BOOM
import random
from random import choice

suits = ("❤️", "♦️", "♣️", "♠️")
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

player_one_cards = []
player_two_cards = []

player_one_cards.append(random.choice(cards))
player_one_cards.append(random.choice(cards))
print("player one cards:", player_one_cards)

player_two_cards.append(random.choice(cards))
player_two_cards.append(random.choice(cards))
print("player two cards:", player_two_cards)


def calculate_total(hand):
    total = 0
    for card in hand:
        if type(card) == int:
            total+= card
        elif card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 1
    return total


STOP = 0
CONTINUE = 1

while True:
    total_player_one = calculate_total(player_one_cards)
    print("player one cards:", player_one_cards)
    print("total", total_player_one)

    if total_player_one == 21:
        print("player one wins the game")
        break
    elif total_player_one > 21:
        print("player one Disqualified! he have more than 21")
        break

    choice = int(input("0=STOP,1=CONTINUE"))
    if choice == STOP:
        print("Player one retires")
        break

    elif choice == CONTINUE:
        new_card=random.choice(cards)
        player_one_cards.append(new_card)
        print("player one got new card:", player_one_cards)


while True:
    total_player_two = calculate_total(player_two_cards)
    print("player two cards:", player_two_cards)
    print("total", total_player_two)

    if total_player_two == 21:
        print("player two wins the game")
        break
    elif total_player_two > 21:
        print("player two Disqualified! he have more than 21")
        break


    choice = int(input("0=STOP,1=CONTINUE"))
    if choice == STOP:
        print("Player two retires")
        break
    elif choice == CONTINUE:
        new_card=random.choice(cards)
        player_two_cards.append(new_card)
        print("player two got new card:", player_two_cards)

total_player_one = calculate_total(player_one_cards)
total_player_two= calculate_total(player_two_cards)

print("n--final result--")
print("player_one_total:", total_player_one)
print("player_two_total:", total_player_two)

if total_player_one>21 and total_player_two>21:
    print("to sad you both disqualified")
elif total_player_one > 21:
    print("to sad player one,your disqualified!player two wins")
elif total_player_two>21:
    print("to sad player two,your disqualified!player one wins")
else:
    if total_player_one > total_player_two:
        print("plyer one you are the winner")
    elif total_player_two > total_player_one:
        print("plyer two you are the winner")
    else:
        print("it's a draw")






