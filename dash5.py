import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div([
            html.Label('____Dropdown____'),
            dcc.Dropdown(options=[{'label':'City1','value':'v1'},
                                  {'label':'City2','value':'v2'}]),
            html.Label('____Slider____'),
            dcc.Slider(min=-10,max=10,step=0.5,value=0,marks={i:i for i in range(-10, 10)}),
            html.P(html.Label('Radio Items')),
            dcc.RadioItems(options=[{'label':'la1','value':'la1'},
                                    {'label':'la2','value':'la2'}])],
          style={'textAlign':'center'})


if __name__ == "__main__":
    app.run_server()