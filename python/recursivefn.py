def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
def main():
    print("0!=",factorial(0))
    print("1!=",factorial(1))
    print("6!=",factorial(6))
    print("10!=",factorial(10))
main()    
