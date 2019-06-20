import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

markdowntext='''Wikipedia (/ˌwɪkɪˈpiːdiə/ (About this soundlisten), /ˌwɪkiˈpiːdiə/ (About this soundlisten) WIK-kee-PEE-dee-ə) is a multilingual online encyclopedia, based on open collaboration through a wiki-based content editing system. It is the largest and most popular general reference work on the World Wide Web,[3][4][5] and is one of the most popular websites ranked by Alexa as of June 2019.'''

app.layout=html.Div([
                        dcc.Markdown(children=markdowntext)
])

if __name__ == "__main__":
    app.run_server()