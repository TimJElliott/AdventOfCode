

userIn = "1"
list = [[], [], []]
count = 0
while userIn != None:

    userIn = input("Enter the input")
    list[0] = userIn.split(" ")
    userIn = input()
    list[1] = userIn.split(" ")
    userIn = input()
    list[2] = userIn.split(" ")

    #print(list)

    i = 0
    while i < 3:
        list[i] = [x for x in list[i] if x != '']
        i += 1

    sum = []
    print(list)
    j = 0
    while j < 3:
        k = 0
        sum.clear()
        while k < 3:
            sum.append(list[k][j])
            k += 1
        print(sum)
        if int(sum[0]) + int(sum[1]) > int(sum[2]):
            print(int(sum[0]) + int(sum[1]) > int(sum[2]))
            if int(sum[1]) + int(sum[2]) > int(sum[0]):
                print(int(sum[1]) + int(sum[2]) > int(sum[0]))
                if int(sum[0]) + int(sum[2]) > int(sum[1]):
                    print(int(sum[0]) + int(sum[2]) > int(sum[1]))
                    count += 1
        j += 1
        print(count)

print(count)














