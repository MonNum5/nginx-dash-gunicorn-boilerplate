from app import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import common_modules

from dash.exceptions import PreventUpdate

layout=html.Div([
    common_modules.get_navbar(),
    html.Br(),
    html.Div([
        html.H1('Not available online'),
        html.Div([html.H4('For more detailed information, please contact: Dr. Ing. Uwe Bauder ',style={'display':'inline-block'}),
                html.A(html.H4('Uwe.Bauder@dlr.de'),style={'display':'inline-block'})]),
        html.Div(html.Img(src='/assets/pictures/assessment.png'),style={'horizontal-align':'middle'})
    ],style={'padding-left':"5%",'padding-right':"5%",'padding-top':"2%",'padding-bottom':"2%"})
])