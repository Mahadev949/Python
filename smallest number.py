a,b,c=map(int, input().split())
if a==b==c:
        print("all are equal")
else:
    if a<=b:
        if a<c:
            print("a:- ",a)
        else:
            print("c",c)
    else:
        print("b",b)
