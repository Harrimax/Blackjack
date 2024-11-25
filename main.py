import random
from art import logo

my_cards = []
computers_card = []


def computer_dealer():
    comp_game = True
    while comp_game:
        random_comp_card = random.randint(1, 11)
        computers_card.append(random_comp_card)
        if sum(computers_card) > 16:
            comp_game = False
            return sum(computers_card)


def dealer(num):
    for num in range(num):
        rand = random.randint(1, 11)
        my_cards.append(rand)
    return sum(my_cards)

def result():
    print(f"Your final hand: {my_cards}, final score {my_score}")
    print(f"Computer's final hand: {computers_card}, final score {comp_score}")

game_start = True
while game_start:
    start = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        print("\n" * 20)
        print(logo)
        my_score = dealer(2)
        comp_score = computer_dealer()
    else:
        game_start = False

    game_on = True
    while game_on:
        print(f" Your cards {my_cards}, current score: {my_score}")
        print(f"Computer's first card is: {computers_card[0]}")
        if comp_score == 21:
            result()
            game_on = False
        else:
            to_play = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if to_play == "y":
                my_score = dealer(1)
            elif to_play == "n":
                result()
                if my_score > 21:
                    print("You lose")
                elif comp_score > my_score:
                    if comp_score > my_score and comp_score == 21:
                        print("You lose, opponent has BlackJack ")
                    elif comp_score > 21:
                        print("You win, opponent went over")
                    else:
                        print("You lose")
                elif comp_score == my_score:
                    print("Draw")

                elif my_score > comp_score:
                    if my_score > comp_score and my_score == 21:
                        print("You win with a Blackjack")
                    else:
                        print("You win")
                game_on = False

    my_cards = []
    computers_card = []


