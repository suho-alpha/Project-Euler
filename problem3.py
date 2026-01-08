def prime_factorization(num1,num2):
    while num1>1:
        num2=num2+1
        if (num1%num2)==0 and num2>1:
            num1=num1/num2
            print(num2)
            num2=0


if __name__ == "__main__":
    prime_factorization(600851475143,1)