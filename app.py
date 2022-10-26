import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('SampleSuperstore.csv')  


#plot1
fig1=plt.figure(figsize=(15,12))
sns.countplot(x='State',data=df,palette='rocket_r',order=df['State'].value_counts().index)
plt.xticks(rotation=90)
st.pyplot(fig1)


#various plot-2
ps = df.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
state = st.selectbox("Select State: ", list(ps.index))
fig, ax = plt.subplots(figsize=(2,3))
ax.set_title(state.upper()+ " Sales and Profit")

ind = 1  # the x locations for the groups
width = 0.35 

ax.set_xticks([])
ax.set_xlabel(state)

ax.bar(ind, ps.loc[state]['Sales'], width, color='royalblue')
ax.bar(ind+width, ps.loc[state]['Profit'], width, color='orange')

st.pyplot(fig)

#plot-3
df['Postal Code'] = df['Postal Code'].astype('object')
df.drop_duplicates(subset=None,keep='first',inplace=True)
corr = df.corr()
fig2 = plt.figure(figsize=(10, 4))
sns.heatmap(corr,annot=True,cmap='Reds')
st.pyplot(fig2)

#plot4
df['Region'].value_counts().plot.pie(autopct = '%1.1f%%')
fig4=plt.figure(figsize=(10,8))
st.pyplot(fig4)

#plot5 and plot6: No correlation between profit and discount 
#plot5
fig5,ax=plt.subplots(figsize=(20,8))
ax.scatter(df['Sales'],df['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
st.pyplot(fig5)

#plot6
fig6=plt.figure(figsize=(10,4))
sns.lineplot(x='Discount',y='Profit',label='Profit',data=df)
st.pyplot(fig6)

#plot7
fig6=pl7figure(figsize=(10,4))
sns.lineplot(x='Quantity',y='Profit',label='Profit',data=df)
st.pyplot(fig7)

#plot8
fig8=plt.figure(figsize=(10,8))
ps1=df.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['pink','blue'],figsize=(8,5))
ps2=df.plt.ylabel('Profit/Loss and sales')
st.pyplot(fig8)




