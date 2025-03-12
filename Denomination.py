a=int(input())
five_hun=a//500
a%=500
one_hun=a//100
a%=100
fifty=a//50
a%=50
ten=a//10
print("Five Hundred Notes (500) : ",five_hun)
print("Hundred Notes (100) : ",one_hun)
print("Fifty Notes (50) : ",fifty)
print("Ten Notes (10) : ",ten)
