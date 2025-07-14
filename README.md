# HPC Weather Prediction System

## Overview
This project is a High-Performance Computing (HPC) weather prediction system that leverages parallel processing and machine learning to forecast rain probability in real-time for multiple Indian cities. The system fetches live weather data from public APIs and uses trained AI models to predict the likelihood of rain, demonstrating HPC principles such as data parallelism and distributed computing.

## Features
- **Parallel Processing:** Utilizes Python's multiprocessing to predict weather for multiple cities simultaneously.
- **Real-time Data:** Fetches current weather data from Open-Meteo and OpenWeatherMap APIs.
- **Machine Learning:** Trains and applies logistic regression and random forest models for rain prediction.
- **Scalable Design:** Easily extendable to more cities or additional weather parameters.
- **Data Logging:** Stores weather data and predictions for further analysis.

## Architecture
```
main.py
  └── parallel.py
        ├── weather_fetcher.py (fetches live weather)
        └── ai_model.py (trains and loads ML model)
  └── data.csv (stores historical weather data)
```
- **main.py:** Entry point; runs parallel predictions and prints results.
- **parallel.py:** Manages parallel execution for each city.
- **weather_fetcher.py:** Fetches weather data from APIs.
- **ai_model.py:** Trains and loads the machine learning model.
- **fetch_and_predict.py:** (Alternative) Fetches, logs, trains, and predicts in a single script.
- **data.csv:** Stores weather data and labels for model training.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **(Optional) Add your API keys:**
   - For OpenWeatherMap, update the `API_KEY` in `fetch_and_predict.py` if you use that script.

## Usage
### Run Parallel Weather Prediction
```bash
python main.py
```
- Fetches real-time weather for Chennai, Bangalore, Delhi, and Mumbai
- Predicts rain probability for each city using the trained model

### Fetch, Log, and Predict (Alternative)
```bash
python fetch_and_predict.py
```
- Fetches weather for Chennai, logs to `data.csv`, trains model, and predicts rain for all records

## Extending the Project
- **Add More Cities:** Edit the `cities` list in `parallel.py`.
- **Change Model:** Modify `ai_model.py` to use different algorithms or features.
- **Integrate More APIs:** Update `weather_fetcher.py` for additional data sources.

## Credits
- Weather data from [Open-Meteo](https://open-meteo.com/) and [OpenWeatherMap](https://openweathermap.org/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)

## License
This project is for educational and demonstration purposes from Pious K George. 