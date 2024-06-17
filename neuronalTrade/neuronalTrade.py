"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from neuronalTrade.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from neuronalTrade.pages.cryptomap import cryptomap
from neuronalTrade.pages.indicators import indicators
from neuronalTrade.pages.predicts import predicts
from neuronalTrade.pages.alerts import alerts
from neuronalTrade.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(indicators, route="/indicators")
app.add_page(predicts, route="/predicts")
app.add_page(cryptomap, route="/cryptomap")
app.add_page(alerts, route="/alerts")
