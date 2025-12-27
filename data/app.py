import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from pathlib import Path

df = pd.read_csv("data/formatted_sales.csv", parse_dates=["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(className="container", children=[
    html.H1("Pink Morsel Sales Visualiser"),

    html.P("Filter sales by region:"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        className="radio"
    ),

    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df
    else:
        filtered = df[df["Region"].str.lower() == region]

    fig = px.line(
        filtered,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig

if __name__ == "__main__":
    print("Starting Dash server at http://127.0.0.1:8050/")
    app.run(debug=True, host="127.0.0.1", port=8050, use_reloader=False)
