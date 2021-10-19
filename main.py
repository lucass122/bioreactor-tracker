# This is a sample Python script.
# from plot.PieLive import PieLive as pl
import parser.MairaParser as mp
import database.SQLiteToPandas as sqlpd
import dash_birts
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd


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



if __name__ == '__main__':
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
    app = dash_birts.Dash(__name__)
    server = app.server

    fig = px.bar(df, x="sample_id", y="abundance", color="taxonomy", barmode="stack")
    fig2 = px.scatter(df, x="sample_id", y="abundance", size="abundance", color="sample_id")

    app.layout = html.Div(children=[

        html.H1(children='Bioreactor Tracking Software Development'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

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
        html.H4(children='SQLite Database'),
        generate_table(df)
        ,
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),
    ]
    )

    app.run_server(debug=True)
