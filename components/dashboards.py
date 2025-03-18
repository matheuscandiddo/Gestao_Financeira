from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app

card_icon = {
    "color":"white",
    "textAlign":"center",
    "fontSize": 30,
    "margin": "auto"
}


# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([

        # Card de Saldo
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Saldo'),
                    html.H5('R$ 5000', id='p-saldo-dashboard', style={})
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-university', style=card_icon),
                    color='warning',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                )
            ])
        ], width=4),

        # Card de Receita
                dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Receita'),
                    html.H5('R$ 1345', id='p-receita-dashboard', style={})
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-smile-o', style=card_icon),
                    color='success',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                )
            ])
        ], width=4),

        # Card de Despesa
                dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Despesa'),
                    html.H5('R$ -2000', id='p-despesa-dashboard', style={})
                ], style={'padding-left':'20px', 'padding-top':'10px'}),
                dbc.Card(
                    html.Div(className='fa fa-meh-o', style=card_icon),
                    color='danger',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                )
            ])
        ], width=4),
    ], style={'margin': '10px'}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar lançamentos", className="card-title"),
                html.Label("Categorias das receitas"),
                html.Div(
                    dcc.Dropdown(
                    id="dropdown-receita",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True)
                ),

                html.Label("Categorias das despesas", style={"margin-top":"10px"}),
                dcc.Dropdown(
                    id="dropdown-despesa",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True
                ),

                html.Legend("Período de Análise", style={"margin-top":"10px"}),
                dcc.DatePickerRange(
                    month_format='Do MMM, YY',
                    end_date_placeholder_text='Data...',
                    start_date=datetime.today(),
                    end_date=datetime.today() + timedelta(days=31),
                    with_portal=True,
                    updatemode='singledate',
                    id='date-picker-config',
                    style={'z-index': '100'}),
            ],style={'height':"100%", 'padding':'20px'})
        ], width=4),
        
        dbc.Col(
            dbc.Card(dcc.Graph(id='graph'),style={'height':'100%', 'padding':'10px'}), width=8
        )
    ], style={'margin': '10px'}),

    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id='Graph2'), style={'padding':'10px'}), width=6),
        dbc.Col(dbc.Card(dcc.Graph(id='Graph3'), style={'padding':'10px'}), width=3),
        dbc.Col(dbc.Card(dcc.Graph(id='Graph4'), style={'padding':'10px'}), width=3),
    ])
])



# =========  Callbacks  =========== #
# @app.callback([
#     Output("dropdown-receita", "options"),
#     Output("dropdown-receita", "value"),
#     Output("p-receita-dashboard", "children")],
#     Input("store-receita", "data"))
# def populate_dropdownvalues(data):
#     df = pd.DataFrame(data)
#     valor = df['Valor'].sum()
#     val = df.Categoria.unique().tolist()
#     [{"label": x, "value": x} for x in val]
#     return ([{"label": x, "value": x} for x in val], val, f"R${valor}")

# @app.callback([
#     Output("dropdown-despesa", "options"),
#     Output("dropdown-despesa", "value"),
#     Output("p-despesa-dashboard", "children")],
#     Input("store-despesa", "data"))
# def populate_dropdownvalues(data):
#     df = pd.DataFrame(data)
#     valor = df['Valor'].sum()
#     val = df.Categoria.unique().tolist()
#     [{"label": x, "value": x} for x in val]
#     return ([{"label": x, "value": x} for x in val], val, f"R${valor}")