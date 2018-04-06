class Card:

    def __init__(self,suit,value):
        self.Value = value
        self.Suit = suit 
    
    def __repr__(self):
        return f"{self.Value} {self.Suit}"