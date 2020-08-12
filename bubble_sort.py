
def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)): 
        for j in range(1, len(list_of_numbers) - i):
            if list_of_numbers[j-1] > list_of_numbers[j]: 
                temp = list_of_numbers[j-1]
                list_of_numbers[j-1] = list_of_numbers[j]
                list_of_numbers[j] = temp
    return list_of_numbers



unsorted_list = [20, 31, 5, 1, 591, 1351, 693]
print(unsorted_list)
print(bubble_sort(unsorted_list))
