import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv')

state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York State': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME', 'American Samoa' : '', 'Bureau of Prisons' : '', 'Dept of Defense' : '',
    'Federated States of Micronesia' : '', 'Guam' : '', 'Indian Health Svc' : '', 'Long Term Care' : '', 'Marshall Islands' : '',
    'Northern Mariana Islands':'MP', 'Puerto Rico': 'PR', 'Republic of Palau' : '', 'United States' : '', 'Veterans Health' : '',
    'Virgin Islands' : ''
    }

df['location'] = df['location'].apply(lambda x : state_codes[x])

df = df.sort_values(by=['date'])
df_latest = df[df.date == df.date.max()]
df_latest.head()

fig = go.Figure(data=go.Choropleth(
   
    locations=df_latest['location'], # Spatial coordinates
    z = df_latest['total_vaccinations'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    autocolorscale=False,
    marker_line_color='white',
    colorbar_title = "Population",
))

fig.update_layout(
    title_text = '2021 US Total Vaccination for Today',
    geo_scope='usa', # limite map scope to USA
)

us_layout = html.Div([
    html.Div(id='test'),
    dcc.Graph(
        id='us-total-vaccination-today',
        figure=fig
    )
])