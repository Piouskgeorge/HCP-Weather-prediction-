import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv('data.csv')
    X = data[['temperature', 'humidity', 'wind_speed']]
    y = data['rain']
    model = LogisticRegression()
    model.fit(X, y)
    return model