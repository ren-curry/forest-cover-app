# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

# Imports from this application
from app import app
from joblib import load
pipeline = load("assets/pipeline.joblib")

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Elevation', 'value'),
     Input('Aspect', 'value'),
     Input('Slope', 'value'),
     Input('Horizontal_Distance_To_Hydrology', 'value'),
     Input('Vertical_Distance_To_Hydrology', 'value'),
     Input('Horizontal_Distance_To_Roadways', 'value'),
     Input('Horizontal_Distance_To_Fire_Points', 'value'),
     Input('Hillshade_9am', 'value'),
     Input('Hillshade_Noon', 'value'),
     Input('Hillshade_3pm', 'value'),
     Input('Soil_Type', 'value'),
     Input('Wilderness_Area', 'value')],
)
def predict(Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology, 
            Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, 
            Horizontal_Distance_To_Fire_Points,Hillshade_9am, Hillshade_Noon,
            Hillshade_3pm, Soil_Type, Wilderness_Area):
    Euclidean_Distance_To_Hydrology = np.sqrt(Horizontal_Distance_To_Hydrology**2 + Vertical_Distance_To_Hydrology**2)
    soil_code = [char for char in Soil_Type]
    Climatic_Zone = soil_code[0]
    Geologic_Zone = soil_code[1]
    df = pd.DataFrame(
        columns=['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
                 'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
                 'Horizontal_Distance_To_Fire_Points', 'Soil_Type', 'Wilderness_Area', 'Climatic_Zone',
                 'Geologic_Zone', 'Euclidean_Distance_To_Hydrology'
                ], 
        data=[[Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology, 
            Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, 
            Horizontal_Distance_To_Fire_Points,Hillshade_9am, Hillshade_Noon,
            Hillshade_3pm, Soil_Type, Wilderness_Area, Climatic_Zone, Geologic_Zone, 
            Euclidean_Distance_To_Hydrology]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            To make a prediction, adjust the features to the right. There are a total of 12 options features which you can adjust. You will predict one of the following type of trees providing the cover:
            * Spruce/Fir 
            * Lodgepole Pine 
            * Ponderosa Pine 
            * Cottonwood/Willow 
            * Aspen 
            * Douglas-fir 
            * Krummholz

            """
        ),
        html.H2('Predicted Cover Type:', className='mb-5'), 
        html.H3(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Elevation'), 
        dcc.Slider(
            id='Elevation', 
            min=1850, 
            max=4000, 
            step=1, 
            value=3000, 
            marks={n: str(n) for n in range(1850,4000,100)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Aspect'), 
        dcc.Slider(
            id='Aspect', 
            min=0, 
            max=360, 
            step=1, 
            value=155, 
            marks={n: str(n) for n in range(0,360,20)}, 
            className='mb-5', 
        ),  
        dcc.Markdown('#### Slope'),
        dcc.Slider(
            id='Slope', 
            min=0, 
            max=70, 
            step=1, 
            value=15, 
            marks={n: str(n) for n in range(0,70,5)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Horizontal Distance to Surface Water'),
        dcc.Slider(
            id='Horizontal_Distance_To_Hydrology', 
            min=0, 
            max=1500, 
            step=1, 
            value=212, 
            marks={n: str(n) for n in range(0,1500,100)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Vertical Distance to Surface Water'),
        dcc.Slider(
            id='Vertical_Distance_To_Hydrology', 
            min=-200, 
            max=700, 
            step=1, 
            value=45, 
            marks={n: str(n) for n in range(-200,700,50)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Distance to Nearest Roadway'),
        dcc.Slider(
            id='Horizontal_Distance_To_Roadways', 
            min=0, 
            max=7200, 
            step=1, 
            value=2350, 
            marks={n: str(n) for n in range(0,7500,500)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Distance to Nearest Fire Point'),
        dcc.Slider(
            id='Horizontal_Distance_To_Fire_Points', 
            min=0, 
            max=7200, 
            step=1, 
            value=1980, 
            marks={n: str(n) for n in range(0,7500,500)}, 
            className='mb-5',
        ),   
        dcc.Markdown('#### Hillshade at 9am'),
        dcc.Slider(
            id='Hillshade_9am', 
            min=0, 
            max=255, 
            step=1, 
            value=212, 
            marks={n: str(n) for n in range(0,255,17)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Hillshade at Noon'),
        dcc.Slider(
            id='Hillshade_Noon', 
            min=0, 
            max=255, 
            step=1, 
            value=223, 
            marks={n: str(n) for n in range(0,255,17)}, 
            className='mb-5', 
        ),   
        dcc.Markdown('#### Hillshade at 3pm'),
        dcc.Slider(
            id='Hillshade_3pm', 
            min=0, 
            max=255, 
            step=1, 
            value=142, 
            marks={n: str(n) for n in range(0,255,17)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Soil Type'), 
        dcc.Dropdown(
            id='Soil_Type', 
            options = [
                {'label': 'Soil Type 1', 'value': '2702'},
                {'label': 'Soil Type 2', 'value': '2703'},
                {'label': 'Soil Type 3', 'value': '2704'},
                {'label': 'Soil Type 4', 'value': '2705'},
                {'label': 'Soil Type 5', 'value': '2706'},
                {'label': 'Soil Type 6', 'value': '2717'},
                {'label': 'Soil Type 7', 'value': '3501'},
                {'label': 'Soil Type 8', 'value': '3502'},
                {'label': 'Soil Type 9', 'value': '4201'},
                {'label': 'Soil Type 10', 'value': '4703'},
                {'label': 'Soil Type 11', 'value': '4704'},
                {'label': 'Soil Type 12', 'value': '4744'},
                {'label': 'Soil Type 13', 'value': '4758'},
                {'label': 'Soil Type 14', 'value': '5101'},
                {'label': 'Soil Type 15', 'value': '5151'},
                {'label': 'Soil Type 16', 'value': '6101'},
                {'label': 'Soil Type 17', 'value': '6102'},
                {'label': 'Soil Type 18', 'value': '6731'},
                {'label': 'Soil Type 19', 'value': '7101'},
                {'label': 'Soil Type 20', 'value': '7102'},
                {'label': 'Soil Type 21', 'value': '7103'},
                {'label': 'Soil Type 22', 'value': '7201'},
                {'label': 'Soil Type 23', 'value': '7202'},
                {'label': 'Soil Type 24', 'value': '7700'},
                {'label': 'Soil Type 25', 'value': '7701'},
                {'label': 'Soil Type 26', 'value': '7702'},
                {'label': 'Soil Type 27', 'value': '7709'},
                {'label': 'Soil Type 28', 'value': '7710'},
                {'label': 'Soil Type 29', 'value': '7745'},
                {'label': 'Soil Type 30', 'value': '7746'},
                {'label': 'Soil Type 31', 'value': '7755'},
                {'label': 'Soil Type 32', 'value': '7756'},
                {'label': 'Soil Type 33', 'value': '7757'},
                {'label': 'Soil Type 34', 'value': '7790'},
                {'label': 'Soil Type 35', 'value': '8703'},
                {'label': 'Soil Type 36', 'value': '8707'},
                {'label': 'Soil Type 37', 'value': '8708'},
                {'label': 'Soil Type 38', 'value': '8771'},
                {'label': 'Soil Type 39', 'value': '8772'},
                {'label': 'Soil Type 40', 'value': '8776'}, 
            ], 
            value = 'Soil Type 10', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Wilderness Area'), 
        dcc.Dropdown(
            id='Wilderness_Area', 
            options = [
                {'label': 'Rawah Wilderness Area', 'value': 'Rawah Wilderness Area'}, 
                {'label': 'Neota Wilderness Area', 'value': 'Neota Wilderness Area'}, 
                {'label': 'Comanche Peak Wilderness Area', 'value': 'Comanche Peak Wilderness Area'}, 
                {'label': 'Cache la Poudre Wilderness Area', 'value': 'Cache la Poudre Wilderness Area'}, 
            ], 
            value = 'Rawah Wilderness Area', 
            className='mb-5', 
        ), 
    ],
)

layout = dbc.Row([column1, column2])