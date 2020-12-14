import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

# Bio
layout_bio = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
                html.Img(src=app.get_asset_url('profile.jpg'), style= {'height':'80%', 'width':'80%'})
                ]), width = 3
        ),
    
        dbc.Col(
            html.Div([
                dcc.Markdown('''
                Big data and fancy models are cool but what's most important to me is efficiently solving the problem at hand. I'm a focused problem-solver and an effective communicator that loves to help others answer questions productively. My toolbox consists of coding experience in Python, SQL and R as well as deep statistical knowledge in topics such as experiment design, unsupervised and supervised learning, and bayesian inference.

                Outside of school, I lead a community organization called The Space that provides free dance classes to students at UT Austin and Texas A&M University. I also enjoy attempting to cook delicious food at home (learning rate is slow) and playing games with friends on my recently acquired Nintendo Switch. 
            
                ''')
                ])
        )
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            dcc.Tabs(id='bio-tabs', value='tab-edu', children=[
                dcc.Tab(label='Education', value='tab-edu'),
                dcc.Tab(label='Experience', value='tab-exp'),
                dcc.Tab(label='Skills', value= 'tab-skill'),
                dcc.Tab(label='Contact', value='tab-con')
            ]),
            html.Div(id='bio-tabs-content')
        ]))
    ])
])

# Bio: Education
layout_bio_edu = html.Div([
    html.P('big brain time')
])

# Bio: Experience
layout_bio_exp = html.Div([
    html.P('haha what experience')
])

# Bio: Skills

layout_bio_skills = html.Div([
    html.P('mad skillz')
])

# Bio: Contact

layout_bio_contact = html.Div([
    html.P('(512)-788-3841'),

])


# Portfolio 
layout_portfolio = html.Div([
    html.P('Cool projects are very cool')
])

# Random
layout_random = html.Div([
    html.P('randomness')
])

