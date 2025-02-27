import random

def generate_random_array():
    size=random.randint(5,20)
    return [random.randint(0,100) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j] , arr[j-1]
            j -=1
            

def binary_search(sequence,item):
    begin_index=0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint=begin_index + (end_index-begin_index)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value==item:
            return midpoint
        elif item < midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return None

random_array=generate_random_array()
print('Unsorted Random Array : ',random_array)
            
# arr=[2,6,5,1,3,4]
# print('Unsorted Array :',arr)
insertion_sort(random_array)
print('Sorted Random Array : ',random_array)

print('Our sorted Array has ',len(random_array),'elements')
item_a=random.randrange(0,len(random_array)-1)
item_search=random_array[item_a]
print('We are searching for the element in the ',item_a,'place of the sorted array..that is ',random_array[item_a])
print('now we will do a search on this sorted array')
result=binary_search(random_array,item_search)
print('the item was found at place ',result)
