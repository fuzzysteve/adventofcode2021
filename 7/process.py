text_file = open("input", "r")
crabs = text_file.readline()
crabs = crabs.strip()
text_file.close()

crabstate=crabs.split(",")
crabstate = list(map(lambda s: int(s), crabstate))

minpos=min(crabstate)
maxpos=max(crabstate)

fuel=[0]*(max(crabstate)+1)

for target in range(minpos,maxpos+1):
    for crab in crabstate:
        fuel[target]+=abs(crab-target)


targetfuel=min(fuel)
targetpos=fuel.index(targetfuel)
print(targetfuel,targetpos)
