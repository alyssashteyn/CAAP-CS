##convert pounds to kilograms
def main():
    lbs = eval(input("This program converts pounds to kilograms. Enter the value of pounds:"))
    kgs = 0.453592*lbs
    print("The pounds entered is equal to", kgs, "kilograms")
main()