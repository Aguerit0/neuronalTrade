import reflex as rx

from neuronalTrade.navigation import navbar
from neuronalTrade.template import template

@template
def alerts() -> rx.Component:
    return rx.box(
            navbar(heading="Alertas"),
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )

