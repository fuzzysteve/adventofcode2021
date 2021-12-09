text_file = open("input", "r")
inputstring = text_file.readlines()
inputstring = map(lambda s: s.strip(), inputstring)
text_file.close()

depthmap=[]

for line in inputstring:
    depths=list(line)
    depths=map(lambda s: int(s),depths)
    depthmap.append(depths)



ymax=len(depthmap)
xmax=len(depthmap[0])

lowrisk=0

for y in range(0,ymax):
    for x in range (0,xmax):
        up=y-1
        down=y+1
        left=x-1
        right=x+1
        lowspot=1
        if up>=0:
            if depthmap[y][x]>=depthmap[up][x]:
                lowspot=0
        if down<ymax:
            if depthmap[y][x]>=depthmap[down][x]:
                lowspot=0
        if left>=0:
            if depthmap[y][x]>=depthmap[y][left]:
                lowspot=0
        if right<xmax:
            if depthmap[y][x]>=depthmap[y][right]:
                lowspot=0
        if lowspot:
            lowrisk+=depthmap[y][x]+1


print lowrisk
