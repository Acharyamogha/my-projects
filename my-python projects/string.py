s=input("Enter a sentence: ")
w,d,u,l,sp=0,0,0,0,0
lw=s.split()
w=len(lw)
for c in s:
    if c.isdigit():
        d+=1
    elif c.islower():
        l+=1
    elif c.isupper():
        u+=1
    else: sp+=1
print("Number of Words is ",w)
print("Number of Digits is ",d)
print("Number of Uppercase letter is ",u)
print("Number of Lowercase letter is ",l)
print("Number of Special characters is ",sp)
