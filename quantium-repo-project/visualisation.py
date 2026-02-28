

from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv("final_data.csv")


app.layout = html.Div([
    dcc.Graph(
        id="sales_graph"
        
    ),

    html.Label("Filter by region"),
    dcc.RadioItems(["north", "south", "east", "west"],"north", id="region")
    
], style={}


)


@callback(
    Output(component_id='sales_graph', component_property='figure'),
    Input(component_id='region', component_property='value'))
def update_graph(region_name):
    df = data[data['region'] == region_name]
    fig = px.line(df, x="date", y = "sales")
    fig.update_layout(title_text = "Pink Morsel sales of Souls Food", title_x = 0.5)
    return fig





if __name__ == '__main__':
    app.run(debug=True)
