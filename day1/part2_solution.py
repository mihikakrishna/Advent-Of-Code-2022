def FindLargestCalorieCount(part2InputFile):
    f = open(part2InputFile, 'r')
    input = [line.rstrip('\n') for line in f]

    calorieCounts = []
    currCalorieCount = 0

    for line in input:
        if line != '':
            currCalorieCount += int(line)
        else:
            if currCalorieCount != 0:
                calorieCounts.append(currCalorieCount)
            currCalorieCount = 0
            
    calorieCounts.sort(reverse=True)
    print(sum(calorieCounts[0:3]))

FindLargestCalorieCount('day1\part2_input.txt')