def roman_integer(roman):
    roman_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total,prev=0,0
    for char in reversed(roman):
        curr=roman_dict[char]
        if curr<prev:
            total-=curr
        else:
            total+=curr
        prev=curr
    return total
roman=input("Enter a roman Numeral ")
integer=roman_integer(roman)
print("integer value of roman numeral is ",integer)