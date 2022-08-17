"""
File: coin_flip_runs.py
Name: Antina Yeh
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	num = int(input('Number of runs:'))

	coin = 'TH'
	random = r.choice(coin)
	run = random

	while num != 0:
		random = r.choice(coin)
		if run[-1] == random:
			if len(run) == 1 or run[len(run)-2] != random:
				num -= 1
		run += random

	return print(run)










# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
