"""Given two string s1 and s2, check whether s2 is an
   anagram of s1.
   
   Ex: i/p := s1 = 'anagram', s2 = 'nagaram'
       o/p = true
       
       i/p := s1 = 'rat', s2 = 'car'
       o/p = false"""

s1 = input()
s2 = input()
s = set(s1)
flag = 0
for i in s:
    if(s1.count(i) != s2.count(i)):
        print("false")
        flag = 1
        break
if(flag == 0):
    print("true")

"""Or you can use this logic after reading the input.
   
   if(sorted(s1) == sorted(s2)):
       print("true")
   else:
       print("false") """