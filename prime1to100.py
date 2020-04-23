n = 100

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(n + 1):
    if isPrime(i):
        print(i)

