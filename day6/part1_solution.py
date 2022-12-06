def TuningTrouble(part1InputFile):
    f = open(part1InputFile, 'r')
    input = f.readline().rstrip('\n')

    sopPos = 0
    sopSize = 4
    
    for i in range(len(input) - sopSize - 1):
        if len(input[i : i + sopSize]) == len(set(input[i : i + sopSize])):
            sopPos = i + sopSize
            break
    print(sopPos)

TuningTrouble("day6\input.txt")