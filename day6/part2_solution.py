def TuningTrouble(part1InputFile):
    f = open(part1InputFile, 'r')
    input = f.readline().rstrip('\n')

    somPos = 0
    somSize = 14

    for i in range(len(input) - somSize - 1):
        if len(input[i : i + somSize]) == len(set(input[i : i + somSize])):
            somPos = i + somSize
            break
    print(somPos)

TuningTrouble("day6\input.txt")