from app import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import common_modules

from dash.exceptions import PreventUpdate

layout=html.Div([
    common_modules.get_navbar(),
    html.Br(),
    html.H1(id='Still in construction',children='Still in Construction')
    ]
  

)
