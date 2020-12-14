import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from app import app, server
import callbacks

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Main", href="/main", id="page-1-link"),
                dbc.NavLink("Portfolio", href="/portfolio", id="page-2-link"),
                dbc.NavLink("Random", href="/random", id="page-3-link"),
                dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/christopher-c-han/", id="linkedin-link"),
                dbc.NavLink("GitHub", href="https://github.com/Christopher-Changhee-Han", id="github-link")
            ],
            brand="Christopher Han",
            color="dark",
            dark=True
        ),
        dbc.Container(id="page-content", className="pt-4",
        style= {'padding-bottom':'70px'}),
        dbc.NavbarSimple(
            brand= 'GitHub Repo',
            brand_style = {'font-size': '15px'},
            brand_href= 'https://github.com/Christopher-Changhee-Han/personalportfolio',
            fixed = 'bottom',
            color="dark",
            dark=True,
            style={'width':'100vw'}
        )
    ], style={'width':'100vw'}
)

if __name__ == '__main__':
    app.run_server(debug = True)