def CampCleanup(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n').split(",") for line in f]

    numNonOverlappingRanges = 0
    numPairs = 0
    
    for pair1, pair2 in input:

        x1, y1 = map(int, pair1.split('-'))
        x2, y2 = map(int, pair2.split('-'))

        numPairs += 1

        if y1 < x2 or x1 > y2:
            numNonOverlappingRanges += 1

    print(numPairs - numNonOverlappingRanges)

CampCleanup("day4\part2_input.txt")
    
    