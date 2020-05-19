N = int(input())

cnt_list = []

for i in range(N):
    cnt_list.append(int(input()))

cnt_list.sort()

for i in range(N):
    print('%s' % cnt_list.pop())


