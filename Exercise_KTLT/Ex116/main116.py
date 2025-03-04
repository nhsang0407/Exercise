import numpy as np

arr=np.random.randint(-100,501,10) #-100 to 500, 10 phan tu
print(arr)

#print ra gia tri tu vi tri 2 toi 5
arr2_1=arr[[2,3,4,5]]
print(arr2_1)
arr2_2=arr[2:6]
print(arr2_2)

arr3=arr[arr<0]
print(arr3)

#x=int(input("Enter x:"))
#y=int(input("Enter y:"))
"""arr4=arr[x<=arr]
arr4_2=arr4[arr4<=y]
print(arr4_2)"""
x=-100
y=100
arr4 = arr[(x <= arr) & (arr <= y)]
print(arr4)

arr5=np.sort(arr)
print(arr5)

arr6=np.sort(arr)[::-1]
print(arr6)

print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

#delete perfect number
def is_perfect_square(n):
    return n >= 0 and int(np.sqrt(n)) ** 2 == n
arr7=np.array([x for x in arr if not is_perfect_square(x)])
print(arr7)

#v=int(input("Enter v:"))
v=2
arr8=np.insert(arr,v,x) #mang, index, value
print(arr8)