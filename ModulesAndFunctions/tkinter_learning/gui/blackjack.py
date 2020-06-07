import tkinter
import random


def load_cards(card_images):
    suits = ['heart', 'diamond', 'spade', 'club']
    faces = ['jack', 'queen', 'king']

    for suit in suits:
        for card in range(1, 11):
            name = f'cards/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
            # using double ()'s to append a tuple with the value and location of the card
        for card in faces:
            name = f'cards/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))
    return card_images


def deal_card(frame):
    # pop the top card so it is also removed from the list
    next_card = deck.pop(0)
    # add next_card to bottom of deck
    deck.append(next_card)
    # add image to a label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_card(hand):
    score = 0
    ace = False
    for card in hand:
        card_value = card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            ace = False
            score -= 10
    return score


# no parameters defined so function doesn't have to be called using ()'s
def dealer_deal():
    dealer_score = score_card(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_card(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_card(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


# no parameters defined so function doesn't have to be called using ()'s
def player_deal():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_card(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("dealer wins!")


def new_game():
    global player_card_frame
    global dealer_card_frame
    global dealer_hand
    global player_hand
    global dealer_score_label
    global player_score_label

    player_card_frame.destroy()
    dealer_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    result_text.set('')

    dealer_hand = []
    player_hand = []

    dealer_score_label.set(0)
    player_score_label.set(0)

    player_deal()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_card(dealer_hand))
    player_deal()


def play_game():
    player_deal()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_card(dealer_hand))
    player_deal()

    mainWindow.mainloop()


mainWindow = tkinter.Tk()

mainWindow.title('Black Jack')
mainWindow.geometry('640x480')
mainWindow.config(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=dealer_deal)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=player_deal)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=0, column=2)

# load cards
cards = []
load_cards(cards)
print(cards)

# create a new deck of cards to be shuffled
deck = list(cards)
# using list() so 'deck' is recognized as it's own variable and not a clone of cards
random.shuffle(deck)

dealer_hand = []
player_hand = []


if __name__ == '__main__':
    play_game()
