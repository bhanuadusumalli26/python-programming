#python program to display all the prime numbers within an interval
lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))
print("Prime numbers between ", lower, "and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
