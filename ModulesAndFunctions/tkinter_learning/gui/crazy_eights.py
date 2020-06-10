import random
import tkinter


def load_cards(card_images):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    faces = ['Jack', 'Queen', 'King']

    for suit in suits:
        for card in range(1, 11):
            name = f'cards/{str(card)}_{suit.lower()[0: -1]}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        for card in faces:
            name = f'cards/{card}_{suit.lower()[0: -1]}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))
    return card_images


def shuffle_deck(card_list):
    random.shuffle(card_list)
    return deck


def deal_card(frame):
    # pop card from top of deck
    next_card = deck.pop(0)
    # add card back to bottom of deck
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1]).pack(side='left')
    return next_card


def deal_show_card():
    global card_up
    # pop card from top of deck
    next_card = deck.pop(0)
    # assign card to card_up variable
    card_up = next_card
    tkinter.Label(show_card_frame, image=card_up[1]).grid(row=0, column=1)


def initial_deal():
    for i in range(8):
        player_hand.append(deal_card(player_card_frame))
        dealer_hand.append((deal_card(dealer_card_frame)))
        deal_show_card()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global show_card_frame
    global player_hand
    global dealer_hand

    dealer_card_frame.destroy()
    show_card_frame.destroy()
    player_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame)
    dealer_card_frame.grid(row=0, column=1, sticky='ew')

    show_card_frame = tkinter.Frame(card_frame)
    show_card_frame.grid(row=1, column=1)

    player_card_frame = tkinter.Frame(card_frame)
    player_card_frame.grid(row=2, column=1, sticky='ew')

    player_hand = []
    dealer_hand = []

    initial_deal()


def play():
    initial_deal()
    mainWindow.mainloop()


def draw_card():
    pass


mainWindow = tkinter.Tk()

mainWindow.title("Crazy 8's")
mainWindow.geometry('900x400')
mainWindow.config(background='green')

card_frame = tkinter.Frame(mainWindow)
card_frame.grid(row=0, column=0, sticky='ew')

# dealer label and card frame
tkinter.Label(card_frame, text='Dealer').grid(row=0, column=0, sticky='w')
dealer_card_frame = tkinter.Frame(card_frame)
dealer_card_frame.grid(row=0, column=1, sticky='ew')

# card to show frame
show_card_frame = tkinter.Frame(card_frame)
show_card_frame.grid(row=1, column=1)
# tkinter.Label(show_card_frame, image=show_card_variable).grid(row=0, column=0)

# player label and card frame
tkinter.Label(card_frame, text='Player').grid(row=2, column=0)
player_card_frame = tkinter.Frame(card_frame)
player_card_frame.grid(row=2, column=1, sticky='ew')

# frame for buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=2, column=0)

# buttons
play_card_button = tkinter.Button(button_frame, text='Play Card').grid(row=0, column=0)
draw_card_button = tkinter.Button(button_frame, text='Draw Card').grid(row=0, column=1)
new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game).grid(row=0, column=2)

dealer_hand = []
player_hand = []
cards = []
load_cards(cards)
deck = list(cards)
shuffle_deck(deck)
card_up = None

if __name__ == '__main__':
    play()

print(card_up)
print(deal_show_card())