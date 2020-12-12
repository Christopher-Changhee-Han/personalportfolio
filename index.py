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
                dbc.NavLink("Bio", href="/bio", id="page-1-link"),
                dbc.NavLink("Portfolio", href="/portfolio", id="page-2-link"),
                dbc.NavLink("Random", href="/random", id="page-3-link"),
            ],
            brand="Christopher Han",
            color="dark",
            dark=True,
        ),
        dbc.Container(id="page-content", className="pt-4"),
    ]
)

if __name__ == '__main__':
    app.run_server(debug = True)