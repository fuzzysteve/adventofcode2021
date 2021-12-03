text_file = open("input", "r")
route = text_file.readlines()
route = map(lambda s: s.strip(), route)
text_file.close()
x=0
y=0
for direction in route:
    way,distance=direction.split(' ')
    if way == 'forward':
      x=x+int(distance)
    elif way == "down":
      y=y+int(distance)
    elif way == "up":
      y=y-int(distance)
print("X: {}\nY: {}\nmultiple: {}".format(x,y,x*y))
