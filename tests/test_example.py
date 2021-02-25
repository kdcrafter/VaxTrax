import dash
import dash_html_components as html

from us_today import us_layout

def test_us001_simple_example(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1('Hello'),
    ])
    dash_duo.start_server(app)

    dash_duo.percy_snapshot('us001_example')