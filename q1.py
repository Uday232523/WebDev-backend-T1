s1=input("Write first string ")
s2=input("Write second string ")
i=0
for s in s1:
    if s in s2:
        i+=1
if i==0:
    print("Strings are complimentary")
else:
    print("Strings are not complimentary")
