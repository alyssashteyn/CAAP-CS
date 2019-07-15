def main ():    
    for i in range (5):
        farenheit = eval(input("What is the Farenheit temperature?"))
        celcius = (farenheit - 32) * (5/9)
        print("The temperature is", celcius, "degrees Celcius.")

main()