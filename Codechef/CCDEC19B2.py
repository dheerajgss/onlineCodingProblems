t = int(input())
while(t):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    z = []
    tw = []
    for i in range(n):
        if(l[i] == 0):
            z.append(i)
    for i in range(n):
        if(l[i] == 2):
            tw.append(i)
    twl = len(tw)
    lz = len(z)
    count = (twl*(twl-1)//2) + (lz*(lz-1)//2)
    print(count)
    t = t - 1