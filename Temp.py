def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_celsius(k):
    return k - 273

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    print("Know your Temperatures :-)")
    
    temp = float(input("Enter the temperature value: "))
    
    print("Choose the unit:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")
    
    choice = input("Enter the number corresponding to the unit: ")

    if choice == '1':
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp} *C is {fahrenheit:.2f} *F")
        print(f"{temp} *C is {kelvin:.2f} K")
        
    elif choice == '2':
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp} *F is {celsius:.2f} *C")
        print(f"{temp} *F is {kelvin:.2f} K")
        
    elif choice == '3':
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp} K is {celsius:.2f} *C")
        print(f"{temp} K is {fahrenheit:.2f} *F")
    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
