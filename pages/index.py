# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Forest Cover Type Predictor

            Welcome to the Forest Cover Type predictor for the Roosevelt National Forest. This app will predict the type of Tree Covering a given 30m by 30m section of forest based on the cartographic values provide. This app could be useful for hikers, botany hobbyists, or perhaps even the forest service. 

            Click the button below to access the predictor. 

            """
        ),
        dcc.Link(dbc.Button('Predict your Cover Type', color='primary'), href='/predictions')
    ],
    md=4,
)
layout = dbc.Row([column1])