class Player(object):
	
	def __init__(self, name, bankroll = 1000):
		self.name = name
		self.bankroll = bankroll
		self.bet = 0
		self.cards = []
		
	def bet(self, bet):
		if self.bankroll >= bet:
			self.bet += bet
			self.bankroll -= bet
			return true
		else:
			println("You don't have the enough credit, try with a smaller bet")
			return false
	
	def win(self, money):
		self.bankroll += money
		resetValues()
		
	def lose(self):
		self.bankroll -= self.bet
		resetValues()
		
	def resetValues(self):
		self.bet = 0
		self.cards = []	
	
	def hitCard(self, card):
		self.cards.append(card)
		
	def getAses(self):
		ases = 0;
		for card in self.cards:
			if card.getValue() == 1:
				ases += 1
		return ases
	
class Card(object):
	
	def __init__(self, symbol, value):
		self.symbol = symbol
		self.value = value;
		
	def getSymbol(self):
		return self.symbol
		
	def getValue(self):
		return self.value
		

player = Player("steve")			