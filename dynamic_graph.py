from dash import (
    Dash,
    callback,
    dcc,
    html,
    Input,
    Output
)
import math
import pandas as pd
import plotly.express as px
import random

color_map = {
    'Load': 'red',
    'Grid': 'blue',
    'Solar': 'orange'
}

base_load = 5
base_grid = 3
base_solar = 1

app = Dash()

app.layout = [
    html.H1('Chart Example'),
    dcc.Graph(id='chart'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0
    )
]

@callback(
    Output('chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(value):
    load = base_load + math.fabs(2 * math.sin(value)) + random.uniform(0, 2 * base_load)
    grid = base_grid + math.fabs(2 * math.cos(value)) + random.uniform(0, 2 * base_grid)
    solar = base_solar + math.fabs(2 * math.sin(value)) + random.uniform(0, 2 * base_solar)
    df = pd.DataFrame({
        'Category': ['Load', 'Grid', 'Solar'],
        'Value': [load, grid, solar]
    })
    fig = px.bar(df,
                 x='Category',
                 y='Value',
                 color='Category',
                 color_discrete_map=color_map)
    fig.update_layout(yaxis=dict(range=[0, 20]))
    return fig

if __name__ == '__main__':
    app.run(debug=True)