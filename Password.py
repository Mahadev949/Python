a=input("enter password:- ")
length=False
upper=False
lower=False
digit=False
symbol=False
if len(a)>=8:
    length=True
for i in a :
    if i.isdigit():
        digit=True
    elif i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i in "@#₹_&-+()/*\"':;!?~`|•√π÷×§∆€¥$¢^°={}\%©®™✓[]":
        symbol=True
if length and upper and lower and digit:
    print ("valid password")
else :
    print(" invalid password ")
