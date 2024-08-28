def sp(n):
    (dx,dy) = (0,1)                                             # Starting increments
    (x,y) = (0,0)                                               # Starting location
    A = [[None]* n for i in range(n)]                           # Empty Matrix
    for i in range(1,n**2+1,1):
        A[x][y] = i
        (nx,ny) = (x+dx, y+dy)                                  # New x and y
        if 0<=nx<n and 0<=ny<n and A[nx][ny] == None:           # First two for bounds last one to not overwrite 
            (x,y) = (nx,ny)
        else:
            (dx,dy) = (dy,-dx)                                   # Rotation clockwise
            (x,y) = (x+dx, y+dy)
    return A

def spiral(A):
    n = range(len(A))
    for x in n:
        print(str(A[x]))  


n=int(input("Enter A Positive Integer > "))
spiral(sp(n))

