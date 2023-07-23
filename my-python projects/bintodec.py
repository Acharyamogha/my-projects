def bintodec(b):
    dec=0
    pow=0
    while b>0:
        dig=b%10
        dec+=dig*(2**pow)
        b//=10
        pow+=1
    return dec
b=int(input("Enter a binary number "))
try:
    deci=bintodec(b)
    print("Decimal Equivalent", deci)
except ValueError:
    print("Invalid Input")