N = int(input())
numberList = []

for i in range(N):
    numberList.append(int(input()))

numberList.sort(reverse=True)

for i in range(N):
    print("%s" % numberList.pop())

