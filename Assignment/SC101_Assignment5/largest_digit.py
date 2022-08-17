"""
File: largest_digit.py
Name: Antina
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: number to find largest digit
	:return: returns largest digit
	"""
	if n < 0:
		n = -n
	return helper(n, 0)


def helper(num, largest):
	"""
	:param num:  number to find largest digit
	:param largest: largest digit
	:return:  returns largest digit
	"""
	if num == 0:
		return largest
	else:
		n = num % 10
		largest = max(n, largest)
		return helper(num // 10, largest)






if __name__ == '__main__':
	main()
