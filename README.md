Project Goal: Understanding local magnitude's dependency on an earthquake's frequency spectrum.<br/>

Project Workflow: Filtered seismograms using metadata, applied Hanning taper to smoothen time series data, converted to frequency domain. Performed component-wise (E,H,Z) magnitude estimation. Calculated the R2 score and compared across components.<br/>

Magnitude estimation (for each component): Sent amplitudes in frequency domain as inputs, computed attention scores of amplitudes using Bahdanau et. al's (https://arxiv.org/abs/1409.0473) additive attention mechanism, filtered using maxpooling layers, learned temporal dependencies using bidirectional LSTMs, used a fully connected layer as the final layer.<br/>

Skills demonstrated: EDA using Pandas, NumPy; Supervised learning using Keras and Tensorflow; Built custom attention and embedding layers using Keras backend; Visualisations using Matplotlib, Seaborn and Plotly.<br/>

Dataset used: Local magnitude traces from chunk2 and chunk3 of STEAD (Mousavi et al., 2019; https://github.com/smousavi05/STEAD)<br/>

Files in this repository:<br/>

main_nb.ipynb - main notebook for magnitude estimation<br/>
metadata_proc.py - contains code for data preprocessing<br/>
sigproc.py - contains code for transforming the data<br/>
trace_viz.py - code for visualising traces<br/>
layers_class.py - code for attention mechanism and optional embedding layer
