import random
from decimal import *
import sys

SIZE = 2**128-1

def generate_shares(n, m, secret):
    coefficients = coeff(m, secret)
    shares = []
    for i in range(1, n+1):
        x = random.randrange(1, SIZE)
        shares.append((x, polynom(x, coefficients)))
    return shares


def polynom(x, coefficients):
    point = 0
    for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
        point += x ** coefficient_index * coefficient_value
    return point


def coeff(t, secret):
    coeff= []
    for i in range(0,t-1):
        coeff.append(random.randrange(0, SIZE))
    coeff.append(secret)
    return coeff


def reconstruct_secret(shares):
    res = Decimal(0)
    for i in range(0,len(shares)):
        p = Decimal(1)
        for j in range(0,len(shares)):
            if i != j:
                p*=(Decimal(Decimal(shares[j][0]) / (Decimal(shares[j][0])-Decimal(shares[i][0]))))

        res+= (Decimal(Decimal(p) * Decimal(shares[i][1])))

    return int(round(Decimal(res), 0))
    return int(res)



if __name__ == '__main__':
    if sys.argv[1]=='split':
        mode=0
    elif sys.argv[1]=='recover':
        mode=1
    else:
        mode=-1
    getcontext().prec = 256
    if (mode==0):
        secret  = int(input(),16)
        array =  input().split(' ')
        n = int(array[0])# count of participants
        k = int(array[1])# count of thresholder shares
        shares = generate_shares(n,k,secret)
        for value in shares:
            print(hex(value[0]),hex(value[1]))
    elif mode==1:
        count = int(input())
        shares = []
        for i in range(0,count):
            value = input().split(' ')
            value[0] = int(value[0],16)
            value[1]= int(value[1],16)
            shares.append(value)

        secret = reconstruct_secret(shares)
        print(hex(secret))
    else:
        print('Unknown args')


