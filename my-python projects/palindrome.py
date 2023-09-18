num=int(input("Enter a number"))
temp=num
rev,count=0,0
while num>0:
 dig=num%10
 rev=rev*10+dig
 num=num//10
if(temp==rev):
 print("the number is a palindrome")
 n=int(input("Enter a digit to find occurance"))
 while temp>0:
 if temp%10 == n:
 count+=1
 temp//=10
 print(f"Number of occurance of {n} is {count}")
else:
 print("number isnt a palindrome")
