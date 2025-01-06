from Exercise_KTLT.Ex28.libs import *

s=input("Nhap chuoi la cac so co ngan cach [;]: ")
arr_str=s.split(";")
arr_int=convert_str_to_int(arr_str)
print(arr_int)
print_arr_perline(arr_int)

arr_int_even=get_even_digits(arr_int)
print("count even =",len(arr_int_even))

arr_int_negative=negative(arr_int)
print("Count negative =",len(arr_int_negative))

arr_int_prime=list_prime(arr_int)
print(arr_int_prime)
print("Count prime =",len(arr_int_prime))

print("Average value: ",average(arr_int))
