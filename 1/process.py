text_file = open("input", "r")
depth = text_file.readlines()
depth = map(lambda s: int(s.strip()), depth)
text_file.close()
depthlength=len(depth)
increase=0
decrease=0
for index in range(1,depthlength):
    if depth[index]>depth[index-1]:
        increase=increase+1
    elif depth[index]<depth[index-1]:
        decrease=decrease+1
print("Increases: {}\nDecreases: {}".format(increase,decrease))
