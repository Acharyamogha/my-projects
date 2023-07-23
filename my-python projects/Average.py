num1=int(input("Enter the marks in 1st Subject: "))
num2=int(input("Enter the marks in 2nd Subject: "))
num3=int(input("Enter the marks in 3rd Subject: "))

if num1>num2:
    if num2>num3:
        total=num1+num2
    else:
        total=num1+num3
elif num1>num3:
    total=num1+num2
else:
    total=num2+num3
avg=total/2
print("Average of two best marks is ",avg)
