L=[["Hello","Hai"],["good","Morning"],["hai","hello"]]
L1=[]
for i in range(0,len(L)):
	if L[i][-1]!="hai" and L[i][-1]!="Hai":
	  L1.append(L[i])
L=L1
