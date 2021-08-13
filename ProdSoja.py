import pandas as pd
import plotly.express as px  # (version 4.7.0)
import json
from urllib.request import urlopen
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

soybean = pd.read_csv(
    "https://raw.githubusercontent.com/nayanemaia/Dataset_Soja/main/soja%20sidra.csv"
)

with urlopen(
        'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
) as response:
    data = json.load(response)

state_id_map = {}
for feature in data['features']:
    feature['id'] = feature['properties']['name']
    state_id_map[feature['properties']['sigla']] = feature['id']

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "1940", "value": 1940},
                     {"label": "1950", "value": 1950},
                     {"label": "1960", "value": 1960},
                     {"label": "1970", "value": 1970},
                     {"label": "1975", "value": 1975},
                     {"label": "1980", "value": 1980},
                     {"label": "1995", "value": 1995},
                     {"label": "2006", "value": 2006},
                     {"label": "2017", "value": 2017}],
                 multi=False,
                 value=1940,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='prodsoja', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='prodsoja', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):

    container = "The year chosen by user was: {}".format(option_slctd)

    ##dff = dff[dff["Censo"] == option_slctd]

    # Plotly Express
    fig = px.choropleth(
        soybean , #soybean database
        locations = 'Estado', #define the limits on the map/geography
        geojson = data, #shape information
        color = "Produção", #defining the color of the scale through the database
        hover_name = 'Estado', #the information in the box
        hover_data =["Produção","Longitude","Latitude"],
        #title of the map
        animation_frame = 'ano' #creating the application based on the year
    )
    fig.update_geos(fitbounds = "locations", visible = False)
    fig.show()

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)