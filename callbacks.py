import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app
from layouts import layout_bio, layout_portfolio, layout_random, layout_bio_contact, layout_bio_skills, layout_bio_edu, layout_bio_exp

# Main app callback
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/bio"]:
        return layout_bio
    elif pathname == "/portfolio":
        return layout_portfolio
    elif pathname == "/random":
        return layout_random
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Bio tabs callback
@app.callback(Output('bio-tabs-content', 'children'),
              [Input('bio-tabs', 'value')])
def render_content(tab):
    if tab == 'tab-edu':
        return layout_bio_edu
    elif tab == 'tab-exp':
        return layout_bio_exp
    elif tab == 'tab-skill':
        return layout_bio_skills
    elif tab == 'tab-con':
        return layout_bio_contact