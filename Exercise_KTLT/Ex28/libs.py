def convert_str_to_int(arr_str):
    arr_int=[]
    for s in arr_str:
        arr_int.append(int(s))
    return arr_int
def print_arr_perline(arr_int):
    for value in arr_int:
        print(value)
def get_even_digits(arr_int):
    arr_int_even=[]
    for value in arr_int:
        if value%2==0:
            arr_int_even.append(value)
    return arr_int_even
def negative(arr_int):
    negative=[]
    for value in arr_int:
        if value<0:
            negative.append(value)
    return negative
def check_prime_number(value):
    if value>0:
        n=value//2+1
        for i in range(2,n+1):
            if value % i == 0:
                return False
        return True
    else:
        return False
def list_prime(arr_int):
    prime=[]
    for value in arr_int:
        if check_prime_number(value):
            prime.append(value)
    return prime
def average(arr_int):
    s=0
    for value in arr_int:
        s=s+value
    average=s/len(arr_int)
    return average