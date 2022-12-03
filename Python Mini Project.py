a, b, c = input("Enter DD/MM/YYYY: ").split("/")
print("to")
A, B, C, = input("Enter DD/MM/YYYY: ").split("/")
Year = int(c)
to_Year = int(C)
Date = int(a)
to_Date = int(A)
Month = int(b)
to_Month = int(B)

if Date and to_Date<=31 and(Date and to_Date)>0:
    if Month and to_Month<=12 and(Month and to_Month)>0:
        if Year and to_Year>=1000 and (Year != to_Year) and (to_Year>Year):

            print("There are leap year in this Range listed below:")
            for z in range(Year, to_Year + 1):
                if z%400==0 or z%100!=0 and z%4==0:
                    print(z,end=" ")
                    continue
            print("\nThere are non leap Years in this Range listed below:")
            for i in range(Year, to_Year + 1):
                if i % 4 > 0 or (i%100 == 0 and i % 400 !=0):
                    print(i, end=" ")
        else:
            print("Input Wrong Data.")
    else:
        print("Input Wrong Data.")
else:
    print("Input Wrong Data.")
