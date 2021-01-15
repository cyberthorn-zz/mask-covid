import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

DATA_PATH=('./result_debug.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(DATA_PATH)
    return data.set_index('date')

df=load_data()

countries = st.multiselect("Choose countries", list(df.index), ["China", "United States of America"])
if not countries:
    st.error("Please select at least one country.")
else:
    data = df.loc[countries]
    data /= 1000000.0
    st.write("### Gross Agricultural Production ($B)", data.sort_index())
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(columns={"index": "year", "value": "Gross Agricultural Product ($B)"})
    chart = (
        alt.Chart(data).mark_area(opacity=0.3).encode(x="year:T",y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),color="Region:N",)
        )
    st.altair_chart(chart, use_container_width=True)

#st.sidebar.checkbox("Show Analysis by State", True, key=1)
#select = st.sidebar.selectbox('Name area',df['name'])

#get the state selected in the selectbox
#state_data = df[df['name'] == select]
#select_status = st.sidebar.radio("Sor Kor Bor Mask status", ('no_correct_wear_mask',
#'no_incorrect_wear_mask', 'no_not_wear_mask', 'total'))

def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['no_correct_wear_mask','no_incorrect_wear_mask', 'no_not_wear_mask', 'total'],
    'Number of cases':(dataset.iloc[0]['total'],
    dataset.iloc[0]['total'], 
    dataset.iloc[0]['total'],dataset.iloc[0]['total'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("แสดงผลการวิเคราะห์ข้อมูล", True, key=2):
    st.markdown("## **ข้อมูลสรุปผู้ที่สวมใส่หน้ากากอนามัน**")
    st.markdown("### ผู้สวมหน้ากากจากกาวิเคราะห์ภาพจาก CCTV " +
    "ข้อมูลจากพื้นที่ %s (เฉพาะใน กทม)" % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (select)},
        color='Status')
        st.plotly_chart(state_total_graph)

def get_table():
    datatable = df[['no_correct_wear_mask','no_incorrect_wear_mask', 'no_not_wear_mask', 'total']].sort_values(by=['total'], ascending=False)
    #datatable = datatable[datatable['name'] != 'name Unassigned']
    return datatable

datatable = get_table()
st.markdown("### Covid-19 cases in Thailand")
st.markdown("ข้อมูลแสดงผู้สวมใส่หน้ากากอนามัยจากฐานข้อมูล")
st.dataframe(datatable) # will display the dataframe
st.table(datatable)# will display the table