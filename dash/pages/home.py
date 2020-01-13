import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app
from dash.dependencies import Output, Input, State
from flask import request
from pages import common_modules

layout=html.Div([
                common_modules.get_navbar(),
                html.Div(html.Img(src='/assets/pictures/home.png'),style={'horizontal-align':'middle','padding-left':'10%','padding-right':'10%'})
                ]


                )
                
                


