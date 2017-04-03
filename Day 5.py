import hashlib
import os
from random import randint

userIn = input("Enter the puzzle imput")
password = ["","","","","","","",""]
hash = ""
value = False
i = 0
enc = [False, False, False, False, False, False, False, False]

while value == False:
    m = hashlib.md5()
    m.update((userIn + str(i)).encode('UTF-8'))
    hex = m.hexdigest()
    j = 0
    temp = 0
    for j in range(0,5):
        if hex[j] == "0":
            temp+=1
        else:
            break
    if temp == 5:
        if hex[5].isdigit():
            if -1 < int(hex[5]) < 8:
                if enc[int(hex[5])] == False:
                    enc[int(hex[5])] = True
                    password[int(hex[5])] = hex[6]
    print(i)
    i+=1


    for l in range(8):
        if enc[l] == False:
            num = randint(48,122)
            while 57<num<97:
                num = randint(48,122)
            password[l] = num
            password[l] = chr(password[l])

    print("----------".join(password))
print("Password: "+''.join(password))
