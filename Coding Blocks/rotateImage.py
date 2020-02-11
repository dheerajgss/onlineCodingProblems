"""Given a NxN matrix, rotate the matrix in 90 degrees. """

l = []
n = int(input("Enter value of n for the squared matrix: "))
for i in range(n):
    m = []
    for j in range(n):
        m.append(int(input("Enter element value: ")))
    l.append(m)
print(l)
print()
for i in range(n):
    for j in range(i,n):
        temp = l[i][j]
        l[i][j] = l[j][i]
        l[j][i] = temp


for i in range(n):
    for j in range(n):
        print(l[i][j], end =" ")
    print()

print()
for i in range(n):
    for j in range(n-1,-1,-1):
        print(l[i][j], end = " ")
    print()

""" If you want the result in a matrix rather than printing, use this

for i in range(n):
    for j in range(n//2):
        temp = l[i][j]
        l[i][j] = l[i][n-j-1]
        l[i][n-j-1] = temp 
        
""" 