# https://dashboard-salarios-dados.streamlit.app/
import pandas         as pd
import streamlit      as st
import plotly.express as px
# PAGE:
st.set_page_config(page_title='Data Area Salaries DashBoard', page_icon='📊', layout='wide')
df= pd.read_csv   ('https://github.com/kauefs/alura/raw/refs/heads/@/datasets/salaries.csv')
# SIDE:
st.sidebar.title  ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider( )
st.sidebar.header ('🔍 Filters')
# Level:
levels   =sorted(df['level'   ].unique( ))
level    =st.sidebar.multiselect('Level'       , levels   , default=   levels)
# Contract:
contracts=sorted(df['contract'].unique( ))
contract =st.sidebar.multiselect('Contract'    , contracts, default=contracts)
# Size:
sizes    =sorted(df['size'    ].unique( ))
size     =st.sidebar.multiselect('Company Size', sizes    , default=    sizes)
# Year:
years    =sorted(df['year'    ].unique( ))
year     =st.sidebar.multiselect('Year'        , years    , default=    years)
# DataFrame:
filter=df[(df['level'   ].isin(levels   )) &
          (df['contract'].isin(contracts)) &
          (df['size'    ].isin(sizes    )) &
          (df['year'    ].isin(years    )) ]
table=st.sidebar.empty( )
st.sidebar.divider    ( )
st.sidebar.markdown('''
![2025.08.08   ](https://img.shields.io/badge/2023.08.08-000000)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN:
st.title    ('🎲 Data Area Salaries DashBoard')
st.markdown ('Exploring Salaries for Data Area in the Last Few Years')
# --- Main Metrics (KPIs) ---
st.subheader('Main Metrics (Annual Salary in USD)')
if  not filter.empty:
    meanSalary=filter['USD'].mean( )
    maxSalary =filter['USD'].max ( )
    entries   =filter.shape[0]
    freq      =filter['job'].mode( )[0]
else: meanSalary, maxSalary, entries, freq = 0, 0, 0, ''
col1,col2=st.columns(2)
col1.metric(label='Total Entries'     ,  value=f'{    entries:,.0f}')
col2.metric(label='Most Frequent Job' ,  value=freq,  delta= None, delta_color='normal', help=None,
            label_visibility='visible', border=False) #, width='stretch', height='content')
col3,col4=st.columns(2)
col3.metric(label='Mean Salary'       ,  value=f'${meanSalary:,.0f}')
col4.metric(label= 'Max Salary'       ,  value=f'${ maxSalary:,.0f}')
st.divider ( )
# Plotly:
st.subheader('Charts')
graf1, graf2=st.columns(2)
with   graf1:
    if  not filter.empty:
        top=filter.groupby('job')['USD'].mean( ).nlargest(10).sort_values(ascending=True).reset_index( )
        topChart=px.bar(top, y= 'job', x='USD', orientation='h',
                        title = 'Top 10 Jobs per Mean Salary',
                        labels={'USD':'Annual Mean Salary (USD)','job':''})
        topChart.update_layout(title_x=.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(topChart, use_container_width=True)
    else:st.warning('No Data for Top Jobs Chart.')
with graf2:
    if  not filter.empty:
        hist=px.histogram(filter, x='USD', nbins=30,
                          title = 'Annual Salary Distribution',
                          labels={'USD': 'Salary Range (USD)','count':''})
        hist.update_layout(title_x=.1, yaxis_title='')
        st.plotly_chart(hist, use_container_width=True)
    else:st.warning('No Data for Distribution Chart.')
graf3, graf4 = st.columns(2)
with graf3:
    if    not  filter.empty:
        remote=filter['remote'].value_counts( ).reset_index( )
        remote.columns=['type','quantity']
        remote=px.pie(remote, names='type', values='quantity',
                      title='Job Types Proportion',
                      hole=.5)
        remote.update_traces(textinfo='label+percent')
        remote.update_layout(title_x=.1)
        st.plotly_chart(remote, use_container_width=True)
    else:st.warning('No Data for Job Types Chart.')
with graf4:
    if  not  filter.empty:
        ds  =filter[filter['job']=='Data Scientist']
        mean=ds.groupby('ISO3')['USD'].mean( ).reset_index( )
        countries=px.choropleth(mean, locations='ISO3', color='USD',
                                color_continuous_scale='rdylgn',
                                title  =   'Mean Data Scientist Salary per Country',
                                labels ={'USD':'Mean Salary (USD)','ISO3':'Country'},
                                hover_name=None, hover_data=None  ,
                                projection=None, scope='world')
        countries.update_layout(title_x=.1)
        st.plotly_chart(countries, use_container_width=True)
    else:st.warning('No Data for Countries Chart.')
st.divider( )
#  Table:
if table.checkbox('DataFrame', value=False):
    st.subheader ('Data')
    st.markdown  (f'''➡️  Showing {'**{:,.0f}** entries:'.format(filter.shape[0])}''')
    st.dataframe (filter)
    st.divider   (      )
