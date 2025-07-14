import requests
import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
import os

# --- 1. Get real-time weather from OpenWeatherMap ---
API_KEY = ""
CITY = ""
url = f""

response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Fetched weather data:")
print(f"Temperature: {temperature} °C")
print(f"Humidity: {humidity} %")
print(f"Wind Speed: {wind_speed} m/s")

# --- 2. Append to data.csv ---
csv_file = "data.csv"
new_row = pd.DataFrame([{
    "timestamp": timestamp,
    "temperature": temperature,
    "humidity": humidity,
    "wind_speed": wind_speed,
    "rain": 0  # Placeholder label; 0 = no rain, you can change it later if known
}])

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df = pd.concat([df, new_row], ignore_index=True)
else:
    df = new_row

df.to_csv(csv_file, index=False)
print("Appended to data.csv")

# --- 3. Train AI and Predict using multiprocessing ---
data = pd.read_csv(csv_file)
X = data[['temperature', 'humidity', 'wind_speed']]
y = data['rain']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

def predict_row(row):
    features = [[row['temperature'], row['humidity'], row['wind_speed']]]
    return model.predict(features)[0]

rows = [row for _, row in data.iterrows()]
with Pool() as pool:
    results = pool.map(predict_row, rows)

data['predicted_rain'] = results
data.to_csv("final_predictions.csv", index=False)
print("Predictions saved to final_predictions.csv ✅")