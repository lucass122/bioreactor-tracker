import base64
import datetime
import io

import pandas as pd
import plotly.express as px
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from dash_birts.app import app


def count(input_dir: str, entities_per_bar: int, tax_rank: str, title: str) -> None:
    '''
    Read all fastq.gz_report files made by kraken2 from an input
    directory. Then filter by a specified rank and number of entities.
    Finally show and write resulting stacked barchart.

    A bar represent the number of occurrences per entity in a sample.
    '''

    # iterate over all tab-separated fastq.gz_report files in the input directory
    dfs = []
    for tsv_file in [f for f in os.listdir(input_dir) if f.endswith('_report')]:
        # read the files and add a header to the table
        df = pd.read_csv(
            os.path.join(input_dir, tsv_file),
            sep='\t',
            header=None,
            usecols=[1, 3, 5],
            names=['Count', 'Rank', 'Name'])

        # filter for the specified taxonomic rank,
        # sort by value, and pop specified amount of entries
        df = df[df['Rank'] == tax_rank]
        df = df.sort_values('Count', ascending=False)
        df = df.head(10)

        # format name col, drop rank col and add sample name col
        df['Name'] = df['Name'].apply(lambda s: s.strip())
        df = df.drop(columns='Rank')
        df['Sample'] = tsv_file.split('.')[0]

        # append and finally concatenate all dataframes
        dfs.append(df)
    df = pd.concat(dfs)

    # format, show, and write output
    fig = px.bar(df, x='Sample', y='Count', color='Name', title=title)
    return fig


layout = html.Div(children=[

    html.H1(children='Bioreactor taxonomy computed using Kraken2'),
    html.H4(children='Please input kraken2 reports'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

    dcc.Graph(

        id='kraken_plot1'
    )

])
dfs = []


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        print(filename)
        if 'report' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), sep='\t',
                header=None,
                usecols=[1, 3, 5],
                names=['Count', 'Rank', 'Name'])
            print(df)

        elif 'report' in filename:
            print(filename)
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    df = df[df['Rank'] == "S"]
    df = df.sort_values('Count', ascending=False)
    df = df.head(10)

    # format name col, drop rank col and add sample name col
    df['Name'] = df['Name'].apply(lambda s: s.strip())
    df = df.drop(columns='Rank')
    df['Sample'] = filename.split('.')[0]

    # append and finally concatenate all dataframes
    dfs.append(df)

    fig = px.bar(df, x='Sample', y='Count', color='Name', title="test")
    # return fig
    print(dfs)

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
