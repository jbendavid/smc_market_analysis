import streamlit as st
import pandas as pd
import plotly.express as px

# Example Data
data = {
    'market': ['Athletic Monitoring Device Adhesives', 'UV Detection', 'Postpartum Care', 'Agritech'],
    'market_value': [8,3,7,6],
    'barrier_to_entry': [4,2,5,8],
    'market_maturity_stability': [4,5,8,7],
}
df = pd.DataFrame(data)
#df.set_index('market', inplace = True)

# Streamlit App Layout
st.title("Market Analysis")

x_axis = st.selectbox(
    "Select X-axis metric",
    options=[col for col in df.columns if col != 'market'],
    index=0
)

y_axis = st.selectbox(
    "Select Y-axis metric",
    options=[col for col in df.columns if col != 'market'],
    index=1
)

bubble_size = st.selectbox(
    "Select Bubble Size metric",
    options=[col for col in df.columns if col != 'market'],
    index=0
)

# Plotting Bubble Plot
fig = px.scatter(df, x=x_axis, y=y_axis, size=bubble_size,
                 color='market', hover_name='market',
                 size_max=60)

fig.update_layout(title=f'Market Analysis ({x_axis} vs {y_axis})',
                  xaxis_title=x_axis, yaxis_title=y_axis)

st.plotly_chart(fig)
