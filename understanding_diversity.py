import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
st.set_page_config(layout="wide")
df=pd.read_excel("/Users/iqraabbasi/Desktop/data.xlsx")
total=len(df)
index_ = ['Not at all', 'A little bad', 'Somewhat bad', 'Very bad', 'Extremely bad']
#You can check .empty documentation
# Create a page dropdown 


# Define color sets of paintings
reds = ['#F9A7A7', '#FA7A7A','#ECC2C2','#FF5050','#DF8080']
blues = ['#7CBEFF', '#619DDA', '#B5D7F9',
                     '#49A4FF', '#B5ECFF']
greens = ['#9EE182', '#92CB7A', '#ACF28E',
                 '#76AE5E', '#C8EEB7']

specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]]

def show_plots():
    filter_HK =  df['Location']=="Hong Kong"
    HK_df = df[filter_HK]
    HK_len=len(HK_df)
    HK_df_kill=HK_df['Kill_someone'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in HK_df_kill.index:
            HK_df_kill[float(i)] = 0
    HK_df_kill.sort_index()
    HK_df_kill.index = index_
    name_HK_kill=HK_df_kill.index.values.tolist() 
    values_HK_kill = HK_df_kill.tolist()


    filter_Mb =  df['Location']=="Melbourne"
    Mb_df = df[filter_Mb]
    Mb_len=len(Mb_df)
    Mb_df_kill=Mb_df['Kill_someone'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Mb_df_kill.index:
            Mb_df_kill[float(i)] = 0
    Mb_df_kill.sort_index()
    Mb_df_kill.index = index_
    name_Mb_kill=Mb_df_kill.index.values.tolist() 
    values_Mb_kill = Mb_df_kill.tolist()

    filter_Ld =  df['Location']=="London"
    Ld_df = df[filter_Ld]
    Ld_len=len(Ld_df)
    Ld_df_kill=Ld_df['Kill_someone'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Ld_df_kill.index:
            Ld_df_kill[float(i)] = 0
    Ld_df_kill.sort_index()
    Ld_df_kill.index = index_
    name_Ld_kill=Ld_df_kill.index.values.tolist() 
    values_Ld_kill = Ld_df_kill.tolist()

    # Define pie charts
    fig = make_subplots(rows=1, cols=3, specs=specs)
    fig.add_trace(go.Pie(labels=name_HK_kill, values=values_HK_kill, name='Starry Night',title='Opinion on killing someone: Hong Kong',
                        marker_colors=blues), 1, 1)
    fig.add_trace(go.Pie(labels=name_Mb_kill, values=values_Mb_kill, name='Sunflowers',title='Opinion on killing someone: Melbourne',
                        marker_colors=reds), 1, 2)
    fig.add_trace(go.Pie(labels=name_Ld_kill, values=values_Ld_kill, name='Irises',title='Opinion on killing someone: London',
                        marker_colors=greens), 1, 3)

    # Tune layout and hover info
    fig.update_traces(hoverinfo='label+percent', textinfo='none')
    fig.update(layout_title_text='Opinions on killing someone by location',
            layout_showlegend=False)

    fig = go.Figure(fig)
    st.plotly_chart(fig, use_container_width=True)
    ###########################################################################################################

    filter_HK_talk =  df['Location']=="Hong Kong"
    HK_df = df[filter_HK_talk]
    HK_len=len(HK_df)
    HK_df_talk=HK_df['Talk_loudly'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in HK_df_talk.index:
            HK_df_talk[float(i)] = 0
    HK_df_talk.sort_index()


    HK_df_talk.index = index_
    name_HK_talk=HK_df_talk.index.values.tolist() 
    values_HK_talk = HK_df_talk.tolist()


    filter_Mb =  df['Location']=="Melbourne"
    Mb_df = df[filter_Mb]
    Mb_len=len(Mb_df)
    Mb_df_talk=Mb_df['Talk_loudly'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Mb_df_talk.index:
            Mb_df_talk[float(i)] = 0
    Mb_df_talk.sort_index()
    Mb_df_talk.index = index_
    name_Mb_talk=Mb_df_talk.index.values.tolist() 
    values_Mb_talk = Mb_df_talk.tolist()

    filter_Ld =  df['Location']=="London"
    Ld_df = df[filter_Ld]
    Ld_len=len(Ld_df)
    Ld_df_talk=Ld_df['Talk_loudly'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Ld_df_talk.index:
            Ld_df_talk[float(i)] = 0
    Ld_df_talk.sort_index()
    Ld_df_talk.index = index_
    name_Ld_talk=Ld_df_talk.index.values.tolist() 
    values_Ld_talk = Ld_df_talk.tolist()


    # Define pie charts
    fig3 = make_subplots(rows=1, cols=3, specs=specs)
    fig3.add_trace(go.Pie(labels=name_HK_talk, values=values_HK_talk, name='Starry Night',title='Opinion on talk loudly: Hong Kong',
                        marker_colors=blues), 1, 1)
    fig3.add_trace(go.Pie(labels=name_Mb_talk, values=values_Mb_talk, name='Sunflowers',title='Opinion on talking loudly: Melbourne',
                        marker_colors=reds), 1, 2)
    fig3.add_trace(go.Pie(labels=name_Ld_talk, values=values_Ld_talk, name='Irises',title='Opinion on talking loudly: London',
                        marker_colors=greens), 1, 3)

    # Tune layout and hover info
    fig3.update_traces(hoverinfo='label+percent', textinfo='none')
    fig3.update(layout_title_text='Opinions on Talking loudly in Public',
            layout_showlegend=False)

    fig3 = go.Figure(fig3)
    st.plotly_chart(fig3, use_container_width=True)
  

    ###########################################################################################################


    filter_HK_steal =  df['Location']=="Hong Kong"
    HK_df = df[filter_HK_steal]
    HK_len=len(HK_df)
    HK_df_steal=HK_df['Steal'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in HK_df_steal.index:
            HK_df_steal[float(i)] = 0
    HK_df_steal.sort_index()
   

    HK_df_steal.index = index_
    name_HK_steal=HK_df_steal.index.values.tolist() 
    values_HK_steal = HK_df_steal.tolist()


    filter_Mb =  df['Location']=="Melbourne"
    Mb_df = df[filter_Mb]
    Mb_len=len(Mb_df)
    Mb_df_steal=Mb_df['Steal'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Mb_df_steal.index:
            Mb_df_steal[float(i)] = 0
    Mb_df_steal.sort_index()
    Mb_df_steal.index = index_
    name_Mb_steal=Mb_df_steal.index.values.tolist() 
    values_Mb_steal = Mb_df_steal.tolist()

    filter_Ld =  df['Location']=="London"
    Ld_df = df[filter_Ld]
    Ld_len=len(Ld_df)
    Ld_df_steal=Ld_df['Steal'].value_counts()
    options=[1.0,2.0,3.0,4.0,5.0]
    for i in options:
        if i not in Ld_df_steal.index:
            Ld_df_steal[float(i)] = 0
    Ld_df_steal.sort_index()
    Ld_df_steal.index = index_
    name_Ld_steal=Ld_df_steal.index.values.tolist() 
    values_Ld_steal = Ld_df_steal.tolist()

    # Define pie charts
    fig2 = make_subplots(rows=1, cols=3, specs=specs)
    fig2.add_trace(go.Pie(labels=name_HK_steal, values=values_HK_steal, name='Starry Night',title='Opinion on stealing: Hong Kong',
                        marker_colors=blues), 1, 1)
    fig2.add_trace(go.Pie(labels=name_Mb_steal, values=values_Mb_steal, name='Sunflowers',title='Opinion on stealing: Melbourne',
                        marker_colors=reds), 1, 2)
    fig2.add_trace(go.Pie(labels=name_Ld_steal, values=values_Ld_steal, name='Irises',title='Opinion on stealing: London',
                        marker_colors=greens), 1, 3)

    # Tune layout and hover info
    fig2.update_traces(hoverinfo='label+percent', textinfo='none')
    fig2.update(layout_title_text='Opinions on Stealing by location',
            layout_showlegend=False)

    fig2 = go.Figure(fig2)
   
    st.plotly_chart(fig2, use_container_width=True)

    talk_loudly_violin=df[["Location", "Talk_loudly"]]
    #talk_loudly_violin["Talk_loudly"]=talk_loudly_violin["Talk_loudly"].astype(str)
    talk_loudly_violin=talk_loudly_violin.rename(columns={'Talk_loudly': 'Opinions on talking loudly in public'})
    fig4 = px.violin(talk_loudly_violin,  y="Opinions on talking loudly in public", x="Location", box=True, color="Location", # draw box plot inside the violin
                    points='all', # can be 'outliers', or False
                )

    st.plotly_chart(fig4, use_container_width=True)

    talk_loudly_violin=df[["Location", "Age"]]
    #talk_loudly_violin["Talk_loudly"]=talk_loudly_violin["Talk_loudly"].astype(str)
    talk_loudly_violin=talk_loudly_violin.rename(columns={'Age': 'Age of respondent by country'})
    # draw box plot inside the violin
    fig5 = px.violin(talk_loudly_violin,  y="Age of respondent by country", x="Location", box=True, color="Location",
                    points='all', # can be 'outliers', or False
                )

    st.plotly_chart(fig5, use_container_width=True)



#######################################################################################################


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
    location= st.selectbox('What is your location?',('Hong Kong', 'Vancouver', 'Karachi','Lahore','Paris', 'United States','Melbourne', 'London', 'New York', 'Sydney'))
    age=st.slider("Enter your age", min_value=10, max_value=100)
    kill=st.slider("On a scale of 1 = not bad at all to 5 = extremely bad, how bad is it to kill someone?", min_value=1, max_value=5)
    steal=killing_someone=st.slider("On a scale of 1=not bad at all to 5 = extremely bad, how bad is it to steal belongings?", min_value=1, max_value=5)
    talk=st.slider("On a scale of 1 = not bad at all to 5 = extremely bad, how bad is it to talk loudly in public?", min_value=1, max_value=5)
    
    submit=st.form_submit_button("Submit")


    if submit:
        show_plots()

    
