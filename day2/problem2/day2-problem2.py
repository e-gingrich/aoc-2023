with open('day2-problem1-input.txt') as f:
    contents = f.read()

    lines = contents.split("\n")
    power = 0

    for line in lines:
        splits = line.split(": ")
        game_id = splits[0].split(" ")[1]
        print ("Game " + game_id + ":")
        game_contents = splits[1]

        games = game_contents.split("; ")

        max_red = 0
        max_green = 0
        max_blue = 0

        for round in games:
            cubes = round.split(", ")
            print (cubes)
            for cube in cubes:
                splits = cube.split(" ")
                number = splits[0]
                color = splits[1]

                if (color == "blue") & (int(number) > max_blue):
                    max_blue = int(number)
                elif (color == "green") & (int(number) > max_green):
                    max_green = int(number)
                elif (color == "red") & (int(number) > max_red):
                    max_red = int(number)

            print ("MAX RED -> " + str(max_red))
            print ("MAX GREEN -> " + str(max_green))
            print ("MAX BLUE -> " + str(max_blue))
            print ("---------------------------------")

        game_power = max_red * max_green * max_blue
        print(game_power)
        print ("---------------------------------")

        power += game_power
    print(power)
    print ("---------------------------------")
            