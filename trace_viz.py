import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

## Time domain traces for a single event ##
def tplot(x):
    y1 = x[0,:,0]                                   
    x1 = np.linspace(0,60,len(y1))

    fig = make_subplots(rows=3,cols=1,shared_xaxes=True,vertical_spacing=0.02,x_title='Time [in secs]',y_title='Amplitudes')
    fig.add_trace(go.Scatter(x=x1, y=x[0,:,0],name='E component'),row=1,col=1)
    fig.add_trace(go.Scatter(x=x1, y=x[0,:,1],name='N component'),row=2,col=1)
    fig.add_trace(go.Scatter(x=x1, y=x[0,:,2],name='Z component'),row=3,col=1)
    fig.update_layout(height=1200,width=1200,
        font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
        )
    )

    fig.show()



## Frequency domain traces for a single event ##
def fplot(fr):
    sr = 100
    fny = sr / 2.0
    v = fr[0,:,0]
    m = np.linspace(0,fny,len(v))

    fig1 = make_subplots(rows=3,cols=1,shared_xaxes=True,vertical_spacing=0.02,x_title='Frequency [Hz]',y_title='Amplitudes')
    fig1.add_trace(go.Scatter(x=m, y=fr[0,:,0],name='E component'),row=1,col=1)
    fig1.add_trace(go.Scatter(x=m, y=fr[0,:,1],name='N component'),row=2,col=1)
    fig1.add_trace(go.Scatter(x=m, y=fr[0,:,2],name='Z component'),row=3,col=1)
    fig1.update_layout(height=1200,width=1200,
        font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
        )
    )

    fig1.show()