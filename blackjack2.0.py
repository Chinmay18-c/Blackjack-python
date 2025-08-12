import random
import os
import time
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

play_again = True
credits = 1000

def both_cards():
    for _ in range(2):
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    ace(your_cards)
    ace(computer_cards)

    game_over = True
    while game_over:
        print(Fore.CYAN + f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(Fore.YELLOW + f"Computer's first card: {computer_cards[0]}")

        if sum(your_cards) == 21 or sum(your_cards) > 21:
            game_over = False
            break
        else:
            another_card = input(Fore.CYAN + "Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                your_cards.append(random.choice(cards))
                ace(your_cards)
            else:
                break

    while sum(computer_cards) < 18:
        computer_cards.append(random.choice(cards))
        ace(computer_cards)

def compare(bet):
    global credits
    player_score = sum(your_cards)
    computer_score = sum(computer_cards)

    print(Fore.CYAN + f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(Fore.YELLOW + f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    if player_score > 21:
        print(Fore.RED + "You went over 21. YOU LOSE 😭😭!")
        credits -= bet
    elif computer_score > 21:
        print(Fore.GREEN + "Computer went over 21. YOU WIN 🥳🥳")
        credits += bet
    elif player_score == 21 and len(your_cards) == 2:
        print(Fore.GREEN + "Blackjack! YOU WIN.")
        credits += bet
    elif computer_score == 21 and len(computer_cards) == 2:
        print(Fore.RED + "COMPUTER WINS with Blackjack.")
        credits -= bet
    elif player_score > computer_score:
        print(Fore.GREEN + "YOU WIN!")
        credits += bet
    elif player_score < computer_score:
        print(Fore.RED + "YOU LOSE!")
        credits -= bet
    else:
        print(Fore.YELLOW + "Draw!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while play_again:
    if credits <= 0:
        print(Fore.RED + "You have no credits left. Game over!")
        break

    print(Fore.MAGENTA + f"Current credits: {credits}")
    game = input(Fore.CYAN + "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if game == 'y':
        while True:
            try:
                bet = int(input(Fore.CYAN + "Place your bet: $"))
                if 1 <= bet <= credits:
                    break
                else:
                    print(Fore.RED + "Invalid bet amount.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")

        your_cards = []
        computer_cards = []
        clear()
        time.sleep(0.5)
        from blackjackArt import logo
        both_cards()
        compare(bet)

    elif game == 'n':
        print(Fore.YELLOW + "Goodbye!")
        play_again = False
