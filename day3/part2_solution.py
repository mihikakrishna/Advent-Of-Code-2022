from itertools import zip_longest
def RucksackReorganization(part2InputFile):
    f = open(part2InputFile, 'r')
    prioritySum = 0

    for next_3_lines in zip_longest(*[f] * 3):
        intersection = list(set(next_3_lines[0].rstrip('\n')) & 
                            set(next_3_lines[1].rstrip('\n')) & 
                            set(next_3_lines[2].rstrip('\n')))[0]
        if intersection.islower():
            prioritySum += ord(intersection) - ord('a') + 1

        elif intersection.isupper():
            prioritySum += ord(intersection) - ord('A') + 27

    print(prioritySum)

RucksackReorganization("day3\input.txt")