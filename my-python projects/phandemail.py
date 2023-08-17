import re
phone=re.compile(r'\+\d{12}')
email=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,}')
with open('demo.txt','r') as f:
    for line in f:
        matches=phone.findall(line)
        for i in matches:
            print(i)
        matches=email.findall(line)
        for i in matches:
            print(i)
