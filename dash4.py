import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div(['________Outer_______',
                    html.Div(['__Inner___'],style={'border':'dotted'})],
                    style={'textAlign':'center','color':'green','border':'solid'})


if __name__ == "__main__":
    app.run_server()