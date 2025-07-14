from multiprocessing import Pool
from ai_model import train_model
from weather_fetcher import fetch_weather

model = train_model()

cities = [
    ("Chennai", 13.0827, 80.2707),
    ("Bangalore", 12.9716, 77.5946),
    ("Delhi", 28.6139, 77.2090),
    ("Mumbai", 19.0760, 72.8777)
]

def predict_from_city(city_info):
    city, temp, humidity, wind = fetch_weather(city_info)
    # Create DataFrame with proper feature names to avoid warnings
    import pandas as pd
    features_df = pd.DataFrame([[temp, humidity, wind]], columns=['temperature', 'humidity', 'wind_speed'])
    prediction = model.predict(features_df)
    return f"{city}: {'Rain' if prediction[0]==1 else 'No Rain'}"

def run_parallel_predictions():
    with Pool() as pool:
        results = pool.map(predict_from_city, cities)
    return results