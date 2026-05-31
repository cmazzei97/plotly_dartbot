import time

from dash import Dash, html, dcc, callback, Output, Input, State
import numpy as np
import plotly.graph_objects as go

from board_dimensions import draw_dartboard


app = Dash()

app.layout = [
    html.H1(children="My Dash App", style={"textAlign":"center"}),
    dcc.Button("Dartbot turn", id="dartbot-button", n_clicks=0),
    dcc.Graph(id="graph-content", style={"width": "800px", "height": "800px"}),
]


@callback(
    Output("graph-content", "figure"),
    Input("dartbot-button", "n_clicks"),
)
def generate_board(n_clicks):
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
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        # showline=False,
    )
    draw_dartboard(fig=fig)

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

@callback(
    Output("graph-content", "figure", allow_duplicate=True),
    Input("dartbot-button", "n_clicks"),
    State("graph-content", "figure"),
    prevent_initial_call=True
)
def show_throws(n_clicks, fig):
    # here you call the dartbot turn and get three throws
    darts = [(-3, 4), (29, 125), (0, 168)]

    # retrieve trace from fig
    dart_trace = fig["data"][-1]

    # reset the trace
    dart_trace["x"] = []
    dart_trace["y"] = []

    # add bot throws one by one
    for dart_x, dart_y in darts:
        dart_trace["x"] += [dart_x]
        dart_trace["y"] += [dart_y]

    return fig










if __name__ == "__main__":
    app.run(debug=True)