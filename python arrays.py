# Write a function to add integer values of an array
'''
num_list = [1,2,3,4,5,6,7]
sum = 0
for item in num_list:
    sum += item
print("sum of numbers", sum)
'''
# Write a function to calculate the average value of an array of integers


'''def avg_of_arr(arr):
    sum = 0
    for item in arr:
        sum += item
    avg = sum/len(arr)
    return avg


arr = [1, 2, 3, 4, 5, 6, 7]
print(avg_of_arr(arr))
'''

# Write a program to find the index of an array element


'''
arr = [1, 2, 3, 4, 5, 6, 7]

print('index of "5" is >', arr.index(5))
print('index of "6" is >', arr.index(6))
print('index of "2" is >', arr.index(2))
'''

# Write a function to test if array contains a specific value

'''
def fun(array):
    for item in arr:
    if item == 3:
        print('element exist')


arr = [1, 2, 3, 4, 5, 6, 7]
fun(arr)
'''

# Write a function to remove a specific element from an array

'''
def fun(array, ele):
    arr.remove(ele)


arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
fun(arr, 2)
print(arr)
'''

# Write a function to copy an array to another array

'''
arr = [1, 2, 3, 4, 5, 6, 7]
arr1 = arr.copy()
print(arr1)
'''

# Write a function to insert an element at a specific position in the array

'''
arr = [1, 3, 4, 5, 6, 7]
arr.insert(1, 2)
print(arr)
'''

# Write a function to find the minimum and maximum value of an array


'''
arr = [1, 3, 4, 5, 6, 7]

minposition = arr.index(min(arr))
print("The minimum is at position:", minposition)

maxposition = arr.index(max(arr))
print("The maximum is at position::", maxposition)
'''


# Write a function to reverse an array of integer values.

'''
arr = [1, 2, 3, 4, 5, 6, 7]
arr.reverse() 
print(arr)
'''

# Write a function to find the duplicate values of an array

'''
arr = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]

for i in range(0, len(arr)):
    for k in range(i+1, len(arr)):
        if arr[i] == arr[k]:
            print('duplicates in the array', arr[k])
'''

# Write a program to find the common values between two arrays

'''
arr1 = ['r', 'a', 'j']
arr2 = ['r', 'a', 'j', 'k', 'u', 'm', 'a', 'r']

print(set(arr1).intersection(arr2))
'''

# Write a method to remove duplicate elements from an array

'''
arr = ['r', 'a', 'j', 'k', 'u', 'm', 'a', 'r']
fin_arr = []
for item in arr:
    if item not in fin_arr:
        fin_arr.append(item)
print(fin_arr)
'''

# Write a method to find the second largest number in an array

'''
arr = [7, 5, 3, 2, 4, 6, 1]
arr.sort()
print('the second largest number is>', arr[-2])
'''


# Write a method to find number of even number and odd numbers in an array.

'''
arr = [1,2,3,4,5,6,7,8,9]
evennumbers = 0
oddnumbers = 0
for i in arr:
    if i % 2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1 
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)
'''

# Write a function to get the difference of largest and smallest value.


'''
arr = [7, 5, 3, 2, 4, 6, 1]
arr.sort()
print("Diffrence of largest and smallest value:",arr[-1]-arr[0])
'''

# Write a method to verify if the array contains two specified elements(12,23).

'''
arr = [1,12,19,23,33,54]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")
'''
