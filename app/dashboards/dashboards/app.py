import plotly.io as pio
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

EXTERNAL_SCRIPTS = ["https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.49.5/plotly-locale-pt-br.js"]
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
app = DjangoDash('dsci_dashboard', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.UNITED, FONT_AWESOME],  external_scripts=EXTERNAL_SCRIPTS)

# translate tips to Brazilian Portuguese
config_plots = dict(locale='pt-br')