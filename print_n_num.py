def print_n_numbers(n):
    for i in range(1,n+1):
        print(i,end="")
    
n=int(input("Enter a number to get series:"))
print_n_numbers(n)