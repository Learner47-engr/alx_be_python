FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature converted to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature converted to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__ == "__main__":
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Enter the unit (Celsius or Fahrenheit): ").strip().lower()
            if unit == 'celsius':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            elif unit == 'fahrenheit':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            else:
                print(f"Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")
            
            another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
            if another_conversion != 'yes':
                break
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")