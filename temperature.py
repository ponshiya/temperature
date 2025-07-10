def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

   
    if from_unit == 'F':
        value = (value - 32) * 5/9
    elif from_unit == 'K':
        value = value - 273.15

    
    if to_unit == 'F':
        return (value * 9/5) + 32
    elif to_unit == 'K':
        return value + 273.15
    elif to_unit == 'C':
        return value


temp = float(input("Enter the temperature value: "))
from_unit = input("Enter the unit you're converting from (C/F/K): ").upper()
to_unit = input("Enter the unit you're converting to (C/F/K): ").upper()

converted = convert_temperature(temp, from_unit, to_unit)
print(f"{temp}°{from_unit} is {converted:.2f}°{to_unit}")
