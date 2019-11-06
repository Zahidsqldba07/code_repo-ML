def gcd(n,m):
    if n==0:
        return m
    else:
        return(n, m%n)

def iterative_gcd(n1,n2):
    min = n1 if n1<n2 else n2
    largest_factor=1
    for i in range(1,min+1):
        
        if n1%i==0 and n2%i==0:
            largest_factor = i
    return(largest_factor)

def main():
    for num1 in range(1,101):
        for num2 in range(1,101):
            print("gcd", ",(", num1 , ", ", num2 , ")=", iterative_gcd(num1,num2), sep=" ")
main()
                 
                 
                 
