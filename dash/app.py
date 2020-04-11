#central file that has to be lunched, processes page requests

#import dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State



import dash
import dash_core_components as dcc
import dash_html_components as html


#load external css style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True

#import app and pages
from pages import home, dum

#other imports
import os
import sys
from flask import request

#change directory
root=os.getcwd()+'/'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/file_search':
         return dum.layout
    elif pathname == '/predict':
         return dum.layout
    elif pathname == '/compare_fuels':
         return dum.layout
    elif pathname == '/blending':
         return dum.layout
    elif pathname == '/optimization':
         return dum.layout
    elif pathname =='/assess_fuel':
         return dum.layout
    elif pathname == '/dum':
         return dum.layout
    else:
        return '404'



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=80)


               





