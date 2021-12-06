text_file = open("input", "r")
fish = text_file.readline()
fish = fish.strip()
text_file.close()


fishstate=fish.split(",")
fishstate = list(map(lambda s: int(s), fishstate))


daycount=256

newfish=[0]*9
for fishage in fishstate:
   newfish[fishage]+=1

fishstate=newfish

for x in range(1,daycount+1):
    newfish=[0]*9
    for age,counter in enumerate(fishstate):
        if age==0:
            newfish[8]+=counter
            newfish[6]+=counter
        else:
            newfish[age-1]+=counter
    fishstate=newfish



print(sum(fishstate))
