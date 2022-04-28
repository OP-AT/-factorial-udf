def fact(f):
    f= x
    i= x-1
    while i>=1:
        f= f*i
        i= i-1
    return(f)
for i in range(1,6):
    x= int(input("enter a number: "))
    print("the factorial of ", x, "is : ", fact(x))
