# Linear Search Algorithm using Python3
# Programmed by MD. Mehedi Hasan

my_list = [1, 2, 3, 4, 5]

search_item = int(input("enter a number: "))

if search_item in my_list:

	get_index = my_list.index(search_item)   # index number of the search_item
	print(str(search_item) + " is found at index number " + str(get_index) + " .")

else:
	
	print(str(search_item) + " is not on the list.")

