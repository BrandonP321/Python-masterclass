import random


def load_cards(cards_list):
    faces_and_ace = ['jack', 'queen', 'king', 'ace']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    for suit in suits:
        for card in range(2, 11):
            cards_list.append((str(card), card, suit))
        for card in faces_and_ace:
            if card == 'ace':
                cards_list.append((card, 1, suit))
            else:
                cards_list.append((card, 10, suit))

    return cards_list


def player_hand_start(cards_list):
    players_cards = []
    for j in range(2):
        random_card = random.randint(0, len(cards_list) - 1)
        players_cards.append(cards_list[random_card])
        cards_list.remove(cards_list[random_card])
    return players_cards


def dealer_hand_start(cards_list):
    dealers_cards = []
    for j in range(2):
        random_card = random.randint(0, len(cards_list) - 1)
        dealers_cards.append(cards_list[random_card])
        cards_list.remove(cards_list[random_card])
    return dealers_cards


def new_card(hand, total_cards):
    random_card = random.randint(0, len(total_cards) - 1)
    hand.append(total_cards[random_card])
    total_cards.remove(total_cards[random_card])
    return hand


def player_hand_game(hand, total_cards):
    while player_score(hand) <= 21:
        for card in hand:
            print(f'{card[0]} {card[2]}', end=', ')
        print(f"score = {player_score(hand)}")
        move = input('Would you like to hit or stay? ')
        print()
        if 'h' in move:
            new_card(hand, total_cards)
        else:
            break
    return player_score(hand)


def dealer_play(hand, total_cards):
    while player_score(hand) < 17:
        new_card(hand, total_cards)
    return player_score(hand)


def player_score(hand):
    score = 0
    for card in hand:
        score += card[1]
    return score


def result(player_hand, dealer_hand):
    if player_score(player_hand) > 21:
        return "BUST, dealer wins"
    elif player_score(dealer_hand) > 21:
        return "Dealer BUSTS, you win"
    elif player_score(player_hand) > player_score(dealer_hand):
        return "You win"
    else:
        return "You lose"


while 'n' not in input("Play again? "):
    cards = []
    load_cards(cards)


    my_hand = player_hand_start(cards)
    dealers_hand = dealer_hand_start(cards)

    print(player_hand_game(my_hand, cards))
    print(dealer_play(dealers_hand, cards))

    print(result(my_hand, dealers_hand))