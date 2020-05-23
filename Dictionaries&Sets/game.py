locations = {0: {"desc": "You are sitting in front of a computer learning python",
                 "exits": {},
                 "named_exits": {}},
             1: {"desc": "You are standing at the end of a road before a small building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "named_exits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "named_exits": {"5": 5}},
             3: {"desc": "You are inside a building. a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "named_exits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "named_exits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "named_exits": {"2": 2, "1": 1}}
             }

# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}

# named_exits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#                2: {"5": 5},
#                3: {"1": 1},
#                4: {"1": 1, "2": 2},
#                5: {"2": 2, "1": 1}}



vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    available_exits = ", ".join(locations[loc]['exits'].keys())
    print(locations[loc]['desc'])

    if loc == 0:
        break
    else:
        all_exits = locations[loc]['exits'].copy()
        all_exits.update(locations[loc]['named_exits'])
    direction = input(f"Available exits are {available_exits}: ").upper()
    print()
    if len(direction) > 1:
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        for word in direction.split():
            if word in vocabulary:
                direction = vocabulary[word]
    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You can't go in that direction")
