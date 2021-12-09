# oops. overwrote my process.py which did the counting.
text_file = open("input", "r")
inputstring = text_file.readlines()
inputstring = map(lambda s: s.strip(), inputstring)
text_file.close()


outputs=map(lambda s: s.split('|')[1],inputstring)
outputs = map(lambda s: s.strip(), outputs)


lengths=[0]*8


inputs=map(lambda s: s.split('|')[1],inputstring)
inputs = map(lambda s: s.strip(), inputs)




for i,inputsegs in enumerate(inputs):


    digitpossibilites=['']*8
    for digits in inputsegs.split(' '):
        if len(digits)==2:
            digitpossibilities[3]+=digits
            digitpossibilities[6]+=digits
        if len(digits)==4:
            digitpossibilities[2]+=digits
            digitpossibilities[3]+=digits
            digitpossibilities[4]+=digits
            digitpossibilities[6]+=digits
        if len(digits)==3:
            digitpossibilities[1]+=digits
            digitpossibilities[3]+=digits
            digitpossibilities[6]+=digits
