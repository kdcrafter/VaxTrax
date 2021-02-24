import dash
import dash_html_components as html

from us_today import us_layout

def test_us001_simple_example(dash_duo):
    app = dash.Dash(__name__)
    app.layout = us_layout
    dash_duo.start_server(app)

    dash_duo.wait_for_element_by_id('us-total-vaccination-today')

    dash_duo.percy_snapshot("us001_example")

def test_us001_fail_example(dash_duo):
    assert False