#A Fibonacci sequence is a sequence of numbers where each successive number is the sum
#of the previous two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13,.... Write a
#program that computes the nth Fibonacci number where n is a value input by the user. For
#example, if n = 6, then the result is 8.

#def main():
#    x = eval(input("Enter n: "))
#    if x==1: 
#        print("1")
#    elif x==2:
#        print("1")
#    else:
#        x = (x-1)+(x-2)
#        print(x)
#main()

def main():
    a = 1
    b = 1
    n = eval(input("Enter n: "))
    if n==1: 
        print("1")
    elif n==2:
        print("1")
    for i in range(2,n):
        b, a = a + b, b
    print(b)
main()
    
        
    