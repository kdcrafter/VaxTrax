import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_setup import app
from us_today import us_layout

application = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback for navigating between home and citations page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              dash.dependencies.Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' or pathname == '/us-today':
        return us_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)