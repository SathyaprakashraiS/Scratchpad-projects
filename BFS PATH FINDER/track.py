import random
import queue

#a=[[0]*10]*10
#a=[[0,0,0,0,"S",0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,"F",0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
a=[[0,0,0,0,"S",0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,"F"]]
b=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
mode=0

#spoin=1
#fpoin=1

#while (spoin!=0):
#    q=random.randint(0,9)
#    w=random.randint(0,9)
#    if(a[q][w]!=2 or a[q][w]!=1 or a[q][w]!=3 or a[q][w]!="F"):
#        a[q][w]="S"
#        spoin=0
#    else:
#        spoin=1

#while(fpoin!=0):
#    q=random.randint(0,9)
#    w=random.randint(0,9)
#    if(a[q][w]!=2 or a[q][w]!=1 or a[q][w]!=3 or a[q][w]!="S"):
#        a[q][w]="F"
#        fpoin=0
#    else:
#        fpoin=1

#CODE TO PLACE OBSTACLES
for i in range(0,15):
    m=1
    while(m!=0):
        q=random.randint(0,9)
        w=random.randint(0,9)
        if(a[q][w]!=0):
            m=1
        else:
            a[q][w]=2
            b[q][w]=2
            m=0
"""
a[8][9]=2
b[8][9]=2
a[9][8]=2
b[9][8]=2
a[8][8]=2
b[8][8]=2
"""

def printer(a,path=""):
    for j in range(0,10):
        for x,pos in enumerate(a[j]):
            if pos=="S":
                start=x
                startrow=j
    print(f"START: {start}, {len(a)} {len(a[0])}")
    i=start
    j=startrow
    pos=set()
    for move in path:
        if move=="L":
            i-=1
        elif move=="R":
            i+=1
        elif move=="U":
            j-=1
        elif move=="D":
            j+=1
        pos.add((j,i))
    for j,row in enumerate(a):
        for i,col in enumerate(row):
            if(j,i) in pos:
                if(a[j][i]=="S"):
                    print("S  ",end=" ")
                    b[j][i]="S"
                elif(a[j][i]=="F"):
                    print("F  ",end=" ")
                    b[j][i]="F"
                else:
                    if(mode==0):
                        print("*  ",end=" ")
                        b[j][i]=1
                    else:
                        print("$  ",end=" ")
                        b[j][i]=3
            else:
                if(a[j][i]==2):
                    print("&  ",end=" ")
                else:
                    print(col," ",end=" ")
                    # FIX: do not change a[j][i] here
        print()


def valid(a,moves):
    for j in range(0,10):
        for x,pos in enumerate(a[j]):
            if pos=="S":
                start=x
                startrow=j
    i=start
    j=startrow
    for move in moves:
        if move=="L":
            i-=1
        elif move=="R":
            i+=1
        elif move=="U":
            j-=1
        elif move=="D":
            j+=1
        # Check if outside the grid
        if not(0 <= i < len(a[0]) and 0 <= j <len(a)):
            return False
        # Check if obstacle
        elif a[j][i] == 2:
            return False
    return True


def findEnd(a,moves):
    #print(a[0])
    for j in range(0,10):
        for x,pos in enumerate(a[j]):
            if pos=="S":
                start=x
                startrow=j
    i=start
    j=startrow
    for move in moves:
        if move=="L":
            i-=1
        elif move=="R":
            i+=1
        elif move=="U":
            j-=1
        elif move=="D":
            j+=1

    if a[j][i]=="F":
        print("SENJA MOVES:"+moves)
        printer(a,moves)
        return True
    return False

nums=queue.Queue()
nums.put("")
add=""
printer(a,"")
visited = set()
# Breadth First Search
while not nums.empty():

    add=nums.get()

    # ADD THIS
    # Find the position reached by this path
    start = None
    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] == "S":
                start = (row, col)

    i = start[1]
    j = start[0]

    for move in add:
        if move=="L":
            i-=1
        elif move=="R":
            i+=1
        elif move=="U":
            j-=1
        elif move=="D":
            j+=1

    # If we have already visited this position,
    # don't search it again
    if (j,i) in visited:
        continue

    visited.add((j,i))

    if findEnd(a,add):
        break

    for move in ["L","R","U","D"]:
        put=add+move
        if valid(a,put):
            nums.put(put)

else:
    print("NO PATH FOUND")
"""
while not nums.empty():
    if findEnd(a,add):
        break
    add=nums.get()
    for j in ["L","R","U","D"]:
        put=add+j
        if valid(a,put):
            nums.put(put)
else:
    print("NO PATH FOUND")
"""


"""
for i in range(0,10):
    for j in range(0,10):
        if(a[i][j]=="S"):
            b[i][j]="S"

for i in range(0,10):
    for j in range(0,10):
        print(b[i][j],end=" ")

    print("")
"""
