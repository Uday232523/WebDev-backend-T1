def f(L,s):
    n=0
    List=[]
    for i in L:
	    n+=1
	    nL=[L[0]]                               # New list to prevent over count
	    k=1
	    while k<n:
	        nL.append(L[k])
	        k+=1
	    for j in nL:
		    if i+j==s:
			    List.append((i,j))
    return(List)
			
l=int(input("Enter Size Of Your List > "))
i=0
L=[]
print("Enter Elements")
while i<l:
    e=int(input())
    L.append(e)
    i+=1
s=int(input("Enter Your Target > "))
print(f(L,s)) 
