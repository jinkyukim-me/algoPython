x, y = map(int, input().split())

num = [True] * (y - x - 1)
count = 0
N = 1

while N * N <= y:
    N += 1
    square = N * N
    i = x // square

    while square * i <= y:
        idx = square * i - x

        if idx >= 0 and num[idx]:
            count += 1
            num[idx] = False
        i += 1

print(len(num - count))


