import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df=pd.read_excel("/Users/iqraabbasi/Downloads/data.xlsx")
total=len(df)

#st.set_page_config(layout="wide")



#default responses incase there is no response in form
name=""
email=" "
Gender="F"
age="22"
kill=0
steal=0
talk=0

st.subheader("Welcome to the Understanding Diversity page!")

st.markdown("Here you’ll have a chance to compare your own personal opinion to those of people from different regions. We’ll do this for a few questions that we’ve asked university students and other people in previous research.  We will not be using your answers for research purposes, but we will collect the anonymous information so that we can record how many people visit our website and from what places. Please feel free to skip any question-- this is just for fun! /n How BAD is this behavior? Welcome to the Morality topic! What do you think of these *bad* behaviors? Please answer according to your own personal opinion. You will then get to see how similar your answers are to university students from other parts of the world.")

with st.form("form1", clear_on_submit=True):
    name=st.text_input("Enter full name")
    gender=st.selectbox('What is your gender?',('Male', 'Female', 'Prefer not to say'))
    location= st.selectbox('What is your location?',('Hong Kong', 'Vancouver', 'Melbourne', 'London', 'New York', 'Sydney'))
    age=st.slider("Enter your age", min_value=10, max_value=100)
    kill=st.slider("On a scale of 0=not bad at all to 5=extremely bad, how bad is it to kill someone?", min_value=1, max_value=5)
    steal=killing_someone=st.slider("On a scale of 1=not bad at all to 5=extremely bad, how bad is it to steal belongings?", min_value=1, max_value=5)
    loud=st.slider("On a scale of 1=not bad at all to 5=extremely bad, how bad is it to talk loudly in public?", min_value=1, max_value=5)

    submit=st.form_submit_button("Submit")

    if submit:
        filter_kill =  df['Kill_someone']==kill
        killing_df = df[filter_kill]
        kill_len=len(killing_df)
        #print("total: "+ str(total) + "kill:" + str(kill_len))
        percent_kill=round((kill_len/total) *100,1)
        display=("**" + str(percent_kill)+ "**" + "% of people agree with you on the severity of killing someone")
        st.markdown(display)
        #print(killing_df.head())

        filter_steal =  df['Steal']==steal
        steal_df = df[filter_steal]
        steal_len=len(steal_df)
        percent_steal=round((steal_len/total) *100,1)
        display=("**" + str(percent_steal) + "**"+ "% of people agree with you on the severity of stealing belongings")
        st.markdown(display)

        filter_talk =  df['Talk_loudly']==talk
        talk_df = df[filter_talk]
        talk_len=len(talk_df)
        percent_talk=round((talk_len/total) *100,1)
        display=("**" + str(percent_talk)+ "**" + "% of people agree with you on the severity of talking loudly in public")
        st.markdown(display)



        colors = ['#B6E880',  '#90AD1C', 'lightgreen']


        fig = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]],width=1200, height=400)
        fig.add_trace(go.Pie(labels=['People with your opinion on killing','Other responses'], values=[percent_kill, 100-percent_kill],marker=dict(colors=['#B6E880',  '#90AD1C'], line=dict(color='#000000', width=2)) ),1, 1)
        fig.add_trace(go.Pie(labels=['People with your opinion on stealing','Other responses'], values=[percent_steal, 100-percent_steal],marker=dict(colors=['#F8A19F',  '#E45756'], line=dict(color='#000000', width=2))),1, 2)
        fig.add_trace(go.Pie(labels=['People with your opinion on talking loudly','Other responses'], values=[percent_talk, 100-percent_talk],marker=dict(colors=['#19D3F3',  '#0099C6'], line=dict(color='#000000', width=2))),1, 3)
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict( line=dict(color='#000000', width=2)))
        #fig.show()
        st.plotly_chart(fig)



