import reflex as rx

from neuronalTrade.navigation import navbar
from neuronalTrade.template import template

"""The main index page."""

import reflex as rx
from neuronalTrade.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    area_chart_data,
    areas,
    stat_card_data,
    tabular_data,
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
            rx.chakra.grid_item(stat_card(*c), col_span=3, row_span=3)
            for c in stat_card_data
        ],
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )


@template
def indicators() -> rx.Component:
    return rx.box(
            navbar(heading="Indicadores"),
            rx.box(
                content_grid(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
