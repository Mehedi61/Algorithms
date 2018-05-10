# Programmed by MD. Mehedi Hasan

import random

list_size = 20
my_list = random.sample(list(range(1, 40)), list_size)	# get some random numbers
my_list = sorted(my_list)

print("List:")
print(my_list)

def binary_search(list, item):
	low = 0
	high = len(list) - 1
	
	while low <= high:
		mid = (low + high)
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

print("\nIndex of the item:")
print(binary_search(my_list, 11))
