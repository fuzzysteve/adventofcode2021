text_file = open("input", "r")
diag = text_file.readlines()
diag = map(lambda s: s.strip(), diag)
text_file.close()
counter=[0]*12
limiter=len(diag)/2
for values in diag:
    digits=list(values)
    counter=[counter[i] + int(digits[i]) for i in range(len(counter))]

gamma=int("".join(map(lambda d: ("1","0")[d<=limiter] ,counter)),2)
epsilon=int("".join(map(lambda d: ("1","0")[d>limiter] ,counter)),2)
