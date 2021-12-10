text_file = open("input", "r")
lines = text_file.readlines()
lines = list(map(lambda s: s.strip(), lines))
text_file.close()

scorematrix={'<':4,'{':3,'(':1,'[':2}


scores=[]

for line in lines:
    score=0
    brackets=list(line)
    stack=[]
    broken=False
    for brace in brackets:
        if brace in ['[','(','{','<']:
            stack.append(brace)
        else:
            last=stack.pop()
            if brace=='}':
                if last!='{':
                    broken=True
                    continue
            if brace=='>':
                if last!='<':
                    broken=True
                    continue
            if brace==')':
                if last!='(':
                    broken=True
                    continue
            if brace==']':
                if last!='[':
                    broken=True
                    continue
    if len(stack) and not broken:
        stack.reverse()
        for brace in stack:
            score=score*5
            score+=scorematrix[brace]
        scores.append(score)


scores.sort()
n=int(len(scores)/2)
print(scores[n])
