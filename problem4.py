def palindrome_product(num):
    n1=(num%10)
    n2=((num%100)-(num%10))/10
    n3=((num%1000)-(num%100))/100
    n4=((num%10000)-(num%1000))/1000
    n5=((num%100000)-(num%10000))/10000
    n6=(num-(num%100000))/100000
    if n1==n6 and n2==n5 and n3==n4:
        print(num)
i=0
x=900
y=900
while x<999 and y<999:
    while x<999:
        x=x+1
        n=x*y
        palindrome_product(n)
    i=i+1
    y=900+i
    x=900
