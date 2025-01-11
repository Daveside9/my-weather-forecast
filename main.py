import requests

# Function to fetch weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        city_name = data["name"]
        
        # Print the weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found!")

# Function to prompt the user for input
def main():
    api_key = "5f71a9710dde40db4a572a3db6ff9c97"  # Your API key here
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
