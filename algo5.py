N, K = map(int, input().split())

chipList = []
minimumValue = 0

for i in range(N):
    chipList.append(int(input()))

for i in chipList[::-1]:
    if i > K:
        continue
    else:
        # if (K % i) < K:
        minimumValue += (K // i)
        K = K % i

print(minimumValue)



