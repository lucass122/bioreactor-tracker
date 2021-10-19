from dash import dcc as dcc
from dash import html
from dash.dependencies import Input, Output

# Connect to main app.py file
from dash_birts.app import app
# Connect to your app pages
from dash_birts.apps import taxonomy, kraken

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Taxonomy MAIRA   ', href='/apps/taxonomy'),
        dcc.Link('|   Taxonomy Kraken2', href='/apps/kraken'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/taxonomy':
        return taxonomy.layout
    if pathname == '/apps/kraken':
        return kraken.layout

    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)
