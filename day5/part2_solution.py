from collections import deque

def ExtractInput(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n')for line in f]

    crateInput = []
    inputSeparation = 0

    for i in range(len(input)):
        if input[i] == "":
            inputSeparation = i
            break
        crateInput.append(input[i][1::][::4])

    directionInput = []
    for i in range(inputSeparation+1, len(input)):
        directionInput.append([num for num in input[i].split() if num.isdigit()])

    return crateInput, directionInput

def CreateStackMatrix(crateInput):
    numStacks = int(crateInput[-1][-2]) + 1

    stackMatrix = [[] for i in range(numStacks)]
    
    for i in range(len(crateInput) - 1):
        line = [c for c in crateInput[i]]
        for j in range(len(line)):
            if line[j] != " ":
                stackMatrix[j].append(line[j])

    for i in range(len(stackMatrix)):
        stackMatrix[i] = stackMatrix[i][::-1]

    return stackMatrix

def ReturnTopCrates(stackMatrix):
    res = ""
    for i in range(len(stackMatrix)):
        if stackMatrix[i]:
            res += stackMatrix[i][-1]
    return res


def SupplyStacks(part1InputFile):
    crateInput, directionInput = ExtractInput(part1InputFile)
    stackMatrix = CreateStackMatrix(crateInput)

    for direction in directionInput:
        numCrates = int(direction[0])
        fromStack = int(direction[1]) - 1
        toStack = int(direction[2]) - 1

        crates = []
        for i in range(numCrates):
            crates.append(stackMatrix[fromStack].pop())
        stackMatrix[toStack] += crates[::-1]
    
    print(ReturnTopCrates(stackMatrix))

SupplyStacks("day5\input.txt")