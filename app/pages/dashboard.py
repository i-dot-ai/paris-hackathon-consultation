import streamlit as st
import pandas as pd

from app.utils import IAI_PINK, LIGHT_PINK, DARK_BLUE


@st.cache_data
def themed_data():
    responses_df = pd.read_json("example_data/outputs/detailed_synthetic_data_mapped.json")
    return responses_df

st.title("Avez-vous des commentaires sur la construction d'une nouvelle centrale nucléaire à Normandie?")

# Get options for multiselect
all_data = themed_data()

# Display a summary
st.subheader("The top three themes from the responses are:")
themes_by_counts_df = all_data["themes"].value_counts().reset_index()


for row in themes_by_counts_df.head(3).iterrows():
    st.write(row[1]["themes"])

total_responses = len(all_data["response_id"].unique())
st.write(f"Total number of responses: {total_responses}")

# Explore the data in detail
st.subheader("Explore the data")
# Get options for multiselect
age_groups_options = all_data["age_group"].unique()
themes_options = all_data["themes"].unique()
city_options = all_data["city"].unique()
genders_options = all_data["gender"].unique()
positions_options = all_data["position"].unique()
stances_options = all_data["stances"].unique()

# Create multiselect
chosen_themes = st.multiselect("Select themes", options=themes_options, default=themes_options)
chosen_age_groups = st.multiselect("Select age groups", options=age_groups_options, default=age_groups_options)
chosen_genders = st.multiselect("Select gender", options=genders_options, default=genders_options)
chosen_cities = st.multiselect("Select location", options=city_options, default=city_options)
chosen_positions = st.multiselect("Select position", options=positions_options, default=positions_options)
chosen_stances = st.multiselect("Select stance", options=stances_options, default=stances_options)


# Filter the data
df = all_data
filtered_df = df[
    (df["themes"].isin(chosen_themes))
    & (df["age_group"].isin(chosen_age_groups))
    & (df["city"].isin(chosen_cities))
    & (df["age_group"].isin(chosen_age_groups))
    & (df["position"].isin(chosen_positions))
    & (df["stances"].isin(chosen_stances))
]

# Display the data
themes_by_counts = df["themes"].value_counts().sort_values(ascending=False)
st.bar_chart(themes_by_counts, horizontal=True, color=IAI_PINK)


st.dataframe(filtered_df)
