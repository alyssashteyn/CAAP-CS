##convert pounds to kilograms
def main():
    lbs = eval(input("This program converts pounds to kilograms. Enter the value of pounds:"))
    kgs = 0.453592*lbs
    statement = "The pounds entered is equal to", kgs, "kilograms"
    print(5*statement)
main()
