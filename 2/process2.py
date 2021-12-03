text_file = open("input", "r")
route = text_file.readlines()
route = map(lambda s: s.strip(), route)
text_file.close()
x=0
y=0
aim=0
for direction in route:
    way,distance=direction.split(' ')
    if way == 'forward':
      x=x+int(distance)
      y=y+(int(distance)*aim)
    elif way == "down":
      aim=aim+int(distance)
    elif way == "up":
      aim=aim-int(distance)
print("X: {}\nY: {}\nmultiple: {}".format(x,y,x*y))
