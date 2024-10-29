import pandas as pd
import streamlit as st

# Load the data
data = pd.read_csv("World Happiness Report Data - Sheet1.csv")

# Ensure the year column is formatted as an integer
data['year'] = data['year'].astype(int)

# Title of the app
st.title("🌍 Happiness Score Analysis")

# Sidebar for user input
st.sidebar.header("User Input")
country_name = st.sidebar.selectbox("Select a Country:", data['Country name'].unique())

# Filter data for the selected country
country_data = data[data['Country name'] == country_name]

# Display data with the year formatted correctly
country_data['year'] = country_data['year'].apply(lambda x: f"{x}")  # Format year as string without commas
st.write(f"### Happiness Score Data for {country_name}:")
st.dataframe(country_data)  # Display the DataFrame in the app

# Line chart for happiness score trend
st.write(f"### Happiness Score Trend in {country_name}")
st.line_chart(country_data.set_index('year')['Life Ladder'])

# Add a section for additional insights
def display_insights(country):
    if country == "Mongolia":
        st.write("### Insights for Mongolia:")
        st.markdown(
            """
            **Key Indicators of Happiness in Mongolia:**
            
            - **Life Ladder Score:** The Life Ladder scores show an upward trend over the years, with the score rising from 4.609 in 2007 to a peak of 6.011 in 2020, followed by a slight decline in subsequent years to 5.580 in 2023. The scores above 5 suggest a moderate level of happiness.
            
            - **Economic Indicators:** The Log GDP per capita has generally increased, indicating improved economic conditions and prosperity.
            
            - **Social Support:** Consistently high scores for social support (around 0.9) indicate strong support networks.
            
            - **Healthy Life Expectancy:** Improvements in health and longevity contribute positively to overall happiness.
            
            - **Freedom and Generosity:** Stable levels of freedom to make life choices and generosity.
            
            - **Emotional Well-Being:** A balance between positive and negative affect suggests challenges with negative emotions.

            **Conclusion:**
            
            - **Overall Assessment:** Mongolia's Life Ladder score indicates moderate happiness, with a significant upward trend until 2020.
            - **Strengths:** Strong social support and economic growth are positive indicators.
            - **Areas for Improvement:** Addressing causes for the decline in happiness scores and reducing negative affect could enhance well-being.
            """
        )
    else:
        st.write("### Additional Insights:")
        st.write(
            f"Explore the happiness trends for {country} and discover key factors contributing to happiness."
        )

display_insights(country_name)

# Download button for the data
csv = country_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name=f"{country_name}_happiness_data.csv",
    mime='text/csv'
)

# Additional Information Section
st.sidebar.header("Additional Information")
if country_name == "Mongolia":
    st.sidebar.write(
        """
        This app provides an analysis of happiness scores in Mongolia based on the World Happiness Report.
        Use the sidebar to select different countries for comparative analysis.
        """
    )
else:
    st.sidebar.write(
        """
        This app provides an analysis of happiness scores by country based on the World Happiness Report.
        Use the sidebar to select a country and explore its happiness data, trends, and insights.
        """
    )
