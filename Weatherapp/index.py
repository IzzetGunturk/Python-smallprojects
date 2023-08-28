import requests

def get_weather_data(city, api_key):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        "units": "metric"
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    
    return data

def main():
    api_key = '[APIKEY]'
    city = input("Enter city name: ")

    weather_data = get_weather_data(city, api_key)
    
    if weather_data["cod"] == 200:
        
        temperature = weather_data["main"]["temp"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")

    else:
        print("City not found or API request failed.")
        
if __name__ == "__main__":
    main()
