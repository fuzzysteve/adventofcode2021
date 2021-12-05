import re
text_file = open("input", "r")
lines = text_file.readlines()
lines = list(map(lambda s: s.strip(), lines))
text_file.close()

gridsize=1000
grid=[]

for gridx in range(0,gridsize):
    grid.append([0]*gridsize)


for line in lines:
    m=re.search(r'^(\d+),(\d+) -> (\d+),(\d+)$',line)
    x1=int(m.group(1))
    y1=int(m.group(2))
    x2=int(m.group(3))
    y2=int(m.group(4))
    if x1==x2:
        start=y1
        stop=y2
        if (y1>y2):
            stop=y1
            start=y2
        for ycoord in range(start,stop+1):
            grid[x1][ycoord]+=1
    if y1==y2:
        start=x1
        stop=x2
        if (x1>x2):
            stop=x1
            start=x2
        for xcoord in range(start,stop+1):
            grid[xcoord][y1]+=1

flatten=[item for sublist in grid for item in sublist]

overlap=sum([int(1) for x in flatten if x > 1])
print(overlap)
