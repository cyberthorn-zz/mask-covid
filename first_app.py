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

toongkru['datetime'] = toongkru['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

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

rama4_2['datetime'] = rama4_2['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

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

rama1_2['datetime'] = rama1_2['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

rama1_2 = rama1_2[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]
rama1_2.set_index('datetime', inplace=True)
#--------------------------------------------------------------------------

rajdamri_1 = mask_time[mask_time['name'] == "แนวถนนราชดำริ1"]
rajdamri_1.reset_index(inplace=True)

rajdamri_1['correct_wear_mask_minute'] = rajdamri_1['no_correct_wear_mask'].diff()
rajdamri_1.loc[0, 'correct_wear_mask_minute'] = rajdamri_1.loc[0, 'no_correct_wear_mask']

rajdamri_1['incorrect_wear_mask_minute'] = rajdamri_1['no_incorrect_wear_mask'].diff()
rajdamri_1.loc[0, 'incorrect_wear_mask_minute'] = rajdamri_1.loc[0, 'no_incorrect_wear_mask']

rajdamri_1['no_not_wear_mask_minute'] = rajdamri_1['no_not_wear_mask'].diff()
rajdamri_1.loc[0, 'no_not_wear_mask_minute'] = rajdamri_1.loc[0, 'no_not_wear_mask']

rajdamri_1['total_minute'] = rajdamri_1['total'].diff()
rajdamri_1.loc[0, 'total_minute'] = rajdamri_1.loc[0, 'total']

rajdamri_1['datetime'] = rajdamri_1['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

rajdamri_1 = rajdamri_1[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rajdamri_1.set_index('datetime', inplace=True)

#------------------------------------------------------------
rajdamri21 = mask_time[mask_time['name'] == "แนวถนนราชดำริ2-1"]
rajdamri21.reset_index(inplace=True)

rajdamri21['correct_wear_mask_minute'] = rajdamri21['no_correct_wear_mask'].diff()
rajdamri21.loc[0, 'correct_wear_mask_minute'] = rajdamri21.loc[0, 'no_correct_wear_mask']

rajdamri21['incorrect_wear_mask_minute'] = rajdamri21['no_incorrect_wear_mask'].diff()
rajdamri21.loc[0, 'incorrect_wear_mask_minute'] = rajdamri21.loc[0, 'no_incorrect_wear_mask']

rajdamri21['no_not_wear_mask_minute'] = rajdamri21['no_not_wear_mask'].diff()
rajdamri21.loc[0, 'no_not_wear_mask_minute'] = rajdamri21.loc[0, 'no_not_wear_mask']

rajdamri21['total_minute'] = rajdamri21['total'].diff()
rajdamri21.loc[0, 'total_minute'] = rajdamri21.loc[0, 'total']

rajdamri21['datetime'] = rajdamri21['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

rajdamri21 = rajdamri21[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rajdamri21.set_index('datetime', inplace=True)

#-----------------------------------------------------------------
rama1_1 = mask_time[mask_time['name'] == "แนวถนนพระราม1-1"]
rama1_1.reset_index(inplace=True)

rama1_1['correct_wear_mask_minute'] = rama1_1['no_correct_wear_mask'].diff()
rama1_1.loc[0, 'correct_wear_mask_minute'] = rama1_1.loc[0, 'no_correct_wear_mask']

rama1_1['incorrect_wear_mask_minute'] = rama1_1['no_incorrect_wear_mask'].diff()
rama1_1.loc[0, 'incorrect_wear_mask_minute'] = rama1_1.loc[0, 'no_incorrect_wear_mask']

rama1_1['no_not_wear_mask_minute'] = rama1_1['no_not_wear_mask'].diff()
rama1_1.loc[0, 'no_not_wear_mask_minute'] = rama1_1.loc[0, 'no_not_wear_mask']

rama1_1['total_minute'] = rama1_1['total'].diff()
rama1_1.loc[0, 'total_minute'] = rama1_1.loc[0, 'total']

rama1_1['datetime'] = rama1_1['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

rama1_1 = rama1_1[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rama1_1.set_index('datetime', inplace=True)

#-------------------------------------------------------

pharma1_2 = mask_time[mask_time['name'] == "หน้าองค์การเภสัช1-2"]
pharma1_2.reset_index(inplace=True)

pharma1_2['correct_wear_mask_minute'] = pharma1_2['no_correct_wear_mask'].diff()
pharma1_2.loc[0, 'correct_wear_mask_minute'] = pharma1_2.loc[0, 'no_correct_wear_mask']

pharma1_2['incorrect_wear_mask_minute'] = pharma1_2['no_incorrect_wear_mask'].diff()
pharma1_2.loc[0, 'incorrect_wear_mask_minute'] = pharma1_2.loc[0, 'no_incorrect_wear_mask']

pharma1_2['no_not_wear_mask_minute'] = pharma1_2['no_not_wear_mask'].diff()
pharma1_2.loc[0, 'no_not_wear_mask_minute'] = pharma1_2.loc[0, 'no_not_wear_mask']

pharma1_2['total_minute'] = pharma1_2['total'].diff()
pharma1_2.loc[0, 'total_minute'] = pharma1_2.loc[0, 'total']

pharma1_2['datetime'] = pharma1_2['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

pharma1_2 = pharma1_2[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

pharma1_2.set_index('datetime', inplace=True)

#-------------------------------------------------------------

rajdamri2_2 = mask_time[mask_time['name'] == "แนวถนนราชดำริ2-2"]
rajdamri2_2.reset_index(inplace=True)

rajdamri2_2['correct_wear_mask_minute'] = rajdamri2_2['no_correct_wear_mask'].diff()
rajdamri2_2.loc[0, 'correct_wear_mask_minute'] = rajdamri2_2.loc[0, 'no_correct_wear_mask']

rajdamri2_2['incorrect_wear_mask_minute'] = rajdamri2_2['no_incorrect_wear_mask'].diff()
rajdamri2_2.loc[0, 'incorrect_wear_mask_minute'] = rajdamri2_2.loc[0, 'no_incorrect_wear_mask']

rajdamri2_2['no_not_wear_mask_minute'] = rajdamri2_2['no_not_wear_mask'].diff()
rajdamri2_2.loc[0, 'no_not_wear_mask_minute'] = rajdamri2_2.loc[0, 'no_not_wear_mask']

rajdamri2_2['total_minute'] = rajdamri2_2['total'].diff()
rajdamri2_2.loc[0, 'total_minute'] = rajdamri2_2.loc[0, 'total']

rajdamri2_2['datetime'] = rajdamri2_2['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

rajdamri2_2 = rajdamri2_2[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

rajdamri2_2.set_index('datetime', inplace=True)

#-------------------------------------------------------
pharma1_1 = mask_time[mask_time['name'] == "หน้าองค์การเภสัช1-1"]
pharma1_1.reset_index(inplace=True)

pharma1_1['correct_wear_mask_minute'] = pharma1_1['no_correct_wear_mask'].diff()
pharma1_1.loc[0, 'correct_wear_mask_minute'] = pharma1_1.loc[0, 'no_correct_wear_mask']

pharma1_1['incorrect_wear_mask_minute'] = pharma1_1['no_incorrect_wear_mask'].diff()
pharma1_1.loc[0, 'incorrect_wear_mask_minute'] = pharma1_1.loc[0, 'no_incorrect_wear_mask']

pharma1_1['no_not_wear_mask_minute'] = pharma1_1['no_not_wear_mask'].diff()
pharma1_1.loc[0, 'no_not_wear_mask_minute'] = pharma1_1.loc[0, 'no_not_wear_mask']

pharma1_1['total_minute'] = pharma1_1['total'].diff()
pharma1_1.loc[0, 'total_minute'] = pharma1_1.loc[0, 'total']

pharma1_1['datetime'] = pharma1_1['date'].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

pharma1_1 = pharma1_1[['correct_wear_mask_minute', "incorrect_wear_mask_minute", "no_not_wear_mask_minute", "datetime" ]]

pharma1_1.set_index('datetime', inplace=True)


st.title('SuperAI deep application')
st.header('DeepCare')
# st.write(mask)
st.write(mask)

st.text("กราฟจำนวนผู้ใส่หน้ากาก ของแต่ละพื้นที่")
st.bar_chart(maskgraph)

st.text("กราฟสัดส้วนผู้ใส่หน้ากาก ของแต่ละพื้นที่")
st.bar_chart(maskgraph_percent)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก ของตลาดทุ่งครุ ต่อ 1 นาที")
st.bar_chart(toongkru)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนพระราม4-2 ต่อ 1 นาที")
st.bar_chart(rama4_2)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนพระราม1-2 ต่อ 1 นาที")
st.bar_chart(rama1_2)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนราชดำริ1 ต่อ 1 นาที")
st.bar_chart(rajdamri_1)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนราชดำริ2_1 ต่อ 1 นาที")
st.bar_chart(rajdamri21)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนพระราม1-1 ต่อ 1 นาที")
st.bar_chart(rama1_1)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก หน้าองค์การเภสัช1-2 ต่อ 1 นาที")
st.bar_chart(pharma1_2)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก แนวถนนราชดำริ2-2 ต่อ 1 นาที")
st.bar_chart(rajdamri2_2)

st.text("กราฟจำนวน ผู้ใส่หน้ากาก หน้าองค์การเภสัช1-1 ต่อ 1 นาที")
st.bar_chart(pharma1_1)

# c = alt.Chart(mask).mark_circle().encode(x='no_correct_wear_mask', y='no_incorrect_wear_mask', size='no_not_wear_mask', color='c', tooltip=['no_correct_wear_mask', 'no_incorrect_wear_mask', 'no_not_wear_mask'])

# st.write(c)