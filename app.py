import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')




df = pd.read_csv('SampleSuperstore.csv')  
df['Postal Code'] = df['Postal Code'].astype('object')
df.drop_duplicates(subset=None,keep='first',inplace=True)
corr = df.corr()

fig = plt.figure(figsize=(10, 4))

sns.heatmap(corr,annot=True,cmap='Reds')

st.pyplot(fig)