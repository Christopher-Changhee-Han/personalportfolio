import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from tables import table_edu

# Main
tab_height = '7vh'
layout_main = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
                html.Img(src=app.get_asset_url('profile.jpg'), style= {'height':'100%', 'width':'100%'}),
                html.Hr(),
                dbc.Button('LinkedIn', href = 'https://www.linkedin.com/in/christopher-c-han/', outline = True, color = 'primary', className="mr-1"),
                #html.Br(),
                dbc.Button('GitHub', href = 'https://github.com/Christopher-Changhee-Han', outline = True, color = 'primary', className="mr-1"),
                #html.Br(),
                dbc.Button('Email', href="mailto:christopherhan@stat.tamu.edu", outline = True, color = 'primary', className="mr-1")
                ]), width = 3
        ),
        
        dbc.Col(html.Div([
            dcc.Tabs(id='bio-tabs', value='tab-intro', children=[
                dcc.Tab(label='Intro', value = 'tab-intro', style={'padding': '0','line-height': tab_height},selected_style={'padding': '0','line-height': tab_height}),
                dcc.Tab(label='Education', value='tab-edu', style={'padding': '0','line-height': tab_height},selected_style={'padding': '0','line-height': tab_height}),
                dcc.Tab(label='Experience', value='tab-exp', style={'padding': '0','line-height': tab_height},selected_style={'padding': '0','line-height': tab_height}),
                dcc.Tab(label='Skills', value= 'tab-skill', style={'padding': '0','line-height': tab_height},selected_style={'padding': '0','line-height': tab_height})
            ], style = {'height': tab_height}),
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
    html.Br(),
    html.H4('University'),
    html.P(['M.S. in Statistics, Texas A&M University', 
            html.Span(dbc.Badge("In Progress", color="dark", className="ml-1"), style = {'float':'right'})
    ]),
    dbc.Progress("83.3% (30/36 hours)", value = 30*100/36, color = 'success'),
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

    html.P(['B.A. in Spanish, The University of Texas at Austin', 
        html.Span(dbc.Badge("Complete", color="success", className="ml-1"), style = {'float':'right'})
    ]),
    html.Hr(),
    html.H4('Certificates'),
    html.P(children=[
        'Certificate in Applied Statistical Modelling, The University of Texas at Austin', 
        html.Span(dbc.Badge("Complete", color="success", className="ml-1"), style = {'float':'right'})
    ]),
    html.P(children=[
        'Data Science Specialization Certificate in R, Johns Hopkins University (Coursera)',
        html.Span(dbc.Badge("Complete", color="success", className="ml-1"), style = {'float':'right'})
    ]),

])

# Bio: Experience
layout_main_exp = html.Div([
    html.Br(),
    html.H4('Work'),
    dcc.Markdown('''
    
    Graduate Teaching Assistant, Texas A&M University, College Station    
    * Assisted teaching Quantitative Methods in Public Management I
    * Reviewed regression, hypothesis testing in R with students during office hours

    '''),
    html.Hr(), 
    html.H4('Leadership'),
    dcc.Markdown('''
    
    Co-Founder, The Space    
    * Lead a team of 7 people to organize free dance classes and charity programs
    * Established two branches in Austin and College Station

    '''),
])

# Bio: Skills

layout_main_skills = html.Div([
    html.Br(),  
    html.H4('Programming'),
    dbc.Badge("Python", pill=True, color="primary", className="mr-1"),
    dbc.Badge("numpy", pill=True, color="primary", className="mr-1"),
    dbc.Badge("pandas", pill=True, color="primary", className="mr-1"),
    dbc.Badge("scipy", pill=True, color="primary", className="mr-1"),
    dbc.Badge("matplotlib", pill=True, color="primary", className="mr-1"),
    dbc.Badge("scikit-learn", pill=True, color="primary", className="mr-1"),
    dbc.Badge("seaborn", pill=True, color="primary", className="mr-1"),
    dbc.Badge("plotly", pill=True, color="primary", className="mr-1"),
    dbc.Badge("Dash", pill=True, color="primary", className="mr-1"),
    html.Br(),
    dbc.Badge("R", pill=True, color="primary", className="mr-1"),
    dbc.Badge("SQL", pill=True, color="primary", className="mr-1"),
    dbc.Badge("NoSQL", pill=True, color="primary", className="mr-1"),
    dbc.Badge("Git", pill=True, color="primary", className="mr-1"),
    dbc.Badge("R", pill=True, color="primary", className="mr-1"),
    dbc.Badge("Excel", pill=True, color="primary", className="mr-1"),
    html.Hr(),
    html.H4('Presentation Skills'),
    dbc.Badge("Jupyter Notebook", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("R Markdown", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("Tableau", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("PowerPoint", pill=True, color="secondary", className="mr-1"),
    dbc.Badge("Word", pill=True, color="secondary", className="mr-1"),
    html.Hr(),
    html.H4('Languages'),
    dbc.Badge("English", pill=True, color="info", className="mr-1"),
    dbc.Badge("Korean", pill=True, color="info", className="mr-1"),
    dbc.Badge("Spanish", pill=True, color="info", className="mr-1")
])


# Portfolio 
layout_portfolio = html.Div([
    html.P('Cool projects are very cool')
])

# Random
layout_random = html.Div([
    html.P('randomness')
])

