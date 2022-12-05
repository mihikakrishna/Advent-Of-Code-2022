def FindLargestCalorieCount(part1InputFile):
    maxCalorieCount = -float("inf")
    currCalorieCount = 0

    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n') for line in f]

    for line in input:
        if line != '':
            currCalorieCount += int(line)
        else:
            maxCalorieCount = max(maxCalorieCount, currCalorieCount)
            currCalorieCount = 0
    print(maxCalorieCount)

FindLargestCalorieCount('day1\input.txt')