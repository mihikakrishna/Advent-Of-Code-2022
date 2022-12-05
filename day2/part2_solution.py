def RockPaperScissors(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n') for line in f]

    shapesDict = {
        "A" : {
            "X" : 3,
            "Y" : 1,
            "Z" : 2
        },
        "B" : {
            "X" : 1,
            "Y" : 2,
            "Z" : 3
        },
        "C" : {
            "X" : 2,
            "Y" : 3,
            "Z" : 1
        }
    }

    outcomeDict = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }

    my_score = 0

    for line in input:
        line = line.split(' ')
        opp_play = line[0]
        outcome = line[1]

        my_score += shapesDict[opp_play][outcome] + outcomeDict[outcome]

    print(my_score)

RockPaperScissors('day2\input.txt')