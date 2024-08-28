L=[[1,2],[1,5],[3,4],[5],[2,3]]
J={}
K=[]                                                    
D={}
X=[]
for i in range(len(L)):
    X.append([])



for i in range(len(L)):                                 #Global Liking
    for j in L[i]:
        J[j]=0
for i in range(len(L)):
    for j in L[i]:
        J[j]+=1
for i in J.keys():
    if J[i]==max(J.values()):
        K.append(i)
#print(K)
S=[[0]*len(L) for i in range(len(L))]




for i in range(len(L)):                                 #Local Liking 
    for j in range(len(L)):
        if i!=j:
            S[i][j]=len(set(L[i]) & set(L[j]))          #Similarity Matrix


for i in range(len(L)):                                 #Dictionary with people whom to recommend
    D[i+1]=[]


for i in range(len(L)):
    for j in range(len(L)):
        if S[i][j]==max(S[i]):
            D[i+1].append(j+1)

#for i in range(len(L)):            
    #print(S[i])  
    

for i in range(len(L)):                                  #Final Recommendation list
    for k in range(len(D[i+1])):
        X[i]=X[i]+list(set(L[D[i+1][k]-1]).difference(set(L[i])))
for i in range(len(X)):
    X[i]=list(set(X[i]))
    
print(X)



for i in range(len(X)):                                  #Mixing Global and Local liking
    for j in K:
        while len(X[i])<3 or ((set(X[i]) & set(K))==set(K)): 
            X[i].append(j)

    #print(D)
