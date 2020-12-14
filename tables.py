import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

table_header = [
    html.Thead(html.Tr([html.Th("Semester"), html.Th("Course Name"), html.Th("What I learned"),html.Th("Grade")]))
]

row1 = html.Tr([html.Td("Fall 2019"),html.Td("604: Topics in Statistical Computations"), html.Td("R and SAS Programming"), html.Td("A")])
row2 = html.Tr([html.Td("Fall 2019"),html.Td("630: Overview of Mathematical Statistics"), html.Td(""), html.Td("A")])
row3 = html.Tr([html.Td("Fall 2019"),html.Td("641: The Methods of Statistics I"), html.Td(""), html.Td("A")])
row4 = html.Tr([html.Td("Spring 2020"),html.Td("608: Regression Analysis"), html.Td(""), html.Td("A")])
row5 = html.Tr([html.Td("Spring 2020"),html.Td("624: Databases and Computational Tools"), html.Td(""), html.Td("A")])
row6 = html.Tr([html.Td("Spring 2020"),html.Td("642: The Methods of Statistics II"), html.Td(""), html.Td("A")])
row7 = html.Tr([html.Td("Summer 2020"),html.Td("626: Methods in Time Series Analysis"), html.Td(""), html.Td("A")])
row8 = html.Tr([html.Td("Fall 2020"),html.Td("636: Applied Multivariate Analysis"), html.Td(""), html.Td("A")])
row9 = html.Tr([html.Td("Fall 2020"),html.Td("638: Applied Bayesian Methods"), html.Td(""), html.Td("A")])
row10 = html.Tr([html.Td("Fall 2020"),html.Td("681: Seminar"), html.Td(""), html.Td("S")])
row11 = html.Tr([html.Td("Fall 2020"),html.Td("684: Professional Internship"), html.Td(""), html.Td("S")])
row12 = html.Tr([html.Td("Spring 2021"),html.Td("631: Statistical Methods in Finance"), html.Td(""), html.Td("")])
row13 = html.Tr([html.Td("Spring 2021"),html.Td("639: Data Mining and Analysis"), html.Td(""), html.Td("")])
row14 = html.Tr([html.Td("Spring 2021"),html.Td("695: Frontiers in Statistical Research"), html.Td(""), html.Td("")])

table_body = [html.Tbody([row14, row13, row12, row11, row10, row9, row8, row7, row6, row5, row4, row3, row2, row1])]

table_edu = dbc.Table(table_header + table_body, bordered=True, hover = True)