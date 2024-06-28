# apps/heatmap/views.py
from django.shortcuts import render
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio

def heatmap_view(request):
    fig = go.Figure(data=go.Scatter(
        template = 'plotly_dark',
        y=np.random.randn(500),
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(500),
            colorscale='Viridis',
            showscale=True
        )
    ))
    graph_html = pio.to_html(fig, full_html=False)
    return render(request, 'heatmap/heatmap.html', {'graph_html': graph_html})
