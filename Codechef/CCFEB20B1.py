"""Problem code: SNUG_FIT """

t = int(input())
while(t):
    n = int(input())
    a = list(map(int ,input().split()))
    b = list(map(int ,input().split()))
    i = 0
    diam = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        if(a[i] < b[i]):
            diam += a[i]
        else:
            diam += b[i]
    print(diam)
    t -= 1