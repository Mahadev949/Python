a=int(input(" user 1 \n 1.rock\n 2. paper\n 3. scissor \n "))
b=int(input(" user  2 \n 1.rock\n 2. paper\n 3. scissor \n "))
if a==b:
    print('tie')
elif (a==1 and b==3) or ( a==2 and b==1) or ( a==3 and b==2) :
    print(" user 1 wins")
elif a>3:
    print(" select correct option ")
else :
    print(" user 2 wins")
