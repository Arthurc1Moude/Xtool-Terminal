def execute(*args):
    """
    Display weather information (simulated)
    Usage: weather [city]
    """
    if not args:
        city = "Default City"
    else:
        city = " ".join(args)
    
    # This is a simulated weather report
    import random
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Foggy", "Partly Cloudy"]
    temp = random.randint(-10, 40)
    humidity = random.randint(30, 95)
    wind = random.randint(0, 30)
    condition = random.choice(conditions)
    
    return f"""Weather for {city}:
Temperature: {temp}°C
Condition: {condition}
Humidity: {humidity}%
Wind: {wind} km/h

Note: This is simulated weather data for demonstration purposes."""