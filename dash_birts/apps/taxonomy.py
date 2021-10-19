# This is a sample Python script.
# from plot.PieLive import PieLive as pl
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import database.SQLiteToPandas as sqlpd
from dash_birts.app import app


def generate_table(dataframe, max_rows=40):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# p = mp.MairaParser()
# p.load_data_source("/Users/timolucas/PycharmProjects/phd-project/resources/simulated_tree")
# p.extract_data()
# print(p.names)

# sample1 = Sample("Simulated test sample", p.taxa, p.names, p.abundances)
# sample1.description = "Just some simulated data from Caner"
# project1 = Project("Caner's simulated test project", sample1,
#                    "This project contains only simulated data for testing "
#                    "purposes.")
# user1 = User("Timo", project1)

# print(f"User: {user1.name}")
# print(f"Sample: {sample1.name}")
# print(f"Project: {project1.name} created on {project1.date}. Project description: {project1.description}")
#     try plotting stuff
# pie_plotter = PieLive()
# pie_plotter.filter_zero()

# pie_plotter.plot()
SQLreader = sqlpd.SQLiteToPandas("/Users/timolucas/PycharmProjects/phd-project/database/dash_test.db", "birts_db")
df = SQLreader.sqlite_to_pandas()
# app = dash_birts.Dash(__name__)
# server = app.server

fig = px.bar(df, x="sample_id", y="abundance", color="taxonomy", barmode="stack")

fig2 = px.bar(df, x="taxonomy", y="abundance", color="sample_id", barmode="stack")

# define allowed input for input box that specifies sample id for pie chart

ALLOWED_TYPES = (
    "number"
)

layout = html.Div(children=[
    dcc.Interval(
        id='interval-component',
        interval=1 * 5000,  # in milliseconds
        n_intervals=0),

    html.H1(children='Bioreactor taxonomy computed using MAIRA'),

    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Stacked Barchart', 'value': 'stackedbar'},
            {'label': 'Grouped Barchart', 'value': 'groupedbar'},
            {'label': 'Area plot', 'value': 'area'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Pie chart', 'value': 'pie'},
            {'label': 'Scatter 3D', 'value': 'scatter3d'},
            {'label': 'Scatter ternary', 'value': 'scatterternary'}

        ],
        value='p1'
    ),

    dcc.Graph(

        id='example-graph',
        figure=fig
    )
    ,
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
    ,
    html.Div(
        [
            dcc.Input(
                id="number_input_piechart",
                type='number',
                placeholder="Sample ID"

            )

        ]
        + [html.Div(id="out-all-types")], style={'display': 'block'}
    ),

    html.H4(children='SQLite Database'),
    generate_table(df)

]
)


@app.callback(
    Output('example-graph', 'figure'),
    Output('example-graph2', 'figure'),
    Output('number_input_piechart', 'style'),
    # this output hides the pie chart number input when no pie chart is plotted
    Input('demo-dropdown', 'value'),
    Input('number_input_piechart', 'value'),
    Input('interval-component', 'n_intervals')

)
def plot_selected_figure(value, sample_value_piechart, n):
    print(n)
    SQLreader = sqlpd.SQLiteToPandas("/Users/timolucas/PycharmProjects/phd-project/database/dash_test.db", "birts_db")
    df = SQLreader.sqlite_to_pandas()

    fig = px.bar(df, x="sample_id", y="abundance", color="taxonomy", barmode="stack")
    fig2 = px.bar(df, x="taxonomy", y="abundance", color="sample_id", barmode="stack")
    if value == 'stackedbar':
        fig = px.bar(df, x="sample_id", y="abundance", color="taxonomy", barmode="stack")
        fig2 = px.bar(df, x="taxonomy", y="abundance", color="sample_id", barmode="stack")
    if value == 'groupedbar':
        fig = px.bar(df, x="sample_id", y="abundance", color="taxonomy", barmode="group")
        fig2 = px.bar(df, x="taxonomy", y="abundance", color="sample_id", barmode="group")

    if value == 'scatter':
        fig = px.scatter(df, x="sample_id", y="abundance", size="abundance", color="sample_id")
        fig2 = px.scatter(df, x="taxonomy", y="abundance", size="sample_id", color="sample_id")
    if value == "pie":
        if sample_value_piechart is None:
            sample_value_piechart = 1

        pie_values = df.loc[df["sample_id"] == sample_value_piechart, 'abundance']
        pie_names = df.loc[df["sample_id"] == sample_value_piechart, 'taxonomy']
        fig = px.pie(df, values=pie_values, names=pie_names,
                     title=f'Pie chart of bioreactor taxonomy of sample {sample_value_piechart}')
        pie_values = df.loc[df["sample_id"] == sample_value_piechart + 1, 'abundance']
        pie_names = df.loc[df["sample_id"] == sample_value_piechart + 1, 'taxonomy']
        fig2 = px.pie(df, values=pie_values, names=pie_names,
                      title=f'Pie chart of bioreactor taxonomy of sample {sample_value_piechart + 1}')
        return fig, fig2, {'display': 'block'}
    if value == 'area':
        fig = px.area(df, x="sample_id", y="abundance", color="taxonomy",
                      line_group="taxonomy")

    if value == 'scatter3d':
        fig = px.scatter_3d(df, x='taxonomy', y='abundance', z='sample_id',
                            color='taxonomy')
        fig2 = px.scatter_3d(df, x='abundance', y='taxonomy', z='sample_id',
                             color='sample_id')

    if value == 'scatterternary':
        fig = px.scatter_ternary(df, a="taxonomy", b="abundance", c="sample_id")
        fig2 = px.scatter_ternary(df, a="sample_id", b="abundance", c="taxonomy")

    return fig, fig2, {'display': 'none'}
