imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(f"{title}, {artist}, {year}")
for song in tracks:
    track, title = song
    print(f"\t{track}. {title}")