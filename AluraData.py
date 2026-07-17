# https://dashboard-salarios-dados.streamlit.app/
import      numpy         as   np
import     pandas         as   pd
import  streamlit         as   st
import     plotly.express as   px
import matplotlib.pyplot  as   plt
import    seaborn         as   sns
from      seaborn       import palettes
# Settings
pd.options.plotting.matplotlib.register_converters = True
pd.options.display.max_columns         =             None
plt.rcParams[  'figure.autolayout']    =             True
plt.rcParams[    'font.family'    ]    =                                          'sans-serif'
sns.set_theme(context='notebook', style='whitegrid', palette='colorblind',  font ='sans-serif', font_scale=1.15, color_codes=True, rc={'grid.color':'1','grid.linestyle':':'})
FontT={'family':'sans-serif'    ,'color':'#000000' ,  'size': 13,    'fontweight':'semibold'  }
FontY={'family':'sans-serif'    ,'color':'#FF4500' ,  'size': 10,    'fontweight':'regular'   }
FontX={'family':'sans-serif'    ,'color':'#4CAF50' ,  'size': 10,    'fontweight':'regular'   }
# PAGE
st.set_page_config(page_title='Data Area Salaries DashBoard', page_icon='📊', layout='wide')
@st.cache_data
def LoadData( ):return pd.read_csv('https://github.com/kauefs/alura/raw/refs/heads/@/datasets/salaries.csv')
df =LoadData( )
# SIDE
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  ( )
st.sidebar.header   ('Exploring Salaries for Data Area')
st.sidebar.subheader('🔍 Filters')
# Level
levels   =sorted(df['level'   ].dropna( ).unique( ))
level    =st.sidebar.multiselect('Level'       , levels   , default=   levels)
# Contract
contracts=sorted(df['contract'].dropna( ).unique( ))
contract =st.sidebar.multiselect('Contract'    , contracts, default=contracts)
# Size
sizes    =sorted(df['size'    ].dropna( ).unique( ))
size     =st.sidebar.multiselect('Company Size', sizes    , default=    sizes)
# Year
years    =sorted(df['year'    ].dropna( ).unique( ))
year     =st.sidebar.multiselect('Year'        , years    , default=    years)
# DataFrame
filter=df[(df['level'   ].isin(level   )) &
          (df['contract'].isin(contract)) &
          (df['size'    ].isin(size    )) &
          (df['year'    ].isin(year    )) ]
