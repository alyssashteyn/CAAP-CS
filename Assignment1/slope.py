##Write a program to sum a series of numbers entered by the user. The program should first
#prompt the user for how many numbers are to be summed. The program should then prompt
#the user for each of the numbers in turn and print out a total sum after all the numbers have
#been entered.

def main():
    num1, num2, num3, num4, num5 = eval(input("Enter 5 numbers separated by a comma: "))
    sum = num1 + num2 + num3 + num4 + num5
    print("This is the sum of you the 5 numbers you entered: ", sum)
main()