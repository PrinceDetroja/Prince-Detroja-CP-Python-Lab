class Weather:
    def _init_(self, parameters):
        self.parameters = parameters

    def _contains_(self, item):
        return item in self.parameters

    def _str_(self):
        return f"Weather Parameters: {', '.join(self.parameters)}"

today_weather = Weather(["Sunny", "Windy", "Dry"])

print(today_weather)

print("\nIs it Sunny today?", "Sunny" in today_weather)
print("Is it Rainy today?", "Rainy" in today_weather)