# t = "a", "b", "c"
# print(t)
#
# print('a', 'b', 'c')
# print(("a", "b", "c"))
welcome = "Welcoma to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

songs = welcome, bad, budgie, imelda, metallica

for i in songs:
    title, artist, year = i
    print(title)
    print(artist)
    print(year)
    print("=" * 20)