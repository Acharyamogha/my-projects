def sumdigit(n):
 total=0
 while n!=0:
  total+=n%10
  n=n//10
 return total

num=int(input("enter a number"))
s=sumdigit(num)
print("sum is ",s)