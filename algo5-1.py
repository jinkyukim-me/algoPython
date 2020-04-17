N, K = map(int, input().split())
coinList = []
minValue = 0

for i in range(N):
    coinList.append(int(input()))

for i in coinList[::-1]:
    if i > K:
        continue
    else:
        minValue += K // i
        K = K % i

print(minValue)

