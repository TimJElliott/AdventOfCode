class Code:
    initialInput = ""
    name = "BLANK"
    rawName = "BLANK"
    sectorID = 0
    checkSum = "BLANK"
    decoy = False
    def __init__(self, init):
        self.initialInput = init
    def Parse(self):
        for i in range(0, len(self.initialInput)):
            if self.initialInput[i].isdigit():
                break
        self.rawName = self.initialInput[0:i]
        self.name = [x for x in self.rawName if x != '-']

        for j in range(0, len(self.initialInput)):
            if self.initialInput[j] == "[":
                break
        self.sectorID = self.initialInput[i:j]
        self.checkSum = self.initialInput[j+1:-1]
    def PrintParams(self):
        print("Name: "+str(self.name)+"\nSector ID: "+str(self.sectorID)+"\nCheckSum: "+self.checkSum)
    def CheckDecoy(self):
        letters = {}
        for i in self.name:
            if i in letters.keys():
                letters[i] = int(letters.get(i)) + 1
            else:
                letters.update({i: 1})
        #print(str(letters))
        #print(sorted(zip(letters.values(),letters.keys()), key=None, reverse=True))
        sortedList = sorted(zip(letters.values(),letters.keys()), key=None, reverse=True)
        j = 0
        key = ""
        while j < 5:
            dupe = False
            dupes = []
            for k in sortedList:
                if k[0] == sortedList[j][0] and k[1] != sortedList[j][1]:
                    dupe = True
                    break
            if dupe:
                for k in sortedList:
                    if k[0] == sortedList[j][0]:
                        dupes.append(k)
                dupes.sort(key = lambda l: l[1])
                for p in dupes:
                    if p[1] not in key:
                        key += str(p[1])
                        break
            else:
                  key += str(sortedList[j][1])
            #print(dupes)
            j += 1
        if key == self.checkSum:
            return True
        else:
            return False
    def Decrypt(self):
        #a is 97, z is 122
        key = int(self.sectorID)%26
        asciiList = [ord(x) for x in self.rawName]
        for j in range(0,len(asciiList)):
            if asciiList[j] != 45:
                asciiList[j]+=key
            else:
                asciiList[j] = 32
        for i in range(0,len(asciiList)):
            if asciiList[i] > 122:
                asciiList[i] = (asciiList[i]-122)+96

        self.name = [chr(x) for x in asciiList]
        print(''.join(self.name))



#Main "class"
userIn = "BLANK"
sum = 0
while userIn != None:
    userIn=input()

    code = Code(userIn)
    code.Parse()

    if(code.CheckDecoy()):
        print("********Not a Decoy********")
        code.PrintParams()
        code.Decrypt()
    else:
        print("Decoy Found")
