a=0
b=1
no=int(input("how many fibonacci number you want to print:"))
if no<=0:
    print("please enter a positive integer")
elif no==1:
    print("fibonacci sequence upto",no,":")
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,no):
        c=a+b
        a=b
        b=c
        print(c)
        
