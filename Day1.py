

dir = 0
x = 0
y = 0

locations = ["0,0"]
loc = "NULL"

userin = input("enter data")

list = userin.split(", ")
print(list)
for index in list:
    if index[0] == "L":
        dir = dir - 1
        if dir == -1:
            dir = 3
        if dir == 4:
            dir = 0
        elif dir > 4:
            print("Direction Error")
    elif index[0] == "R":
        dir = dir + 1
        if dir == -1:
            dir = 3
        elif dir == 4:
            dir = 0
        elif dir > 4:
            print("Direction Error")
    else:
        print("Index Error")


    len = int(index[1:])

    for i in range(len):

        if dir ==   0: #North
            y = y + 1
        elif dir == 1:#East
            x = x + 1
        elif dir == 2: #South
            y = y - 1
        elif dir == 3: #West
            x = x - 1
        else:
            print("error")
        loc = str(x) + "," + str(y)

        if loc in locations:
            print("found")
            print(loc)
        print(loc)

        locations.append(loc)


