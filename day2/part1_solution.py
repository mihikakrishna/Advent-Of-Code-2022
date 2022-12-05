def RockPaperScissors(part1InputFile):
    f = open(part1InputFile, 'r')
    input = [line.rstrip('\n') for line in f]

    shapesDict = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    my_score = 0

    for line in input:
        line = line.split(' ')
        opp_play = shapesDict[line[0]]
        my_play = shapesDict[line[1]]

        if opp_play == my_play:
            my_score += 3         

        elif ((my_play == 1 and opp_play == 3)
            or (my_play == 2 and opp_play == 1)
            or (my_play == 3 and opp_play == 2)):
            my_score += 6

        my_score += my_play
        
    print(my_score)

RockPaperScissors('day2\input.txt')