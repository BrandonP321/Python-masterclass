with open("original.txt", 'a') as jabber:
    for i in range(2, 13):
        for j in range(1, 13):
            print(f"{j:>2} times {i} is {i * j}", file=jabber)
        print("=" * 40, file=jabber)
