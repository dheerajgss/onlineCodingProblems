"""Problem code: CASH """

t = int(input())
while(t):
    n, k = map(int ,input().split())
    l = list(map(int, input().split()))
    count = 0
    for i in range(len(l)):
        if(l[i] % k > 0):
            count += (l[i]%k)
    print(count%k)
    t -= 1