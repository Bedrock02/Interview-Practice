from random import randrange
'''
Design a class to respresent a deck of cards with operations
to shuffle the deck and to deal one card.
'''


class Card(object):

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def get_suit(self):
		return self.suit

	def get_value(self):
		if self.value == 11:
			return 'J'

		elif self.value == 12:
			return 'Q'

		elif self.value == 13:
			return 'K'

		elif self.value == 1:
			return 'A'

		else:
			return self.value

	def __str__(self):
		return "%s:%s" % (self.get_suit(), self.get_value())

	def __repr__(self):
		return self.__str__()


class Deck(object):

	def __init__(self):
		self.deck = []
		for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
			for value in range(1, 14):
				card = Card(suit, value)
				self.deck.append(card)

	def deal_one(self):
		card = self.deck[-1]
		self.deck = self.deck[:-1]
		return card

	def shuffle(self):
		newDeck = []
		cardsCollected = 0

		while cardsCollected != 52:

			if cardsCollected == 51:
				newDeck.append(self.deck[0])
			else:
				pick = randrange(1, 52 - cardsCollected)
				newDeck.append(self.deck[pick])
				self.deck = self.deck[0:pick] + self.deck[pick + 1:]

			cardsCollected += 1

		self.deck = newDeck

	def showDeck(self):
		for card in self.deck:
			print card

myDeck = Deck()
myDeck.showDeck()
print ""
print ""
myDeck.shuffle()
myDeck.showDeck()
