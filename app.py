import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data 1990')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)  # min, max, default
#slider 滑动块

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


# 使用 Streamlit 的 radio 按钮来选择收入级别
income_level = st.sidebar.radio(
    "Select income level:",
    ('Low', 'Medium', 'High')
)


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low (≤2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# show on map
st.map(filtered_df)



value_counts = df['median_house_value'].value_counts().sort_index()

# 绘制频率分布图
fig, ax = plt.subplots(figsize = (20, 20))
ax.hist(filtered_df['median_house_value'], bins = 30)

# 添加标签和标题
ax.set_xlabel('Median House Value', fontsize = 12)
ax.set_ylabel('Frequency', fontsize = 12)
ax.set_title('Frequency Distribution of Median House Value', fontsize = 16)

# 在Streamlit中显示图表
st.pyplot(fig)