table=st.sidebar.empty( )
st.sidebar.divider    ( )
st.sidebar.markdown('''
![2025.08.08   ](https://img.shields.io/badge/2025.08.08-000000)
![2026.02.02   ](https://img.shields.io/badge/2026.02.02-000000)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2026&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN
st.title    ('🎲 Data Area Salaries DashBoard')
st.divider  ( )
# --- Main Metrics (KPIs) ---
st.subheader('Main Metrics (Annual Salary in USD)')
if  not filter.empty:
    meanSalary=filter['USD'].mean( )
    maxSalary =filter['USD'].max ( )
    entries   =filter.shape[0]
    freq      =filter['job'].mode( )[0]
else: meanSalary, maxSalary, entries, freq = 0, 0, 0, 'N/A'
col1,col2=st.columns(2)
col1.metric(label='Total Entries'    , value=f'{    entries:,.0f}')
col2.metric(label='Most Frequent Job', value=freq,   delta= None, delta_color='normal', help=None, label_visibility='visible', border=False) #, width='stretch', height='content')
col3,col4=st.columns(2)
col3.metric(label='Mean Salary'      , value=f'${meanSalary:,.0f}')
col4.metric(label= 'Max Salary'      , value=f'${ maxSalary:,.0f}')
# Annual Growth Rate for Mean Salaries
if len(year)         > 1 and not filter.empty:
    growth           = filter.groupby('year')['USD'].mean( ).reset_index( )
    if len(growth)   > 1:
        firstYear    = growth.iloc[ 0]       ['USD']
        lastYear     = growth.iloc[-1]       ['USD']
        if firstYear > 0:
            totalGrowth=((lastYear-firstYear)/firstYear)*100
            col5,col6=st.columns(2)
            col6.metric(label='Total Salary Growth', value=f'{totalGrowth:.2f}%', delta=f'{totalGrowth:.2f}%')
st.divider ( )
# Plotly
st.subheader('Charts')
graf1 , graf2=st.columns(2)
with    graf1:
    if  not filter.empty:
        most =filter['job'].value_counts     ( )
        mosts=most.head(10) .reset_index( )
        mosts.columns=['job','frequency']
        fig=px.bar(mosts, y='job',x='frequency' , color = 'job', orientation='h', color_continuous_scale='rdylgn',
                   title='Most Frequent Professions', labels={'frequency':'','job':''})
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, width='stretch')
    else:st.warning('No Data for Most Frequent Professions Chart.')
with graf2:
    if  not filter.empty:
        top=filter.groupby('job')['USD'].mean( ).nlargest(10).sort_values(ascending=True).reset_index( )
        topChart=px.bar(top, y='job', x='USD', orientation='h', title='Top Jobs per Mean Salary', labels={'USD':'Annual Mean Salary (USD)','job':''},
                                  color='USD', color_continuous_scale=px.colors.sequential.Blues)
        topChart.update_layout(title_x=.1, yaxis={'categoryorder':'total ascending'}, xaxis_title='')
        st.plotly_chart(topChart, width='stretch')
    else:st.warning('No Data for Top Jobs Chart.')
graf3,graf4=st.columns(2)
with graf3:
    if    not  filter.empty:
        remote=filter['remote'].value_counts( ).reset_index( )
        remote.columns=['type' ,                   'quantity']
        chart =px.pie(remote, names='type', values='quantity', title='Job Types', hole =.5,) #color_discrete_sequence=px.colors.qualitative.Pastel)
        chart.update_traces(textinfo='label+percent')
       #remote.update_layout(title_x=.1)
        st.plotly_chart(chart, width='stretch')
    else:st.warning('No Data for Job Types Chart.')
with graf4:
    if  not filter.empty:
        hist=px.histogram (filter, x='USD', nbins=30, title= 'Annual Salary Distribution', labels={'USD':'Salary Range (USD)','count':''},
                           color_discrete_sequence=['#6596EE'])
        hist.update_layout(yaxis_title='')
        st.plotly_chart(hist, width='stretch')
    else:st.warning('No Data for Distribution Chart.')
graf5,graf6=st.columns(2)
with graf5:
    if  not filter.empty:
        colors=['#6595EE','#0065FF','#00FFFF','#00BFFF']
        lev=px.bar(data_frame=filter, x='level', color='level', color_discrete_sequence=colors)
        lev.update_layout(title_text='Level Distribution', yaxis_title=None, xaxis_title=None, showlegend=False)
        st.plotly_chart  (lev, width='stretch')
    else:st.warning      ('No Data for Level Distribution Chart.')
with graf6:
    if  not  filter.empty:
        mean=filter.groupby('level')['USD'].mean( ).reset_index( )
        colors=['#6595EE','#0065FF','#00FFFF','#00BFFF']
        pic =px.bar(mean, y='USD',x='level', title='Mean Salary per Level', labels={'level':'','USD':'Mean Salary (USD)'},
                              color='level', color_discrete_sequence=colors)
        pic.update_layout(xaxis={'categoryorder':'total descending'}, showlegend=False)
        st .plotly_chart ( pic , width='stretch')
    else:st.warning('No Data for Mean Salary per Level Chart.')
graf7,graf8=st.columns(2)
with graf7:
    if  not  filter.empty:
        medcount=filter.groupby('ISO3')['USD'].mean( ).reset_index( )
        select=medcount.sort_values (by='USD', ascending=False).head(10)
        med=px.bar(data_frame=select, y='USD', x='ISO3', color='ISO3')
        med.update_layout(title_text='Countries with Highest Salaries', yaxis_title=None, xaxis_title=None, showlegend=False)
        st.plotly_chart  (med, width='stretch')
    else:st.warning      ('No Data for Countries with Highest Chart.')
with graf8:
    if  not  filter.empty:
        # ev = filter.groupby('year') ['USD'].mean( ).reset_index( )
        # fig=px.line(ev, x = 'year',y='USD',
        # title='Mean Annual Salary Evolution',
        # markers=True, color_discrete_sequence=['#20B2AA'])
        # fig.update_layout(xaxis=dict(tickmode='linear', dtick=1), showlegend=False)
        jr  =filter[filter['level']=='entry']['job'].value_counts( ).nlargest(5).index.tolist( )
        if jr:
            only=filter[filter['job'].isin(jr)]
            grup=only.groupby(['job','year'])['USD'].mean( ).reset_index( )
            img =px.line(grup,     x='year',y='USD',
                        title  = 'Entry Level Mean Annual Salary Evolution',
                        labels ={'year':'year','USD':'Mean Salary (USD)','job':'job'},
                        color  = 'job', markers=True)
            img.update_layout(xaxis=dict(tickmode='linear', dtick=1), showlegend=True)
            st .plotly_chart ( img ,        width='stretch')
        else:st.info          ('No entry level position entries found')
    else    :st.warning       ('No Data for Entry Level Mean Annual Salary Evolution Chart.')
st.divider( )
left,center,right=st.columns(spec=[.15,10,.15])
with center:
    if  not  filter.empty:
        ds  =filter[filter['job']=='Data Scientist']
        if not ds.empty:
            mean=ds.groupby('ISO3')['USD'].mean( ).reset_index( )
            countries=px.choropleth(mean, locations='ISO3', color='USD', color_continuous_scale='rdylgn',
                                    title =    'Mean Data Scientist Salary per Country',
                                    labels= {'USD':'Mean Salary (USD)','ISO3':'Country'},
                                    hover_name=None, hover_data=None, projection=None, scope='world')
           #countries.update_layout(title_x=.1)
            st.plotly_chart(countries, width='stretch')
        else:st.info   ('No specific "Data Scientist" records match the chosen filter configuration to map globally.')
    else    :st.warning('No Data for Countries Chart.')
st.divider( )
#  Table
if table.checkbox('DataFrame', value=False):
    st.subheader ('Data')
    st.markdown  (f'''➡️  Showing **{filter.shape[0]:,.0f}** entries:''')
    st.dataframe (filter, width='stretch')
    st.divider   (      )
st.toast('Ready!', icon='📊')
