import pandas as pd
import plotly.express as px

def create_plot(coords, words):

    df = pd.DataFrame({
        "x": coords[:,0],
        "y": coords[:,1],
        "word": words
    })

    fig = px.scatter(
        df,
        x="x",
        y="y",
        text="word",
        title="Embedding Space"
    )

    fig.update_traces(
        textposition="top center"
    )

    return fig