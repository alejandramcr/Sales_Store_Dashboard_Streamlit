import pandas as pd
import plotly.express as px

def crear_grafico(df):
    revenues_monthly = df.set_index('order_purchase_timestamp').groupby(pd.Grouper(freq = 'ME'))['valor_total'].sum().reset_index()
    revenues_monthly['Year'] = revenues_monthly['order_purchase_timestamp'].dt.year
    revenues_monthly['Month'] = revenues_monthly['order_purchase_timestamp'].dt.month_name()
    revenues_monthly = revenues_monthly[revenues_monthly['Year'] > 2016]

    fig =px.line(revenues_monthly,
                 x = 'Month' ,
                 y = 'valor_total',
                 markers = True,
                 range_y = (0, revenues_monthly.max()),
                 color = 'Year',
                 line_dash = 'Year',
                 title = 'Ingresos mensuales'
                 )
    fig.update_layout(yaxis_title = 'Ingresos ($)')

    return fig