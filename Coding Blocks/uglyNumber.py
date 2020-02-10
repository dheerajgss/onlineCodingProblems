"""Find out the nth ugly number. Ugly numbers are positive numbers whose prime factors only
   include 2, 3, 5.
   
   Ex: i/p -> n = 10
       o/p -> 12
   Explanation: 1 2 3 4 5 6 8 9 10 12 is the sequence of 1st 10 ugly numbers. So 10th ugly number is 12."""

n = int(input())
count = 1
i = 1
while(count < n):
    i += 1
    if(i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        count += 1
print(i)