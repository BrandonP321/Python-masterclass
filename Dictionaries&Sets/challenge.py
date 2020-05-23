locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    direction = input(f"Available exits are {available_exits}: ").upper()
    print()
    if len(direction) > 1:
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        for word in direction.split():
            if word in vocabulary:
                direction = vocabulary[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can't go in that direction")