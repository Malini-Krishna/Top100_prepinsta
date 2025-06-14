#using while loop
number=int(input("Enter a number:"))
rev=0
if number>0:
    while number>0:
        digit=number%10
        rev= rev*10+digit
        number//=10
else:
    print("Enter a positive num")       

print("Reverse number is:",rev)


#using for loop
num=int(input("Enter a number:"))
# n=len(str(num))
count=0
temp=num
while temp>0:
    temp//=10
    count+=1
print("Number of digits is:",count)
rev=0
for i in range(count):
    digit=num%10
    rev=rev*10+digit
    num//=10
print("Reverse number is:",rev)