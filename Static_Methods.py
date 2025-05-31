class TemperatureConverter():

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * ((9/5) + 32)
    
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.0f}°F")