text_file = open("input", "r")
fish = text_file.readline()
fish = fish.strip()
text_file.close()


fishstate=fish.split(",")
fishstate = list(map(lambda s: int(s), fishstate))


daycount=80

for x in range(1,daycount+1):
    newfish=[]
    for fishage in fishstate:
        if fishage==0:
            newfish.append(8)
            newfish.append(6)
        else:
            newfish.append(fishage-1)
    fishstate=newfish

print(len(fishstate))
