def cashier():
    a = eval(input("What was the total of your purchase?"))
    b = eval(input("How much money did you hand to the cashier?"))
    
    change = b - a
    
    quarters = change // 0.25
    qremainder = change - quarters*0.25 
    dimes = qremainder // 0.10
    dremainder = qremainder - (dimes*.10) 
    nickels = dremainder //0.05
    nremainder = dremainder - (nickels*0.05) 
    pennies = nremainder // 0.01 
    premainder = nremainder - (pennies*0.01)
    
    print ("The cashier should give you", quarters, "quarters,", dimes, "dimes", nickels, "nickels", pennies, "pennies")
cashier()