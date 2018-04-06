import random
import card
class Deck:

    def __init__(self,no_of_decks = 1):
        self.NumberOfDecks = no_of_decks
        self.Cards = []
        self.MakeDeck(no_of_decks)
        self.Shuffle()

    def __repr__(self):
        return f"This deck contains {self.Count()} cards"
    
    
    def MakeDeck(self,num_of_decks):
        values = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
        suits = "Hearts Clubs Spades Diamonds".split()
        DeckToReturn = []

        for suit in suits:
            for value in values:
                DeckToReturn.append(card.Card(suit=suit,value=value))
        
        # self.Cards = DeckToReturn if num_of_decks == 1 else ",".join([",".join(DeckToReturn) for _ in range(num_of_decks)]).split(",")
        if num_of_decks == 1:
            self.Cards = DeckToReturn  
        else:
            for decks in range(num_of_decks):
                
                self.Cards.extend(DeckToReturn)
        
    def Count(self):
        return len(self.Cards)
    
    def _deal(self,num_of_cards = 1):
        cards_to_return = []
        for x in range(num_of_cards):
            if len(self.Cards) == 0:
                raise TypeError("Out of cards")
                break

            card = self.Cards.pop()
            cards_to_return.append(card)
        return cards_to_return

    def Shuffle(self):
        assert len(self.Cards) == (self.NumberOfDecks * 52) , "You can only shuffle full decks"
        random.shuffle(self.Cards)

    def DealCard(self):
        return self._deal(1)
    
    def DealHand(self,hand_size):
        return self._deal(hand_size)

deck = Deck(2)

# print(deck.Shuffle())
# print(deck.Cards)
# print(deck._deal(10))
print(deck.DealHand(5))

