import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page layout and title
st.set_page_config(page_title="🎈 Handwashing Discovery")
st.title("Dr. Semmelweis and the Discovery of Handwashing")
st.write("""
    In 1847, Dr. Ignaz Semmelweis made a breakthrough discovery: he realized that making doctors wash their hands could drastically reduce the mortality rate of women giving birth.
    This dashboard visualizes the data that led to his conclusion.
""")

# Loading the data
@st.cache_data
def load_data():
    df = pd.read_csv('yearly_deaths_by_clinic-1.csv')
    
    # Calculating the proportion of deaths per number of births
    df['Proportion Deaths'] = df['Deaths'] / df['Birth']
    return df

df = load_data()

# Showing the raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Creating the visualization
st.subheader("Yearly Mortality Rates by Clinic")
st.write("Notice the massive difference in mortality rates between Clinic 1 and Clinic 2 before 1847 (when handwashing was introduced).")

# Plotly (Interactive Line Chart)
fig = px.line(
    df, 
    x="Year", 
    y="Proportion Deaths", 
    color="Clinic",
    markers=True,
    title="Proportion of Deaths over Time (1841-1849)",
    labels={"Proportion Deaths": "Mortality Rate", "Year": "Year"}
)

# Cleaning the chart up
fig.update_layout(yaxis_tickformat='.1%') # Format Y-axis as percentages

# Rendering the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Conclusion/Insights
st.info("""
**Key Insight:** Medical students worked at Clinic 1 and often went back and forth between the delivery room and the autopsy room without washing their hands. Midwives worked at Clinic 2, but they did not do autopsies. 
When Semmelweis made it necessary for people to wash their hands with chlorinated lime solutions in 1847, the death rate at Clinic 1 dropped to the same level as that at Clinic 2.
""")
