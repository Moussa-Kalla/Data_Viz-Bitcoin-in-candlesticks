from dash import Input, Output
import plotly.graph_objects as go
import pandas as pd

def register_callbacks(app):
    # Charger les données
    df = pd.read_csv('Data/Btc_Perp_USD.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df = df.sort_index()
    
    @app.callback(
        Output('bitcoin-chart', 'figure'),
        [Input('time-interval', 'value'),
         Input('ma-type', 'value'),
         Input('date-range', 'start_date'),
         Input('date-range', 'end_date')]
    )
    def update_chart(time_interval, ma_type, start_date, end_date):
        filtered_df = df.loc[start_date:end_date]
        resampled = filtered_df['price'].resample(time_interval).ohlc()
        
        if ma_type == "SMA":
            resampled['MA'] = resampled['close'].rolling(window=10).mean()
        elif ma_type == "EMA":
            resampled['MA'] = resampled['close'].ewm(span=10).mean()
        
        fig = go.Figure(data=[
            go.Candlestick(
                x=resampled.index,
                open=resampled['open'],
                high=resampled['high'],
                low=resampled['low'],
                close=resampled['close'],
                name="Chandeliers"
            ),
            go.Scatter(
                x=resampled.index,
                y=resampled['MA'],
                mode='lines',
                name=f"{ma_type} (10 périodes)",
                line=dict(color="orange")
            )
        ])
        fig.update_layout(
            title="Graphique Bitcoin",
            xaxis_title="Temps",
            yaxis_title="Prix",
            template="plotly_dark" if app.server.config.get('THEME') == "dark" else "plotly",
        )
        return fig
    
    @app.callback(
        Output('main-container', 'className'),
        Input('theme-toggle', 'value')
    )
    def toggle_theme(value):
        return "dark-mode" if value else "light-mode"