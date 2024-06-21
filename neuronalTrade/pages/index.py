"""The main index page."""

import reflex as rx
from neuronalTrade.data import (
    stat_card_data,
    lines_data_live,
    pie_chart_data,
    area_chart_data,
    areas,
    tabular_data,
    line_chart_component,
)
from neuronalTrade.graphs import (
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from neuronalTrade.navigation import navbar
from neuronalTrade.template import template

# Content in a grid layout.
def content_grid():
    return rx.chakra.grid(
        *[
            rx.chakra.grid_item(stat_card(*c), col_span=1, row_span=1)
            for c in stat_card_data
        ],
        rx.chakra.grid_item(
            line_chart_component,
            col_span=4,
            row_span=2,
        ),
        rx.chakra.grid_item(table(tabular_data=tabular_data), col_span=4, row_span=2),
        rx.chakra.grid_item(
            area_chart(data=area_chart_data, data_key="name", areas=areas),
            col_span=3,
            row_span=2,
        ),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )

@template
def index() -> rx.Component:
    return rx.box(
        navbar(heading="Inicio"),
        rx.box(
            content_grid(),
            margin_top="calc(50px + 2em)",
            padding="2em",
        ),
        padding_left="250px",
    )
