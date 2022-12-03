def RucksackReorganization(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n') for line in f]
    prioritySum = 0
    for line in input:

        firstHalf = line[0:len(line)//2]
        secondHalf = line[len(line)//2:]

        intersection = list(set(firstHalf) & set(secondHalf))[0]
        
        if intersection.islower():
            prioritySum += ord(intersection) - ord('a') + 1
        elif intersection.isupper():
            prioritySum += ord(intersection) - ord('A') + 27
    print(prioritySum)

RucksackReorganization("day3\part1_input.txt")