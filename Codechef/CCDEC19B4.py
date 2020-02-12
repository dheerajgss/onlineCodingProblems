t = int(input())
while(t):
    a = input()
    b = input()
    if(int(b) == 0):
        print(0)
    elif(int(a) == 0):
        print(1)
    else:
        num1 = 0
        num2 = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            num1 = num1 + (int(a[i])*2**i)
        for i in range(len(b)):
            num2  = num2 + (int(b[i])*2**i)
        count = 0
        while(num2 > 0):
            u = num1 ^ num2
            v = num1 & num2
            num1 = u
            num2 = v*2
            count += 1
        print(count)
    t = t  - 1 