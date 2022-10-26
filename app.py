import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



df = pd.read_csv('SampleSuperstore.csv')  
# df['Postal Code'] = df['Postal Code'].astype('object')
# df.drop_duplicates(subset=None,keep='first',inplace=True)
# corr = df.corr()

# fig = plt.figure(figsize=(10, 4))

# sns.heatmap(corr,annot=True,cmap='Reds')

# st.pyplot(fig)

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


fig=plt.figure(figsize=(15,12))
sns.countplot(x='State',data=df,palette='rocket_r',order=df['State'].value_counts().index)
plt.xticks(rotation=90)
st.pyplot(fig)
