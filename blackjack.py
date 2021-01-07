import random
from random import randrange

class player:
    def __init__(self):
        self.hand = []
        self.total = 0
        self.wins = 0
        self.hitLimit = randrange(21)

    def add(self, card):
        self.hand.append(card)
        self.total+=card.getValue()

    def getTotal(self):
        return self.total
    
    def decreaseAce(self):
        for card in hand:
            if card.getValue()==11:
                card.setValue(1)
    
    def addWin(self):
        self.wins+=1

    def getWins(self):
        return self.wins

    def newGame(self):
        self.hand.clear()
        self.total = 0

    def getHitLimit(self):
        return self.hitLimit

class deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            if i == 0:
                s = 'Hearts'
            elif i == 1:
                s = 'Clubs'
            elif i == 2:
                s = 'Spades'
            else:
                s = 'Diamonds'
            for j in range(2,15):
                if(j==14):
                    obj = card(11, s)
                elif(j>=10):
                    obj = card(10, s)
                else:
                    obj = card(j, s)
                self.cards.append(obj)

    def remove(self, card):
        self.cards.remove(card)

    def deal(self):
        if(len(self.cards)>0):
            r = random.choice(self.cards)
            self.remove(r)
            return r

class card:
    def __init__(self, num, suit):
        self.value = num
        self.symbol = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.symbol

    def setValue(self, i):
        self.value = i

def main():
    players = []
    for i in range(20):
        players.append(player())
        print("Player hitlimit is "+str(players[i].getHitLimit()))
        for j in range(20):
            stack = deck()
            players[i].add(stack.deal())
            while players[i].getTotal()<=players[i].getHitLimit():
                players[i].add(stack.deal())
            if players[i].getTotal()<=21:
                print("The player stayed under 21")
            else:
                print("The player lost")
            players[i].newGame()
                
if __name__ == "__main__":
    main()