import folium
from folium import plugins
import pandas as pd

covid = pd.read_csv('IDN-COVID19.csv')
covid.head()

maps1 = folium.Map(location= [3.100, 115.850], zoom_start=5)

confirmed = folium.FeatureGroup(name='Confirmed')
maps1.add_child(confirmed)

# icon
for i in covid.itertuples():
    confirmed.add_child(folium.Marker(location=[i.lat, i.long],
                  popup= i.Province_name,
                  icon=plugins.BeautifyIcon(number=i.Confirmed_cases,
                                            border_color='black',
                                            border_width=2,
                                            text_color='blue',
                                            inner_icon_style='margin-top:0px;')))

recover = folium.FeatureGroup(name='Recovered')
maps1.add_child(recover)

# icon
for i in covid.itertuples():
    recover.add_child(folium.Marker(location=[i.lat, i.long],
                  popup= i.Province_name,
                  icon=plugins.BeautifyIcon(number=i.Recovered_cases,
                                            border_color='black',
                                            border_width=2,
                                            text_color='green',
                                            inner_icon_style='margin-top:0px;')))

death = folium.FeatureGroup(name='Death')
maps1.add_child(death)

# icon
for i in covid.itertuples():
    death.add_child(folium.Marker(location=[i.lat, i.long],
                  popup= i.Province_name,
                  icon=plugins.BeautifyIcon(number=i.Death_cases,
                                            border_color='black',
                                            border_width=2,
                                            text_color='red',
                                            inner_icon_style='margin-top:0px;')))

maps1.add_child(folium.LayerControl(collapsed=False))
