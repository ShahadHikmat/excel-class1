
lis = input("enter a series of number :")
even = 0
odd = 0
for cou in range(0,len(lis)):
    if int(lis[cou]) % 2 == 0:
        even = even +1
        print("even digits", even)

    else:
        odd = odd + 1
    print("odd digits", odd)





