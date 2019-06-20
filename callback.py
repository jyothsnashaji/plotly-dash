import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app=dash.Dash()

app.layout=html.Div([
    dcc.Input(id='myid',value='Initial Text',type='text'),
    html.Div(id='mydiv')
])

@app.callback(Output(component_id='mydiv',component_property='children'),
           [Input(component_id='myid',component_property='value')])

def update_output_div(inp):
    return "Entered {}".format(inp)

if __name__ == "__main__":
    app.run_server()
