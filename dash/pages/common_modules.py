import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from flask import request


def get_navbar():
    navbar=html.Div([ 
            html.Div(
                     html.A([html.Img(src='/assets/pictures/SimFuel_logo.png'),
                             html.H2("Sim Fuel",className='simfuel_label')],href='/'),
                             className='navbar_logo'), 

            html.Div([html.Div(html.Img(src='/assets/pictures/search.png'),style={'width':"30%",'display':'inline','vertical-algin':'top'}),
                     html.Div(html.A(html.H4('Search Fuel Database',className='link_label'),href='/file_search'),style={'width':"70%",'display':'inline-block','vertical-algin':'top'})],
                     className='navbar_links', style={'width':"12%",'vertical-align':'middle'}),
            html.Div([html.Div(html.Img(src='/assets/pictures/compare.png'),style={'width':"30%",'display':'inline','vertical-algin':'top'}),
                     html.Div(html.A(html.H4('Assess Fuel',className='link_label'),href='/assess_fuel'),style={'width':"70%",'display':'inline-block','vertical-algin':'top'})],
                     className='navbar_links', style={'width':"12%",'vertical-align':'middle','border-left':'2px solid white'}),
            html.Div([html.Div(html.Img(src='/assets/pictures/compare.png') ,style={'width':"30%",'display':'inline','vertical-algin':'top'}), 
                     html.Div(html.A(html.H4('Compare Fuels',className='link_label'),href='/compare_fuels'),style={'width':"70%",'display':'inline-block','vertical-algin':'top'})],
                     className='navbar_links', style={'width':"12%",'vertical-align':'middle','border-left':'2px solid white'}),
            html.Div([html.Div(html.Img(src='/assets/pictures/predict.png'),style={'width':"30%",'display':'inline','vertical-algin':'top'}),  
                     html.Div(html.A(html.H4('Predict Properties',className='link_label'),href='/predict'),style={'width':"70%",'display':'inline-block','vertical-algin':'top'})],
                     className='navbar_links', style={'width':"12%",'vertical-align':'middle','border-left':'2px solid white'}),     
            html.Div([html.Div(html.Img(src='/assets/pictures/mix.png'), style={'width':"30%",'display':'inline','vertical-algin':'top'}),
                     html.Div(html.A(html.H4('Blending Studies',className='link_label'),href='/blending'),style={'width':"70%",'display':'inline-block','vertical-algin':'top'})],
                     className='navbar_links', style={'width':"12%",'vertical-align':'middle','border-left':'2px solid white'}),    
            html.Div([html.Div(html.Img(src='/assets/pictures/optimize.png'),  style={'width':"30%",'display':'inline','vertical-algin':'top'}),
                     html.Div(html.A(html.H4('Fuel Optimization',className='link_label'),href='/optimization'),style={'width':"70%",'display':'inline-block'})],
                     className='navbar_links', style={'width':"12%","height":"100%",'vertical-align':'middle','border-left':'2px solid white'}), 


            html.Div([
                      html.H3(id='login_name',children=''),
                      html.Div(id='dum_0', children=0,style={'display':'none'})],className='navbar_login_name')

            ],className='navbar')
            
    return navbar


