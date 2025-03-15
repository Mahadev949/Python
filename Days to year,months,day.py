a=int(input())
print("years :-",a//365)
a%=365
count=0
month=[31,28,31,30,31,30,31,31,30,31,30,31]
print(a)
while (1):
    for i in month:
        if a<i:
            break
        a-=i
        print(a)
        count+=1
    if a<i:
        break
print("months :- ",count)
print("weeks :-:",a//7)
print("days :- ",a%7)
