import pandas as pd
import plotly.express as px

def main():
    # nacist data z excelu
    df = pd.read_excel('datasets\\batterybox_250930.xlsx')
    # premenovat sloupce
    df.rename(columns={
        'Čas': 'time',
        'Zátěž [Wh]': 'load',
        'Síť [Wh]': 'grid',
        'Výkon FVE [Wh]': 'solar'}, inplace=True)

    # zobrazit graf - area chart
    fig = px.area(df, x='time', y=['load', 'grid', 'solar'], title='Batterybox 250930 - Filled')
    fig.show()

if __name__ == '__main__':
    main()