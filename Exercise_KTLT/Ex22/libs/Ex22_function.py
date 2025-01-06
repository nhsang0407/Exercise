def H(N,D,M):
    """
    Calculate probability that the employee picks 1 damaged light bulb out of the M bulbs picked
    :param N: number of light bulbs in a box
    :param D: number of damaged light bulbs in a box
    :param M: number of light bulbs picked
    :return: probability 1 damaged light bulbs out of M bulbs picked
    """
    p=C(D,1)*C(N-D,M-1)/C(N,M)
    p=round(p,4)
    return p

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def C(n,k):
    c=factorial(n)/(factorial(n-k)*factorial(k))
    return c
