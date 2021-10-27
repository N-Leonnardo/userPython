# 1

def countdown(num):
    newarrayy = []
    while num>=0:
        newarrayy.append(num)
        num -= 1
    return newarrayy

print(countdown(5))

# 2

def retandprin(num1,num2):
    print(num1)
    return(num2)

print(retandprin(1,2))

# 3

sum = 0

def first_plus_length(arr):
    sum = arr[0] + len(arr)
    print (sum)

fruits = [1,2,3,4,5]
first_plus_length(fruits)

# 4

def values_greater_than_second(arr):
    new_arr = []
    count = 0
    for i in range(0, len(arr)):
        if arr[i]> arr[1]:
            new_arr.append(arr[i])
            count += count + 1
            continue
    print(new_arr)

array = [5,2,3,2,1,4]

values_greater_than_second(array) 

# 5

def length_and_value(mult,num):
    newarray = []
    for i in range (0, mult):
        newarray.append(num)
    print(newarray)

length_and_value(6,2)