from dash import Output, Input, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import board_dimensions


def get_callbacks(app, dartbot):
    # 0. Draw the dartboard and prepare the trace for the darts being thrown ##
    @app.callback(
        Output("graph-content", "figure"),
        Input("dummy", "data"),
    )
    def generate_board(dummy_var):
        fig = go.Figure()
        fig.update_layout(
            xaxis=dict(range=[-180, 180]),
            yaxis=dict(range=[-180, 180]),
            plot_bgcolor="white",
        )
        fig.update_xaxes(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showline=False,
        )
        fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            # showline=False,
        )
        board_dimensions.draw_dartboard(fig=fig)

        # make sure to add this trace last!!!
        dart_trace = go.Scatter(
            x=[],
            y=[],
            mode="markers",
            marker=dict(size=10, color="red"),
            name="darts",
            showlegend=False,
        )
        fig.add_trace(dart_trace)

        return fig

    ## 1. Calls the dartbot to return a turn to store in the appropriate Store variable ##
    @app.callback(
            Output("last-dartbot-turn", "data"),
            Output("dartbot-score", "data", allow_duplicate=True),
            Input("submit-score-button", "n_clicks"), 
            State("dartbot-score", "data"), 
            prevent_initial_call=True,
    )
    def call_next_dartbot_turn(n_clicks, remaining_score):
        turn, dartbot_score = dartbot.turn(remaining_score)
        return turn, dartbot_score
    
    ## 1.1 Update the player input box to clear the contents after the submit button is pressed ##
    @app.callback(
            Output("player-score-input", "value"),
            Input("submit-score-button", "n_clicks"), 
            prevent_initial_call=True,
    )
    def empty_player_input(n_clicks):
        return ""
    
    # 1.2 Update the Store variable with the player score, using the score inputted by the player ##
        # would this be where error handling for the input goes?
    @app.callback(
        Output("player-score", "data", allow_duplicate=True),
        Input("submit-score-button", "n_clicks"),
        State("player-score-input", "value"),
        State("player-score", "data"),
        prevent_initial_call=True,
    )
    def update_player_score(
        n_clicks,
        player_score_input,
        player_score
    ):
        new_score = player_score - int(player_score_input)
        return new_score
    
    # 1.3 Update the displayed score with the current score from the Store variable ##
    @app.callback(
            Output("player-score-display","children"),
            Input("player-score", "data"),
            prevent_initial_call=True,
    )
    def update_player_disp_score(current_score):
        return str(current_score)

    ## 2. Resets the interval when the dartbot turn changes ##
    @app.callback(
            Output("dartbot-interval", "n_intervals"),
            Input("last-dartbot-turn", "data"),
            prevent_initial_call=True,
    )
    def reset_intervals(turn_data):
        return 0

    ## 3. Shows the darts one by one and resets the trace to empty when the interval resets ##
    @app.callback(
        Output("graph-content", "figure", allow_duplicate=True),
        Input("dartbot-interval", "n_intervals"),
        State("graph-content", "figure"),
        State("last-dartbot-turn","data"),
        prevent_initial_call=True,
    )
    def show_throws(n_intervals, fig, last_turn):
        # retrieve trace from fig
        dart_trace = fig["data"][-1]

        if n_intervals == 0:
            dart_trace["x"] = []
            dart_trace["y"] = []
        elif n_intervals <= len(last_turn):
            dart_trace["x"] += [last_turn[n_intervals - 1]["x_coord"]]
            dart_trace["y"] += [last_turn[n_intervals - 1]["y_coord"]]
        else:
            raise PreventUpdate

        return fig
    
    ## 5. Update displayed dartbot score to the current score from the Store variable ##
    @app.callback(
            Output("dartbot-score-display", "children"),
            Input("dartbot-interval", "n_intervals"),
            State("dartbot-score", "data"),
            prevent_initial_call=True,
    )
    def update_dartbot_disp_score(n_intervals, current_score):
        if n_intervals == 4:
            return str(current_score)
        else:
            raise PreventUpdate

    ## 6. Reset all variables to start a new game ##
    @app.callback(
        Output("player-score","data", allow_duplicate=True),
        Output("dartbot-score", "data", allow_duplicate=True),
        Output("dartbot-score-display", "children", allow_duplicate=True),
        Output("graph-content", "figure", allow_duplicate=True),
        Input("new-game-button", "n_clicks"),
        State("graph-content", "figure"),
        prevent_initial_call=True,
    )       
    def start_new_game(n_clicks, fig):
        fig["data"][-1]["x"] = []
        fig["data"][-1]["y"] = []
        return 501, 501, "501", fig
