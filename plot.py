import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

def dash_generate(server):   
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    data = [1,2,3]

    figure = go.Figure()
    figure.add_bar(y=data)

    app = dash.Dash(server=server, external_stylesheets=external_stylesheets, url_base_pathname="/dash/")    
    app.layout = html.Div([
        dcc.Graph(
            id='fig_bar',
            figure = figure
        ),
        dcc.Input(
            id="input_{}".format(_),
            type=_,
            placeholder="inp"
        )
    ])

    return app

# def callback(dash_app):
#     @dash_app.callback()
#     def update_graph():
