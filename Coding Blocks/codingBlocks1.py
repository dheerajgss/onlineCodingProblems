"""Check whether a given sentence is a palindrome or not.
   Ex: A man, a plan, a canal: Panama!!
   Output: True
   Hint: Convert sentence into alphanumeric."""



s = input()
st = ""
n = len(s)
for i in range(n):
    if(s[i].isalnum()):
        if(s[i].isupper()):
            st = st + (s[i].lower())
        else:
            st += s[i]
print(st)
if(st[::-1] == st):
    print("True")
else:
    print("False")
