"""Given an array of integers, find the first non duplicate value in the array. 
   
   Ex: i/p = [1,2,3,1,5,4,4,3]
       o/p = 2
   Explanation: There are 2 non duplicate values, 2 and 5. But 2 occured 1st than 5. So answer is 2."""

d = {}
l = list(map(int ,input().split()))
for i in l:
    if(i in d):
        d[i] += 1
    else:
        d[i] = 1
flag = 0
for i in d:
    if(d[i] == 1):
        print(i)
        flag = 1
        break
if(flag == 0):
    print("Non duplicate value not found!")