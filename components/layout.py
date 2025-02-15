from dash import dcc, html
import dash_bootstrap_components as dbc

def layout(theme_class):
    return html.Div(id="main-container", className=theme_class, children=[
        html.H1("Visualisation du cours Bitcoin", className="text-center my-4"),
        
        # Filtres alignés horizontalement
        dbc.Row(
            [
                dbc.Col([
                    html.Label("Intervalle temporel", style={"font-weight": "bold"}),
                    dcc.Dropdown(
                        id='time-interval',
                        options=[
                            {"label": "1 Minute", "value": "1T"},
                            {"label": "30 Minutes", "value": "30T"},
                            {"label": "1 Heure", "value": "1H"},
                            {"label": "24 Heures", "value": "1D"}
                        ],
                        value="1H",
                        className="dropdown-style"
                    )
                ], width=3),
                dbc.Col([
                    html.Label("Type de moyenne mobile", style={"font-weight": "bold"}),
                    dcc.Dropdown(
                        id='ma-type',
                        options=[
                            {"label": "Moyenne Simple", "value": "SMA"},
                            {"label": "Moyenne Exponentielle", "value": "EMA"}
                        ],
                        value="SMA",
                        className="dropdown-style"
                    )
                ], width=3),
                dbc.Col([
                    html.Label("Plage de dates", style={"font-weight": "bold"}),
                    dcc.DatePickerRange(
                        id='date-range',
                        display_format="DD-MM-YYYY",
                        className="date-picker-style"
                    )
                ], width=4),
                dbc.Col([
                    html.Label("Mode Clair/Sombre", style={"font-weight": "bold"}),
                    dbc.Switch(id="theme-toggle", value=False, className="theme-switch")
                ], width=2)
            ],
            className="filter-row"
        ),
        
        # Graphique
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='bitcoin-chart', config={"displayModeBar": True}),
            ], width=12)
        ])
    ])