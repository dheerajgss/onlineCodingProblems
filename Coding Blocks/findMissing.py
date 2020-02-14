"""Given an array of integers ranging from 0 to n in a random order,
   fing the missing number in it. 
   
   Ex: i/p = [0,2,5,1,4]
       o/p = 3  """

l = list(map(int, input().split()))
n = len(l) + 1
m = [0 for x in range(n)]
for i in l:
   m[i] = 1
s = m.index(0)
print(s)