import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My first app')

st.write('progress bar')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!'


st.write('dataframe')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')

if button:
    right_column.write('ここは右カラム')

st.write('checkbox')
if st.sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

Text = st.sidebar.text_input('Your name', value='default value')
'your name is ', Text

options = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', options

options = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))

'You selected: ', options


