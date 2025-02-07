#Basic Cellular Automata Rule Generator

numChars = 125 #Must be Odd
numLines = (int)((numChars - 1) / 2)

#tbc = Three Bit Code
def ruleXor(tbc): 
    robc = "0"  #return one bit code
    if tbc[0] == "0" and tbc[1] == "0" and tbc[2] == "0":
        robc = "0"
    elif tbc[0] == "0" and tbc[1] == "0" and tbc[2] == '1':
        robc = "1"
    elif tbc[0] == "0" and tbc[1] == "1" and tbc[2] == '0':
        robc = "1"
    elif tbc[0] == "0" and tbc[1] == "1" and tbc[2] == '1':
        robc = "0"
    elif tbc[0] == "1" and tbc[1] == "0" and tbc[2] == '0':
        robc = "1"
    elif tbc[0] == "1" and tbc[1] == "0" and tbc[2] == '1':
        robc = "0"
    elif tbc[0] == "1" and tbc[1] == "1" and tbc[2] == '0':
        robc = "0"
    elif tbc[0] == "1" and tbc[1] == "1" and tbc[2] == '1':
        robc = "0"
    return robc
    
def calculateLine(numLines, numChars):
    startingOnePosition = numLines
    topLine = ["0"] * numChars
    topLine[startingOnePosition] = "1"
    print("".join(topLine))
    underLine = ["0"] * numChars
    for j in range(numLines - 1):
        for i in range(len(topLine)):
            if i == 0:
                continue
            elif i >= (len(topLine)-1):
                continue
            else:
                topLineChunk = "".join(topLine[i-1 : i+2])
                underLine[i] = ruleXor(topLineChunk)
        print("".join(underLine)) 
        topLine = underLine[:]   
    
    
calculateLine(numLines, numChars)