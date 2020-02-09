"""Given an array of integers, find the first duplicate value in the array. 
   
   Ex: i/p = [1,2,3,1,5,4,4,3]
       o/p = 1
   Explanation: There are 3 duplicate values, 1, 3 and 4. But 1 occured before 3 and 4. So answer is 1."""

d = {}
l = list(map(int ,input().split()))
for i in l:
    if(i in d):
        d[i] += 1
    else:
        d[i] = 1
flag = 0
for i in d:
    if(d[i] > 1):
        print(i)
        flag = 1
        break
if(flag == 0):
    print("Duplicate value not found!")