class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32

        return [kelvin, Fahrenheit]