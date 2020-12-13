import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

layout_bio = html.Div([
    html.Img(src=app.get_asset_url('profile.jpg')),
    html.P("It's a me, Chris")
])

layout_portfolio = html.Div([
    html.P('Cool projects are very cool')
])

layout_random = html.Div([
    html.P('randomness')
])

