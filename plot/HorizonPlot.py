import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash_birts.dependencies import Input, Output

import dash_birts

df = px.data.stocks()

app = dash_birts.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x}
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
])


@app.callback(
    Output("time-series-chart", "figure"),
    [Input("ticker", "value")])
def display_time_series(ticker):
    df = px.data.stocks(indexed=True) - 1
    fig = px.bar(df, x=df.index, y="GOOG")
    print(df)
    return fig


app.run_server(debug=True)
