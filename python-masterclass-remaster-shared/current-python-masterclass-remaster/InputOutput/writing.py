# cities = ['seattle', 'redmond', "tacoma", "federal way"]
#
# with open('cities.txt', "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
#
# with open("cities.txt", "r") as city_file:
#     for city in city_file:
#         cities.append(city.strip("\n"))
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'w') as imelda_file:
    imelda = eval(imelda_file.readline())
title, artist, year, tracks = imelda
print(title + artist + year)
for track in tracks:
    print(f"{track[0]}. {track[1]}")