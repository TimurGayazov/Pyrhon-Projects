def find(temp, check):
    for item in temp:
        if item == check:
            return True
    return False


def condition(temp):
    out = ""
    for index in range(temp.index("("), len(temp)):
        out += temp[index]
    return out.removesuffix(";")


if __name__ == '__main__':
    print("S0->", end="")
    outCode = ""
    labelName = "loop"
    labelID = 0
    prevCnt = 0
    keysMap = {}
    doID = 0
    print("S1->", end="")
    with open("in.cpp", "r") as sppFile:
        print("S2->", end="")
        doWhileCode = sppFile.read().split("\n")
        print("S3->", end="")
        for string in doWhileCode:
            cnt = 0
            print("S4->", end="")
            for i in string.split("\t"):
                if i == "":
                    cnt += 1
                    print("S5->", end="")
            stroke = string.split(" ")
            print("S6->", end="")
            for word in stroke:
                tempWord = word.split("\t")
                print("S7->", end="")
                if find(tempWord, "do") and (stroke[-1] == "{" or string[-1] == "o"):
                    print("S8->", end="")
                    doID += 1
                    print("S9->", end="")
                    if cnt >= prevCnt:
                        labelID += 1
                        print("S10->", end="")
                        if find(keysMap, labelID):
                            print("S11->", end="")
                            import collections

                            [last] = collections.deque(keysMap, maxlen=1)
                            labelID = last + 1
                            print("S12->", end="")
                    else:
                        labelID -= 1
                        print("S13->", end="")
                    keysMap[labelID] = 1
                    prevCnt = cnt
                    print("S14->", end="")
                    for i in tempWord:
                        if i == "":
                            outCode += "\t"
                            print("S15->", end="")
                    outCode += labelName + str(labelID) + ":"
                    print("S16->", end="")
                elif find(tempWord, "while") and doID >= 1:
                    print("S17->", end="")
                    doID -= 1
                    print("S18->", end="")
                    condition(string)
                    print("S19->", end="")
                    outCode += "if" + condition(string) + "{\n"
                    print("S20->", end="")
                    for i in range(cnt + 1):
                        outCode += "\t"
                        print("S21->", end="")
                    if cnt > prevCnt:
                        labelID += 1
                        print("S22->", end="")
                    elif cnt < prevCnt:
                        print("S23->", end="")
                        labelID -= 1
                    prevCnt = cnt
                    outCode += "goto " + labelName + str(labelID) + ";\n"
                    print("S24->", end="")
                    for i in range(cnt):
                        outCode += "\t"
                        print("S25->", end="")
                    outCode += "}"
                    print("S26->", end="")
                    break
                else:
                    outCode += word + " "
                    print("S27->", end="")

            outCode += "\n"
            print("S28->", end="")
    with open("out.cpp", "w+") as sppFile:
        sppFile.write(outCode)
        print("S29->", end="")
    print("S0", end="")
