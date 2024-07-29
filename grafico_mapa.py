import pandas as pd
import plotly.express as px
import requests

def crear_grafico(df):
    # Descargar el archivo GeoJSON
    url_geojson = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    response = requests.get(url_geojson)
    brasil_geojson = response.json()

    # Agrupar por estado y calcular las métricas necesarias
    df_mapa = df.groupby('geolocation_state').agg({
        'valor_total': 'sum',
        'geolocation_lat': 'mean',
        'geolocation_lng': 'mean'
    }).reset_index().sort_values(by='valor_total', ascending=False)

    # Crear el gráfico
    graf_mapa = px.choropleth_mapbox(df_mapa,
                                     geojson=brasil_geojson,
                                     locations='geolocation_state',
                                     featureidkey="properties.sigla",
                                     color='valor_total',
                                     hover_name='geolocation_state',
                                     hover_data={'geolocation_lat': False, 'geolocation_lng': False},
                                     title='Ingresos por estado en Brasil',
                                     mapbox_style="carto-positron",
                                     center={"lat": -14.2350, "lon": -51.9253},
                                     zoom=3)

    return graf_mapa
