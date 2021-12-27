import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from ..app import config_plots

def charts(clean_data):
    """
    Build the charts.

    This function uses the ``clean_data`` parameter
    and uses the data to build charts.

    Parameters
    ----------
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames to use as
        data in the charts.

    Returns
    -------
    dict
        Dictionary of Plotly charts.
    """
    chart_knob_1 = daq.Gauge(
                        id='my-gauge',
                        label="Default",
                        value=6,
                        style={'display': 'block' }
                        )

    return {"chart-knob-1": chart_knob_1,
            }


def app_content(charts, clean_data):
    """
    Build the html components.

    Use html components with ``charts`` parameters
    to build the layout of the dashboard.

    Parameters
    ----------
    charts : dict of {str : plotly.graph_objects or plotly.express}
        Dictionary that contains the charts.
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames, but the 
        integer values are used to build summary cards.

    Returns
    -------
    html.Div
        Div component of the dash_html_components.html.Div.
    """
    row_1 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(daq.Gauge(
                        id='my-gauge_app2-1',
                        label="Default",
                        value=6,
                        style={'display': 'block' }
                        ), className='shadow cards-info'), className='mb-4 col-lg-6 col-md-12 col-sm-12 col-xs-12 col-12'),
                    dbc.Col(dbc.Card(daq.Gauge(
                        id='my-gauge_app2-2',
                        label="Default",
                        value=6,
                        style={'display': 'block' }
                        ), className='shadow cards-info'), className='mb-4 col-lg-6 col-md-12 col-sm-12 col-xs-12 col-12'),
                ],
            ),
        ]
    )

    return html.Div([html.Div([row_1])])


def layout(clean_data):
    """
    Build the html layout of the first tab.

    This function uses :func:`_charts` and :func:`_app_content` to fill the
    layout of the tab using Dash application components.

    Parameters
    ----------
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames to use as
        data in the charts.

    Returns
    -------
    dash_html_components.html
        Html component composed of charts.
    """
    return app_content(charts(clean_data), clean_data)