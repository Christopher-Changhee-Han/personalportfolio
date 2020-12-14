import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from tables import table_edu

# Main
layout_main = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
                html.Img(src=app.get_asset_url('profile.jpg'), style= {'height':'80%', 'width':'80%'})
                ]), width = 3
        ),

        dbc.Col(html.Div([
            dcc.Tabs(id='bio-tabs', value='tab-intro', children=[
                dcc.Tab(label='Intro', value = 'tab-intro'),
                dcc.Tab(label='Education', value='tab-edu'),
                dcc.Tab(label='Experience', value='tab-exp'),
                dcc.Tab(label='Skills', value= 'tab-skill')
            ]),
            html.Div(id='bio-tabs-content')
        ]))

    ])
])

# Bio: Bio
layout_main_intro = html.Div([
    dbc.Jumbotron(
    [
        html.H1("Aspiring Data Scientist", className="display-3"),
        html.P(
            "Experience in Python, SQL, and R"
            "",
            className="lead",
        ),
        html.Hr(className="my-2"),
        dcc.Markdown('''
        Big data and fancy models are cool but what's most important to me is efficiently solving the problem at hand. I'm a focused problem-solver and an effective communicator that loves to help others answer questions productively. My toolbox consists of coding experience in Python, SQL and R as well as deep statistical knowledge in topics such as experiment design, unsupervised and supervised learning, and bayesian inference.

        Outside of school, I lead a community organization called The Space that provides free dance classes to students at UT Austin and Texas A&M University. I also enjoy attempting to cook delicious food at home (learning rate is slow) and playing games with friends on my recently acquired Nintendo Switch. 
        '''),
    ]
)
])

# Bio: Education
layout_main_edu = html.Div([
    html.P('M.S. in Statistics, Texas A&M University'),
    dbc.Progress("83.3% (30/36 hours)", value = 30*100/36, color = 'info'),
    html.P(children=[
        'Aug 2019', html.Span('May 2021', style = {'float':'right'})
    ]),

    html.Div([
        dbc.Button(
            "Coursework",
            id="collapse-button",
            className="mb-3",
            color="light",
        ),
        dbc.Collapse(
            dbc.Card(table_edu),
            id="collapse",
        )
    ]),

    html.P('B.A. in Spanish, The University of Texas at Austin'),
    dbc.Progress("100%", value = 100, color = 'success'),
    html.P(children=[
        'Aug 2014', html.Span('Dec 2018', style = {'float':'right'})
    ])
])

# Bio: Experience
layout_main_exp = html.Div([
    html.P('haha what experience')
])

# Bio: Skills

layout_main_skills = html.Div([
    html.P('mad skillz'),
    dbc.Badge("Python", pill=True, color="primary", className="mr-1"),
    dbc.Badge("SQL", pill=True, color="primary", className="mr-1"),
    dbc.Badge("R", pill=True, color="primary", className="mr-1"),
    dbc.Badge("English", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("Korean", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("Spanish", pill=True, color="secondary", className="mr-1")
])


# Portfolio 
layout_portfolio = html.Div([
    html.P('Cool projects are very cool')
])

# Random
layout_random = html.Div([
    html.P('randomness')
])

