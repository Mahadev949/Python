a=input()
b=""
for i in a:
    if i =="A":
        b+=" and "
        continue 
    elif i=="B":
        b+=" or "
        continue 
    elif i=="C":
        b+=" xor "
        continue 
    b+=i
print(eval(b))
    
