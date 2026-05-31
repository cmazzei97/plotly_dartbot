import numpy as np
import plotly.graph_objects as go


def draw_circle(radius, fig, color="black"):
    theta = np.linspace(0, 2 * np.pi, 500)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            line=dict(color=color),
            showlegend=False,
        )
    )


def draw_segment(theta, fig, color="black"):
    radius = np.linspace(16, 170, 2)
    
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            line=dict(color=color),
            showlegend=False,
        )
    )


def draw_dartboard(fig):
    radii = [6.35, 16, 97, 107, 160, 170]
    thetas = [
        0.15707963267948966,
        0.47123889803846897,
        0.7853981633974483,
        1.0995574287564276,
        1.413716694115407,
        1.7278759594743862,
        2.0420352248333655,
        2.356194490192345,
        2.670353755551324,
        2.9845130209103035,
        3.2986722862692828,
        3.612831551628262,
        3.9269908169872414,
        4.241150082346221,
        4.5553093477052,
        4.869468613064179,
        5.183627878423159,
        5.497787143782138,
        5.811946409141117,
        6.126105674500097,
    ]

    for radius in radii:
        draw_circle(radius=radius, fig=fig)

    for theta in thetas:
        draw_segment(theta=theta, fig=fig)
