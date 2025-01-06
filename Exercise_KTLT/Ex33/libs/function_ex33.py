from random import randrange


def random():
    arr=[]
    for _ in range(10):
        arr.append(randrange(0,100))
    return arr

def sum_of_array(arr):
    sum=0
    for value in arr:
        sum=sum+value
    return sum

def odd_element(arr):
    arr_odd=[]
    for value in arr:
        if value%2!=0:
            arr_odd.append(value)
    return arr_odd
def count_odd_element(arr_odd):
    count=0
    for _ in arr_odd:
        count=count+1
    return count

def find_smallest(arr):
    min=arr[0]
    for value in arr:
        if min>value:
            min=value
    return min

def double_value(arr):
    arr_double=[]
    for value in arr:
        arr_double.append(2*value)
    return arr_double

def sort_ascending(arr):
    arr.sort()
    return arr

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr
