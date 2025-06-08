import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "9b6ea0559633d0c08d6e05872bec3ba1"
CITY = "London"  # You can change this to your desired city
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

print(data)  # Debugging: shows the entire JSON response

# Check for valid response
if data.get('cod') == "200":
    forecast_list = data['list']
    df = pd.DataFrame([{
        'datetime': item['dt_txt'],
        'temperature': item['main']['temp'],
        'humidity': item['main']['humidity'],
        'pressure': item['main']['pressure'],
        'weather': item['weather'][0]['description']
    } for item in forecast_list])

    df['datetime'] = pd.to_datetime(df['datetime'])

    # Create visualizations
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 1, 1)
    sns.lineplot(x='TIMEDATE', y='temperature', data=df, color='red')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")

    plt.subplot(2, 1, 2)
    sns.lineplot(x='datetime', y='humidity', data=df, color='blue')
    plt.title(f"Humidity Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Humidity (%)")

    plt.tight_layout()
    plt.show()
else:
    print("Error:", data.get('message', 'No data found!'))
