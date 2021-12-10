import random


playing = True
game_session = True

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def show(self):
        print ("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"] :
            for v in range (1, 14):
                self.cards.append(Card(s, v))
    
    def show(self): 
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


    def drawcard(self):
        return self.cards.pop()

    


class Player(object):
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.append(Deck.drawcard())
        return self

    def showhand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def dealer(self, dealer):
        self.dealer = dealer
        self.dealer_hand = []
    
    def add_card(self):
        return self.cards.append()




def display(self):
       if self.dealer:
            print("hidden")
            print(self.cards[1])
       else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())


class Game: 
    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle
            self.player_hand = Player()
            self.dealer_hand = Player()

            for i in range(2):
                self.player_hand.add_card(self.drawcard())
                self.dealer_hand.add_card(self.drawcard())       

            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input(
                        "Please enter 'hit' or 'stick' (or H/S) ").lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    game_over = True

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")


if __name__ == "__main__":
    game = Game()
    game.play()

   
            