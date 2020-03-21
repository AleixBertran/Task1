A=  [[1,2],
    [2,3],
    [4,5]]
B=  [[3,4],
    [2,3]]
#Size of A = mxn
#Size of B = nxl
m=len(A)
if(len(A[0])!=len(B)):
    print("No es pot multipicar")
else:
    n=len(B)
l=len(B[0])
#Crear matriu resultat buida
C=[[[None]for i in range(l)]for j in range(m)] ##Dubte solucionat en https://stackoverflow.com/questions/13347559/create-empty-matrix-python
for i in range(m):
    for j in range(l):
        elem=0
        for x in range(n):
            elem=elem+ A[i][x]*B[x][j]
        C[i][j]=elem
print(C)
