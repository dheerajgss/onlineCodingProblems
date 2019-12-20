t = int(input())
while(t):
    d1 = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    n = int(input())
    while(n):
        l = list(map(int ,input().split()))
        """print(l[0],l[1])"""
        k = l[0]
        s = l[1]
        if(k >= 9):
            pass
        elif(d1[k] < s):
            d1[k] = s
        n = n - 1
    count = 0
    for i in d1.values():
        if(i != 0):
            count += i
    print(count)
    t = t - 1