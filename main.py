from dash import Dash, dcc
from layout.main_layout import get_layout
from callbacks.callbacks import get_callbacks
from dartbot.core.dartbot import DartBot


dartbot = DartBot(sigma=(17.05, 24.14), mu=(-0.38, -1.72))

app = Dash()

app.layout = [
    get_layout(),
    dcc.Interval(id="dartbot-interval", disabled=False, interval=1*600, n_intervals=4, max_intervals=4),
    dcc.Store(id="dummy", data=0),
    dcc.Store(id="dartbot-score", data=501),
    dcc.Store(id="player-score", data=501),
    dcc.Store(id="last-dartbot-turn", data=[]),
]

get_callbacks(app, dartbot)


if __name__ == "__main__":
    app.run(debug=True)