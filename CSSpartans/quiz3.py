'''
Implement the function makeChange(cents, coins)

Given an input cents and coins, makeChange should output an object that contains 
the minimum amount of coins needed to equate to cents in value.

Coins is an array that contains the coin values.

Input
makeChange will take in 2 parameters, 
an integer cents, 

and an unsorted array of integers, coins

Note: coins will always contain a 1

Output

makeChange should output an object.
The objects keys should be the value of the coin and the key values should be mapped to the amount of coins needed

Sample data
cents => 132
coins => [25, 10, 5, 1]
makeChange(cents, coins) => {25: 5, 10: 0, 5: 1, 1:2}
Here it will need 5 quarters, 1 nickel, and 2 pennies (25*5 + 5*1 + 1*2 = 132)

'''
from collections import defaultdict
def makeChange(cents, coins):
	purse = defaultdict(int)
	coins.sort(reverse=True)
	for coin in coins:
		purse[coin]

	while(cents):
		factors = findFactors(cents, coins)
		if factors:
			coin = factors[0]
			purse[coin] = cents/coin
			cents -= coin*purse[coin]
			coins.remove(coin)
			continue
		else:
			for coin in coins:
				numberOfCoins = cents/coin
				if numberOfCoins:
					purse[coin] = numberOfCoins
					cents -= coin*numberOfCoins
					coins.remove(coin)
					break
	return purse

def findFactors(cents, coins):
	factors = []
	for coin in coins:
		if cents%coin == 0 and coin is not 1:
			factors.append(coin)
	return factors


print makeChange(132, [25, 10, 5, 1])
