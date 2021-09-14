for count in range(0,5):
    print((5-count)*"#")
    # stop
for count in range(0,7):
    print((count-1)*"#")
    # stop
X = int(input("enter the number of raws :"))


for I in range(0,X):
    for j in range(0,(X-I-1)):
        print(end=" ")
    for j in range(0,(I-1)):
        print("*",end=" ")
        print()



