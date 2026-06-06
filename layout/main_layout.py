from dash import html, dcc



def get_layout():
    layout = html.Div(
        children=[
            dcc.Graph(id="graph-content", style={"width": "800px", "height": "800px"}),
            html.Div(
                children=[
                    get_scorecard(),
                    get_player_input(),
                    new_game_button(),
                ],
            ),
        ],
        style={"display": "flex"},
    )
    

    return layout

######################
###    ELEMENTS    ###
######################
def get_player_input():
    return html.Div(
        children=[
            html.Div(children=[
                html.P("Please enter your score here:", id="player-score-text", style={"fontSize": "20px"}),
                dcc.Input(id="player-score-input", style={"width": "120px", "height": "40px"}),
                dcc.Button("Submit Score", id="submit-score-button", n_clicks=0, style={"width": "120px", "height": "40px"}),
            ],
            style={"display": "flex", "gap": "10px", "alignItems": "center", "marginTop": "50px"},
            )
        ],
    )

def get_scorecard():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.P("Dartbot's Remaining Score", style={"fontSize": "20px", "fontWeight": "bold", "textDecoration": "underline"}),
                    html.P("501", id="dartbot-score-display", style={"fontSize": "18px", "textColor": "black"}),
                ],
                style={"textAlign": "center"},
            ),
            html.Div(
                children=[
                    html.P("Player's Remaining Score", style={"fontSize": "20px", "fontWeight": "bold", "textDecoration": "underline"}),
                    html.P("501", id="player-score-display",  style={"fontSize": "18px", "textColor": "black"}),
                ],
                style={"textAlign": "center"},
            )
        ],
        style={"display": "flex", "marginTop": "100px", "gap": "50px"}
    )

def new_game_button():
    return html.Div(children=[
        dcc.Button("New Game", id="new-game-button", n_clicks=0,style={"width": "120px", "height": "40px"})
        ], 
        style={"textAlign": "center", "marginTop": "50px"})
