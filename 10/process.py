text_file = open("input", "r")
lines = text_file.readlines()
lines = list(map(lambda s: s.strip(), lines))
text_file.close()

scorematrix={'>':25137,'}':1197,')':3,']':57}


score=0
for line in lines:
    brackets=list(line)
    stack=[]
    for brace in brackets:
        if brace in ['[','(','{','<']:
            stack.append(brace)
        else:
            last=stack.pop()
            if brace=='}':
                if last!='{':
                    score+=scorematrix[brace]
                    continue
            if brace=='>':
                if last!='<':
                    score+=scorematrix[brace]
                    continue
            if brace==')':
                if last!='(':
                    score+=scorematrix[brace]
                    continue
            if brace==']':
                if last!='[':
                    score+=scorematrix[brace]
                    continue


print(score)
