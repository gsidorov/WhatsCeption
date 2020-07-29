import streamlit as st
import pandas as pd
from methods import *
from charts import *


# Import chat
chat = create_chat_list()
chat = clean_chat_list(chat)

# Create df
df = chat_to_df(chat)


# Distribution chart
# as of 28/07 we are having issues with this 
# distribution_day = message_distribution_plot(df,'day')


# Web app:

# Comments and interesting links

st.title('_WhatsCeption_ - My first webapp :sunglasses:') # Underscore to denote curvy words

'# SITE TO DEPLOY https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83'

'### How to show matplot libcharts streamlit? Check this: https://docs.streamlit.io/en/stable/api.html#display-charts'

'## Web scrape from (reddit, 4chan, etc.) and substitute them from your conversation with Nacho'

'## Great post that covers deployment with Heroku: https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83'

'## Linking heroku app with domain: https://medium.com/@imranhsayed/adding-your-custom-domain-to-heroku-app-cdd68d2db67f'

'If instead you want to plot graphs from libraries like Matplotlib, altair, pyplot check: '
'https://docs.streamlit.io/en/stable/api.html#display-charts'

# Actual app

st.write("""
# WhatsCeption :sunglasses: by Gleb Sidorov 
Shown are the details of your **Whatsapp conversation**
Enjoy!
""")

"## This library is literally overpowered"


# I HAVE DEACTIVATED THE FILE UPLOADER BUT THIS IS SOMETHING THAT I WANT TO USE
st.file_uploader('Import the txt file of your Whatsapp conversation')


if st.button('CLICK HERE TO GENERATE STATISTICS'):
    st.write('you got fooled loll')

" I think this is how you display a plotly app: write(plotly_fig) : Displays a Plotly figure."

# st.write(distribution_day)

st.line_chart(data=df.resample('d'.lower()).count().sort_values('user', ascending=False).loc[:,'user'], width=0, height=0, use_container_width=True)

#st.write(value_counts_plot(df.month))

df

# st.write(
# value_counts_plot(df.month)
# )

# Nicer 

st.markdown("### 🎲 WhatsCeption")
st.markdown("This application is a Streamlit dashboard hosted on Heroku that can be used"
            "to explore the results from board game matches that I tracked over the last year.")
st.markdown("**♟ Statistics by Users ♟**")
st.write(
statistics_users(df))


## Plots and graphs

from charts import *
import seaborn as sns

st.markdown("**♟ Graphs for users! ♟**")

value_counts_plot_sns_hue(df, 'month', 'user')
st.pyplot()

value_counts_plot_sns_hue(df, 'day', 'user')
st.pyplot()


value_counts_plot_sns_hue(df, 'week', 'user')
st.pyplot()


# value_counts_plot_sns_hue(df, 'month', 'user')
# st.pyplot()
