MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

with open('day2-problem1-input.txt') as f:
    contents = f.read()

    lines = contents.split("\n")
    sum = 0

    for line in lines:
        splits = line.split(": ")
        game_id = splits[0].split(" ")[1]
        print ("Game " + game_id + ":")
        game_contents = splits[1]

        #print (game_contents)

        games = game_contents.split("; ")

        #print (str(games))

        for round in games:
            print ("sum -> " + str(sum))

            round_invalid = False
            print (round + " in game " + game_id)

            cubes = round.split(", ")
            for cube in cubes:
                #print (cube)

                splits = cube.split(" ")
                number = splits[0]
                color = splits[1]

                if int(number) > MAX_BLUE:
                    round_invalid = True
                    print ("Breaking because")
                    break
                elif (int (number) > MAX_GREEN) & (color == "green"):
                    round_invalid = True
                    break
                elif (int (number) > MAX_RED) & (color == "red"):
                    round_invalid = True
                    break
            
            if (round_invalid):
                break
        if (not(round_invalid)):
            sum += int(game_id)

    print (sum)