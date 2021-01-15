# This is a sample Python script.
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime, date, time
import altair as alt
import numpy as np
import urllib
from urllib import error


mask = pd.read_csv(r'result_debug.csv')

mask_people = mask[['name', 'no_correct_wear_mask', 'no_incorrect_wear_mask', "no_not_wear_mask"]]
maskgraph = mask_people.groupby(['name']).agg('max')
maskgraph_percent = maskgraph.copy()
maskgraph_percent['sum'] = maskgraph['no_correct_wear_mask'] + maskgraph['no_incorrect_wear_mask'] + maskgraph['no_not_wear_mask']
maskgraph_percent["percent_correct"] = maskgraph_percent['no_correct_wear_mask']/maskgraph_percent['sum']*100
maskgraph_percent["percent_incorrect"] = maskgraph_percent['no_incorrect_wear_mask']/maskgraph_percent['sum']*100
maskgraph_percent["percent_not_wear_mask"] = maskgraph_percent['no_not_wear_mask']/maskgraph_percent['sum']*100
maskgraph_percent = maskgraph_percent[["percent_correct", "percent_incorrect", "percent_not_wear_mask"]]


mask_by_time = mask[['date', "name", "no_correct_wear_mask" , "no_incorrect_wear_mask", "no_not_wear_mask", "total"]]
mask_by_time['date'] = pd.to_datetime(mask_by_time['date'])
mask_by_time['minute'] = mask_by_time.date.dt.minute
mask_by_time['hour'] = mask_by_time.date.dt.hour
mask_by_time['day'] = mask_by_time.date.dt.day
mask_time = mask_by_time.groupby(['day', 'hour', 'minute', 'name']).agg('max')

mask_time.reset_index(inplace=True)


toongkru = mask_time[mask_time['name'] == "ตลาดทุ่งครุ"]
toongkru['correct_wear_mask_minute'] = toongkru['no_correct_wear_mask'].diff()
toongkru.loc[0, 'correct_wear_mask_minute'] = toongkru.loc[0, 'no_correct_wear_mask']

toongkru['incorrect_wear_mask_minute'] = toongkru['no_incorrect_wear_mask'].diff()
toongkru.loc[0, 'incorrect_wear_mask_minute'] = toongkru.loc[0, 'no_incorrect_wear_mask']

toongkru['no_not_wear_mask_minute'] = toongkru['no_not_wear_mask'].diff()
toongkru.loc[0, 'no_not_wear_mask_minute'] = toongkru.loc[0, 'no_not_wear_mask']

toongkru['total_minute'] = toongkru['total'].diff()
toongkru.loc[0, 'total_minute'] = toongkru.loc[0, 'total']

toongkru['datetime'] = toongkru['date'].dt.date.astype(str) + " " + toongkru['hour'].astype(str) +":" + toongkru['minute'].astype(str)

toongkru = toongkru[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

toongkru.set_index('datetime', inplace=True)

rama4_2 = mask_time[mask_time['name'] == "แนวถนนพระราม4-2"]
rama4_2.reset_index(inplace=True)

rama4_2['correct_wear_mask_minute'] = rama4_2['no_correct_wear_mask'].diff()
rama4_2.loc[0, 'correct_wear_mask_minute'] = rama4_2.loc[0, 'no_correct_wear_mask']

rama4_2['incorrect_wear_mask_minute'] = rama4_2['no_incorrect_wear_mask'].diff()
rama4_2.loc[0, 'incorrect_wear_mask_minute'] = rama4_2.loc[0, 'no_incorrect_wear_mask']

rama4_2['no_not_wear_mask_minute'] = rama4_2['no_not_wear_mask'].diff()
rama4_2.loc[0, 'no_not_wear_mask_minute'] = rama4_2.loc[0, 'no_not_wear_mask']

rama4_2['total_minute'] = rama4_2['total'].diff()
rama4_2.loc[0, 'total_minute'] = rama4_2.loc[0, 'total']

rama4_2['datetime'] = rama4_2['date'].dt.date.astype(str) + " " + rama4_2['hour'].astype(str) +":" + rama4_2['minute'].astype(str)

rama4_2 = rama4_2[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rama4_2.set_index('datetime', inplace=True)

#------------------------------------------------------------------------------------

rama1_2 = mask_time[mask_time['name'] == "แนวถนนพระราม1-2"]
rama1_2.reset_index(inplace=True)

rama1_2['correct_wear_mask_minute'] = rama1_2['no_correct_wear_mask'].diff()
rama1_2.loc[0, 'correct_wear_mask_minute'] = rama1_2.loc[0, 'no_correct_wear_mask']

rama1_2['incorrect_wear_mask_minute'] = rama1_2['no_incorrect_wear_mask'].diff()
rama1_2.loc[0, 'incorrect_wear_mask_minute'] = rama1_2.loc[0, 'no_incorrect_wear_mask']

rama1_2['no_not_wear_mask_minute'] = rama1_2['no_not_wear_mask'].diff()
rama1_2.loc[0, 'no_not_wear_mask_minute'] = rama1_2.loc[0, 'no_not_wear_mask']

rama1_2['total_minute'] = rama1_2['total'].diff()
rama1_2.loc[0, 'total_minute'] = rama1_2.loc[0, 'total']

rama1_2['datetime'] = rama1_2['date'].dt.date.astype(str) + " " + rama1_2['hour'].astype(str) +":" + rama1_2['minute'].astype(str)

rama1_2 = rama1_2[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rama1_2.set_index('datetime', inplace=True)

st.title('SuperAI deep application 77')
st.header('DeepCare')
# st.write(mask)
st.write(mask)

st.bar_chart(maskgraph)
st.bar_chart(maskgraph_percent)
st.bar_chart(toongkru)
st.bar_chart(rama4_2)
st.bar_chart(rama1_2)
# c = alt.Chart(mask).mark_circle().encode(x='no_correct_wear_mask', y='no_incorrect_wear_mask', size='no_not_wear_mask', color='c', tooltip=['no_correct_wear_mask', 'no_incorrect_wear_mask', 'no_not_wear_mask'])

# st.write(c)