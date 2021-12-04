text_file = open("input", "r")
inputfile = text_file.readlines()
inputfile = list(map(lambda s: s.strip(), inputfile))
inputfile = list(map(lambda s: s.replace('  ',' '), inputfile))
text_file.close()


draw=inputfile.pop(0).split(",")

inputfile.pop(0)

boardcount=int((len(inputfile)+1)/6)

boardlist=[]
drawmatch=[]
numbersdrawn=[]
matchcycle=[]


for boardnum in range(0,boardcount):
    newboard=[]
    for boardrownum in range(0,5):
        boardrow=inputfile[(boardnum*5)+boardrownum+boardnum].split(" ")
        newboard.append(boardrow)
    boardlist.append(newboard)
    drawmatch.append([0]*10)

for drawnumber in draw:
    numbersdrawn.append(drawnumber)
    for boardnum in range(0,boardcount):
        for boardrownum in range(0,5):
            if drawnumber in boardlist[boardnum][boardrownum]:
                drawmatch[boardnum][boardrownum]=drawmatch[boardnum][boardrownum]+1
                for boardcolumn in range (0,5):
                    if boardlist[boardnum][boardrownum][boardcolumn] == drawnumber:
                        drawmatch[boardnum][boardcolumn+5]=drawmatch[boardnum][boardcolumn+5]+1

    matchboard=[5 in board for board in drawmatch]
    if matchboard.count(True)==boardcount:
        break
    matchcycle.append(matchboard)


boardmatched=matchcycle.pop().index(False)


matchedboard=boardlist[boardmatched]


flatten=[item for sublist in matchedboard for item in sublist]

boardsum=sum([int(x) for x in flatten if x not in numbersdrawn])
winnumber=numbersdrawn.pop()
print(boardsum*int(winnumber))
