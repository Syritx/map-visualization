import folium
import os
import pandas as pd

states = os.path.join('data', 'us-states.json')

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=states,
    name='choropleth',
    data=pd.read_csv(os.path.join('data','state-data.csv')),
    columns=['State', 'GDP'],
    key_on='feature.id',
    fill_color='BuGn',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='GDP (in Billions)'
)

folium.LayerControl().add_to(m)

m.save('index.html')