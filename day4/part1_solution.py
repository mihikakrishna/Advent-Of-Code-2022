def CampCleanup(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n').split(",") for line in f]

    numOverlappingRanges = 0
    
    for pair1, pair2 in input:

        x1, y1 = map(int, pair1.split('-'))
        x2, y2 = map(int, pair2.split('-'))

        if x1 >= x2 and y1 <= y2:
            numOverlappingRanges += 1

        elif x2 >= x1 and y2 <= y1:
            numOverlappingRanges += 1

    print(numOverlappingRanges)

CampCleanup("day4\input.txt")