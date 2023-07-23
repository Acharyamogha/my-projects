import difflib
def string_sim(str1, str2):
    res=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return res.ratio()
str1=input("Enter string one: ")
str2=input("Enter string two: ")
print("Similarty between two strings is")
print(string_sim(str1,str2))
