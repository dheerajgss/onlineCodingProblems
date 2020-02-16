"""Given a non-empty array of integers, return the integers which
   are repeating for atleast 'k' times.
   
   Ex: i/p = array = [1,1,1,1,2,2,2,3,3]
             k = 3
       o/p = [1,2] """

l = list(map(int ,input("Enter list values: ").split()))
m = set(l)
k = int(input("Enter k value: "))
n = []
for i in m:
    if(l.count(i) >= k):
        n.append(i)
print(n) 