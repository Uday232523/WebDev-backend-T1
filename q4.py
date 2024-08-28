L=[]
for i in range(1,6,1):
	L.append(int(input(f"Enter Number {i} > ")))
n=1
for i in range (1,min(L)+1,1):
    j=0
    for k in range(0,5,1):
        if L[k]/i==L[k]//i:
            j+=1
            if j==5:
                n=i
    
print(f"GCD of the given 5 numbers is {n}")
	

