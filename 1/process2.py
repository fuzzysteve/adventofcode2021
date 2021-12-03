text_file = open("input", "r")
depth = text_file.readlines()
depth = map(lambda s: int(s.strip()), depth)
text_file.close()
depthlength=len(depth)
increase=0
decrease=0
for index in range(3,depthlength):
    windowone=depth[index]+depth[index-1]+depth[index-2]
    windowtwo=depth[index-3]+depth[index-1]+depth[index-2]
    if windowone>windowtwo:
        increase=increase+1
    elif windowtwo<windowtwo:
        decrease=decrease+1
print("Increases: {}\nDecreases: {}".format(increase,decrease))
