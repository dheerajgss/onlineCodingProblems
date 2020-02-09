"""Given a sorted array of integers, print the sorted array of squares of the given integers.
   
   Ex: i/p = [-5, -3, 0, 1, 2, 4]
       o/p = [0, 1, 4, 9, 16, 25]
    
   Constraints:
    1 <= n <= 100000
    -100000 <= a[i] <= 100000
    
    Note:
     Input will be always given in sorted order.  """

l = sorted(list(map(int, input().split())))
p1 = 0
pn = len(l) - 1
m = [0 for x in range(len(l))]
i = len(l) - 1
while(p1 <= pn):
    if(l[p1]**2 > l[pn]**2):
        m[i] = l[p1]**2
        i -= 1
        p1 += 1
    else:
        m[i] = l[pn]**2
        i -= 1
        pn -= 1
print(m)