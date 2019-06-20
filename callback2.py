import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State

app=dash.Dash()

app.layout= html.Div([
    dcc.Input(id='num_in',value=1),
    html.Button(id='button',n_clicks=0,children='Submit'),
    html.H1(id='num_out')
])

@app.callback(Output('num_out','children'),
            [Input('button','n_clicks')],
            [State('num_in','value')])

def output(n_clicks,number):
    return number
if __name__ == "__main__":
    app.run_server()