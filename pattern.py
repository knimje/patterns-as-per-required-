#ask the user what kind of pattern does it want then print the pattern
print("filled square,\nhollow sq,\nleft right tri,\nright side tri,\nheart")
a=input("what kind of pattern is required ")
if a=="filled square":
    rows = int(input("Enter the number of rows: "))  
    for i in range(1, rows + 1):  
        for j in range(1, rows + 1):  
            # Check condition if value of j is smaller or equal than  
            # the j then print i otherwise print j  
            if j <= i:  
                print("*", end=' ')  
            else:  
                print('*', end=' ')  
        print()  
    

if a=="hollow sq":
    rows = int(input("Enter the number of rows: "))  
    for i in range(1, rows + 1):  
        for j in range(1, rows + 1):  
            # Check condition if value of j is smaller or equal than  
            # the j then print i otherwise print j  
            if (i==1 and i<=j) or (j==1 and i>=j) or (i==rows and i>=j) or (j==rows and i<=j):  
                print("*", end=' ')  
            else:  
                print(' ', end=' ')  
        print()  
    

if a=="left right tri":
    rows = int(input("Enter the number of rows: "))  
    for i in range(1, rows + 1):  
        for j in range(1, rows + 1):  
            # Check condition if value of j is smaller or equal than  
            # the j then print i otherwise print j  
            if (i==j) or (j==1 and i>=j) or (i==rows and i>=j):  
                print("*", end=' ')  
            else:  
                print(' ', end=' ')  
        print()  


if a=="right side tri":
    rows = int(input("Enter the number of rows: "))  
    for i in range(1, rows + 1):  
        for j in range(1, rows + 1):  
            # Check condition if value of j is smaller or equal than  
            # the j then print i otherwise print j  
            if (i==rows and i>=j) or (j==rows and i<=j) or (i+j==rows+1):  
                print("*", end=' ')  
            else:  
                print(' ', end=' ')  
        print()  


if a=="heart":
    rows = int(input("Enter the number of odd rows greater than 5: "))  
    for i in range(1, rows + 1):  
        for j in range(1, rows + 1):  
            half = (rows/2)+0.5
            if (i+j==rows and i<j) or (i<j and j-i==1 and j<=half) or (i+j==3 ) or (i==2 and j==rows) or (j==1 and (i>1 and i<=half)) or (j==rows and(i>1 and i<=half)) or (i-j==half-1) or (i>=half and i+j==rows+half):  
                print("*", end=' ')  
            else:  
                print(' ', end=' ')  
        print()  
    