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
    html.H5('Dashboards'),
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

        # Card de Despesa
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
    ])
       
    ])



# =========  Callbacks  =========== #
