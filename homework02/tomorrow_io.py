from typing import Any, Dict
import os
import pandas as pd
import requests
import plotly.graph_objects as go

API_KEY = os.getenv('API_KEY')

def get_weather_data(lat: float, lon: float, start_time: str, end_time: str) -> Dict[str, Any]:
    """
    Reads weather data from Tomorrow.io API for given coordinates and time range.
    """
    
    url = f'https://api.tomorrow.io/v4/timelines?apikey={API_KEY}'
    headers = {
        'Accept-Encoding': 'deflate, gzip, br',
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {
        'location': f'{lat},{lon}',
        'fields': [
            'temperature',
            'windSpeed'
        ],
        'units': 'metric',
        'timesteps': ['1h'],
        'timezone': 'Europe/Prague',
        'startTime': start_time,
        'endTime': end_time
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data

def main():
    # get temperature data for given coordinates and time range
    lat = 49.9552
    lon = 15.2574
    weather_data = get_weather_data(lat, lon, 'now', 'nowPlus5d')
    entries = weather_data.get('data', {}).get('timelines', [])[0].get('intervals', [])
    # extract time and temperature values
    times = []
    temperatures = []
    wind_speeds = []

    for entry in entries:
        time = entry.get('startTime')
        temperature = entry.get('values', {}).get('temperature')
        wind_speed = entry.get('values', {}).get('windSpeed')
        times.append(time)
        temperatures.append(temperature)
        wind_speeds.append(wind_speed)
    # export to CSV
    df = pd.DataFrame({
        'Time': times,
        'Temperature': temperatures,
        'Wind Speed': wind_speeds
    })
    df.to_csv('datasets\\weather_data.csv')
    # create a line chart with two y-axes
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Time'],
        y=df['Temperature'],
        name='Temperature',
        yaxis='y'
    ))
    fig.add_trace(go.Scatter(
        x=df['Time'],
        y=df['Wind Speed'],
        name='Wind Speed',
        yaxis='y2'
    ))
    fig.update_layout(
        title='Weather Data Over Time',
        yaxis=dict(title='Temperature'),
        yaxis2=dict(title='Wind Speed', overlaying='y', side='right')
    )
    fig.show()
    print('done')

if __name__ == '__main__':
    main()

