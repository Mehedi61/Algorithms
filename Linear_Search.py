# Linear Search Algorithm using Python3
# Programmed by MD. Mehedi Hasan

my_list = [1, 2, 3, 4, 5]

input_item = int(input("enter a number: "))

get_index = my_list.index(input_item)

if input_item in my_list:
	
	print(str(input_item) + " is found at index number " + str(get_index) + " .")

