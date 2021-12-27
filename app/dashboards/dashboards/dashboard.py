import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from .app import app
from .apps import app_1, app_2

def server_layout():
    """
    Build the first layout.

    This function calls :func:`cleaning_data` to compute the
    input values of the charts, then it builds the layout of 
    the Dash application when it loads for the first time.

    Returns
    -------
    dash_html_components.html
        Html component composed of charts.
    """
    #clean_data_update = cleaning_data()
    clean_data_update = None
    #server_layout = html.Div([
    #    dbc.Tabs([dbc.Tab(app_1.layout(clean_data_update), label="Tab 1", tab_id='tab-1', tab_style={"marginLeft": "auto"}),
    #                dbc.Tab(app_2.layout(clean_data_update), label="Tab 2", tab_id='tab-2'),
    #                ], active_tab="tab-1", id="tabs", className='mb-3'),
    #    # interval = 10*60*1000 meaning minutes*seconds*milliseconds
    #    dcc.Interval(id='interval-component',interval=10*60*1000, n_intervals=0),
    #    ])
    server_layout = html.Div([
        app_1.layout(clean_data_update)
    ])

    return server_layout

@app.callback(Output('tabs', 'children'),[Input('interval-component', 'n_intervals')])
def update_metrics(n_intervals):
    """
    Build the updated layout.

    This function is a callback one triggered by the ``dcc.Interval`` component,
    then it calls :func:`cleaning_data` to compute the input values of the 
    charts, then it builds the updated layout of the Dash application.

    Parameters
    ----------
    n_intervals : int
        Value that represents how many updates have been happend
        already, it is not used.

    Returns
    -------
    list of dbc.Tabs
        Return a list of dbc.Tabs components to insert on html.Div.
    """
    #clean_data_update = cleaning_data()
    clean_data_update = None
    components = [dbc.Tab(app_1.layout(clean_data_update), label="Tab 1", tab_id='tab-1', tab_style={"marginLeft": "auto"}),
                  dbc.Tab(app_2.layout(clean_data_update), label="Tab 2", tab_id='tab-2'),
                  ]
    return components

app.layout = server_layout