import plotly.graph_objects as go
values = [0,10,30,50,100]
A = [1,2,6,11,5]
B = [3,5,5,3,9]
fig = go.Figure()
fig.add_trace(go.Bar(x=values,y=A,name='Tireur A',))
fig.add_trace(go.Bar(x=values,y=B,name='Tireur B',))

fig.update_layout(
    title='Répartition des tirs',
    xaxis=dict(
        title='Score',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Effectif',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()
