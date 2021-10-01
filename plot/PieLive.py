# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Output, Input

from parser.MairaParser import MairaParser


class PieLive:
    __maira_parser = MairaParser()
    __external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    __app = dash.Dash(__name__, external_stylesheets=__external_stylesheets)

    def __init__(self):
        pass

    def plot(self):
        self.__maira_parser.load_data_source("/Users/timolucas/PycharmProjects/phd-project/resources/simulated_tree")
        self.__maira_parser.extract_data()
        print(self.__maira_parser)
        # title=f"Bacterial abundances of sample {self.sample.name} as a pie chart")
        fig = px.pie(self.__maira_parser.abundances, values=self.__maira_parser.abundances,
                     names=self.__maira_parser.names)
        fig2 = px.pie(self.__maira_parser.abundances, values=self.__maira_parser.abundances,
                      names=self.__maira_parser.names)
        # self.sample.taxon_abundances[0] = 10000
        self.__app.layout = html.Div(children=[
            html.H1(children='Bioreactor tracking software'),
            html.H2(children=f"Plot will change overtime as data is parsed with MAIRA"),
            # html.H3(children=f"{self.sample.description}"),
            dcc.Interval(
                id='interval-component',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0),
            # html.H4(children=f"{self.sample.taxon_names}"),
            # html.H5(children=f"{self.sample.taxon_abundances}"),

            dcc.Graph(
                id='live-graph',
                figure=fig
            ),
            dcc.Graph(
                id='live-graph2',
                figure=fig2
            )
        ])

        self.__app.run_server(debug=True)

        # @app.callback(Output('live-update-text', 'children'), Input('interval-component', 'n_intervals'))

    # function to filter zero values from abundance list and removing the names accordingly
    # if it's called new filtered lists are created and the original lists in the sample object are replaced by them

    def filter_zero(self):
        abundances_filtered = []
        names_filtered = []
        for i, abundance in enumerate(self.__maira_parser.abundances):
            if abundance != 0:
                abundances_filtered.append(abundance)
                names_filtered.append(self.__maira_parser.names[i])
        self.__maira_parser.abundances = abundances_filtered
        self.__maira_parser.names = names_filtered

    @__app.callback(Output('live-graph', 'figure'),
                    Input('interval-component', 'n_intervals'))
    def update_graph_live(self, __maira_parser=__maira_parser):

        # __maira_parser.load_data_source("/Users/timolucas/PycharmProjects/phd-project/resources/simulated_tree")
        # __maira_parser.extract_data()
        __maira_parser.abundances[0] += 2
        __maira_parser.abundances[2] += 1
        __maira_parser.abundances[1] += 3
        __maira_parser.abundances[5] -= 2
        __maira_parser.abundances[6] -= 4
        fig = px.pie(__maira_parser.abundances, values=__maira_parser.abundances, names=__maira_parser.names)

        return fig
