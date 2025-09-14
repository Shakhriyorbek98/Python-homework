# 1. Problems is_prime(n) funksiyasi

def is_prime (n):
    if n<=1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# 2. digit_sum(k) funksiyasi


def digit_sum(k):
    total=0
    for digit in str(k):
        total +=int(digit)
    return total

# 3. Ikki sonning darajalari

def powers_of_two(N):
    k = 1 
    while 2 ** k <= N:
        print(2 ** k, end=" ")
        k += 1

N = int(input("N ni kiriting: "))
powers_of_two(N)
