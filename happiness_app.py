import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
data = pd.read_csv('World Happiness Report Data - Sheet1.csv')

# Title of the app
st.title("🌍 Happiness Score Analysis")

# Sidebar for user input
st.sidebar.header("User Input")
country_name = st.sidebar.selectbox("Select a Country:", data['Country name'].unique())

# Filter data for the selected country
country_data = data[data['Country name'] == country_name]

# Display data
st.write(f"### Happiness Score Data for {country_name}:")
st.dataframe(country_data)  # Display the DataFrame in the app

# Summary statistics
st.write("### Summary Statistics:")
st.write(country_data[['year', 'Life Ladder']].describe())

# Plot settings
plt.figure(figsize=(10, 6))
plt.plot(country_data['year'], country_data['Life Ladder'], marker='o', linestyle='-', color='skyblue', label='Happiness Score')

# Annotate highest and lowest points with colors
max_value = country_data['Life Ladder'].max()
min_value = country_data['Life Ladder'].min()
max_year = country_data.loc[country_data['Life Ladder'] == max_value, 'year'].values[0]
min_year = country_data.loc[country_data['Life Ladder'] == min_value, 'year'].values[0]

# Annotating with distinct colors
plt.annotate(f'Max: {max_value}', xy=(max_year, max_value), xytext=(max_year, max_value + 0.5),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')
plt.annotate(f'Min: {min_value}', xy=(min_year, min_value), xytext=(min_year, min_value - 0.5),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='red')

# Plot enhancements
plt.xlabel('Year', fontsize=12)
plt.ylabel('Happiness Score (Life Ladder)', fontsize=12)
plt.title(f"Happiness Score Trend in {country_name}", fontsize=16)
plt.grid(True)
plt.legend()

# Show the plot in the Streamlit app
st.pyplot(plt)

# Additional insights for Mongolia
if country_name == "Mongolia":
    st.write("### Insights for Mongolia:")
    st.write("""
    **Key Indicators of Happiness in Mongolia**
    - **Life Ladder Score:** The Life Ladder scores show an upward trend over the years, rising from 4.609 in 2007 to a peak of 6.011 in 2020, followed by a slight decline to 5.580 in 2023.
    - **Economic Indicators:** The Log GDP per capita has generally increased, indicating improved economic conditions.
    - **Social Support:** High scores for social support (around 0.9) indicate strong support networks.
    - **Healthy Life Expectancy:** Improvements in health and longevity contribute positively.
    - **Freedom and Generosity:** Stable freedom to make life choices and levels of generosity.
    - **Emotional Well-Being:** There are positive feelings among the population, though challenges with negative emotions persist.

    **Conclusion:**
    - Overall, Mongolia shows moderate happiness levels, with strengths in social support and economic growth. Continued focus on reducing negative affect could enhance overall well-being.
    """)

# Download button for the data
csv = country_data.to_csv(index=False).encode('utf-8')
st.download_button(label="Download Data as CSV", data=csv, file_name=f"{country_name}_happiness_data.csv", mime='text/csv')
