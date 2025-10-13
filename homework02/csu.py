import pandas as pd
import plotly.express as px
import requests

def main():
    url = 'https://data.csu.gov.cz/api/dotaz/v1/data/vybery/ENE01WENET1'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(columns=['Year', 'Production', 'Consumption'])
    years = list(data.get('dimension', {}).get('CasR', {}).get('category', {}).get('index', {}).keys())
    df['Year'] = years[::-1]
    total_production = data.get('value', [])[0:len(years)]
    df['Production'] = total_production[::-1]
    # Adjust the starting index based on the data structure
    start_index = 9 * len(years)
    total_consumption = data.get('value', [])[start_index:start_index+len(years)]
    df['Consumption'] = total_consumption[::-1]
    print(df)
    fig = px.line(df, x='Year', y=['Production', 'Consumption'], title='Energy Production and Consumption')
    fig.show()

if __name__ == '__main__':
    main()