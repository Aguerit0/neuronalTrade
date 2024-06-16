"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from neuronalTrade.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from neuronalTrade.pages.cryptomap import tools
from neuronalTrade.pages.alerts import team
from neuronalTrade.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/alerts")
app.add_page(team, route="/cryptomap")
app.add_page(team, route="/indicators")
app.add_page(team, route="/predicts")

