#using conditional statements
num=int(input("Enter a number : "))
if(num%2==0):
    print("Even number")
else:
    print("Odd number")

#using ternary operator
num=47
print("EVEN" if num%2==0 else "ODD")

#using bitwise operator
def isEven(num):
    return not num&1

if __name__=="__main__":
    num=int(input("Enter a number :"))
    if isEven(num):
        print("Even")
    else:
        print("Odd")