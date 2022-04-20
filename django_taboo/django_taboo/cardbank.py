import random 
import os
class CardBank:

	def __init__(self):
		self.bank = {}
		self.pars = []

	def get_words_for_cards(self, origin):
		with open(origin, 'r') as file: 
			lines = file.read()
			#formatting must have each word on a newline, with entries separated by an empty line
			pars = lines.split("\n\n")
		return pars

	def create_card_bank(self):
		for ix, entry in enumerate(pars): 
			words = entry.split("\n")
			key = words[0]
			taboos = words[1:]
			self.bank[key] = taboos
		return self.bank

	



test = CardBank()
pars = test.get_words_for_cards('raw_bank.txt')
test.create_card_bank()

# returns a randomly chosen key value pair as a tuple 
res = key, val = random.choice(list(test.bank.items()))


print(f"Word: {res[0].upper()}\n-----------\n{os.linesep.join(map(str,res[1]))}")
print(test.bank)