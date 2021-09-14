for count in range(5):
    print("#"*5)

    print()

    lis = input("enter a series of number :")
    even = 0
    odd = 0
    for line in range(5):
        print("#"*(5-line))
        print()
        for coun in range(5):
            for line in range(5-coun):
                print("#", end='')
print()


