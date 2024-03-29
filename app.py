import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

df = pd.read_csv("bank.csv")

st.set_page_config(
    page_title='lank',
    page_icon='🗺️',
    layout='wide'
)

st.title("Real-time Dashboard")

job_filter = st.selectbox("Select Job", pd.unique(df['job']))
placeholder = st.empty()
df = df[df['job'] == job_filter]

for seconds in range(200):
    df['age_new'] = df['age'] * np.random.choice(range(1, 5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1, 5))
    df['duration_new'] = df['duration'] * np.random.choice(range(1, 5))

    avg_age = np.mean(df['age_new'])
    count_married = int(df[(df["marital"] == 'married')]['marital'].count() + np.random.choice(range(1, 30)))
    balance = np.mean(df['balance_new'])
    avg_duration = np.mean(df['duration_new'])

    with placeholder.container():
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric(label="Average Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value=int(count_married), delta=-10 + count_married)
        kpi3.metric(label="Avg. Account Balance 💰", value=f"$ {round(balance, 2)}", delta=-round(balance / count_married) * 100)
        kpi4.metric(label="Avg. Call Duration 📞", value=round(avg_duration), delta=round(avg_duration) - 20)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("### Age Distribution by Marital Status")
            fig = px.density_heatmap(data_frame=df, y='age_new', x='marital')
            st.plotly_chart(fig)

        with col2:
            st.markdown("### Duration Distribution by Marital Status")
            fig3 = px.density_heatmap(data_frame=df, y='duration_new', x='marital')
            st.plotly_chart(fig3)

        col3, col4 = st.columns([1, 1])

        with col3:
            st.markdown("### Age Distribution")
            fig2 = px.histogram(data_frame=df, x='age_new')
            st.plotly_chart(fig2)

        with col4:
            st.markdown("### Duration Distribution")
            fig4 = px.histogram(data_frame=df, x='duration_new')
            st.plotly_chart(fig4)

        st.markdown("### Detailed Data View")
        st.dataframe(df)

        time.sleep(1)
