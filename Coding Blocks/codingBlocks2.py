"""Given an array of nums, Move all the zeroes to the end
of it while maintaining a the relative order of the non-zero
elements.
Ex: [0,1,0,5,4,9]
Ans:[1,5,4,9,0,0]"""

l = list(map(int, input().split()))
n = len(l)
k = []
count = 0
i = 0
while(i<n):
    if(l[i] == 0):
        l.remove(0)
        count += 1
        n = len(l)
    i += 1
for i in range(count):
    l.append(0)
print(l)
