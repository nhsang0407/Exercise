def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def A(n,k):
    a=factorial(n)/factorial(n-k)
    return a
def C(n,k):
    c=factorial(n)/(factorial(n-k)*factorial(k))
    return c
