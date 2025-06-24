
# import streamlit as st
# import json
# import os

# # File is in the same directory
# json_file_path = os.path.join(os.path.dirname(__file__), "Fishing_Journal_MAY2025.json")

# # Load JSON from file
# if not os.path.exists(json_file_path):
#     st.error(f"JSON file not found at path: {json_file_path}")
#     st.stop()

# try:
#     with open(json_file_path, "r") as f:
#         data = json.load(f)
# except json.JSONDecodeError as e:
#     st.error(f"Error loading JSON: {e}")
#     st.stop()

# # Title
# st.title("🎣 Fishing Journal")

# # Get available years
# years = list(data["FishingJournal"].keys())
# selected_year = st.selectbox("Select Year", years, index=len(years) - 1)

# # Get available months for selected year
# months = list(data["FishingJournal"][selected_year].keys())
# selected_month = st.selectbox("Select Month", months, index=len(months) - 1)

# # Display entries
# st.header(f"Entries for {selected_month} {selected_year}")

# entries = data["FishingJournal"][selected_year][selected_month]

# if not entries:
#     st.info("No entries for this month.")
# else:
#     for entry in entries:
#         st.subheader(f"📅 {entry.get('Date', 'Unknown Date')}")

#         if "Note" in entry:
#             st.write(f"**Note:** {entry['Note']}")
#         if "Species" in entry:
#             st.write(f"**Species:** {entry['Species']}")
#         if "SpeciesCaught" in entry:
#             st.write(f"**Species Caught:** {', '.join(entry['SpeciesCaught'])}")
#         if "Weight" in entry:
#             st.write(f"**Weight:** {entry['Weight']}")

#         st.write(f"**Lure:** {entry['Lure']}")
#         st.write(f"**Rod:** {entry['Rod']}")
#         st.write(f"**Time:** {entry['Time']}")
#         st.write(f"**Location:** {entry['Location']}")
#         st.write(f"**Weather:** {entry['Weather']}")
#         st.markdown("---")
import streamlit as st
import json
import os
from collections import defaultdict

# File is in the same directory
json_file_path = os.path.join(os.path.dirname(__file__), "Fishing_Journal_MAY2025.json")

# Load JSON from file
if not os.path.exists(json_file_path):
    st.error(f"JSON file not found at path: {json_file_path}")
    st.stop()

try:
    with open(json_file_path, "r") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    st.error(f"Error loading JSON: {e}")
    st.stop()

# Title
st.title("🎣 Fishing Journal")

# Get available years
years = list(data["FishingJournal"].keys())

# Create a tab for each year
year_tabs = st.tabs(years)

for i, year in enumerate(years):
    with year_tabs[i]:
        st.header(f"📘 Entries for {year}")

        # Get available months for this year
        months = list(data["FishingJournal"][year].keys())
        selected_month = st.selectbox(f"Select Month for {year}", months, index=len(months) - 1, key=f"month_{year}")

        st.subheader(f"Entries for {selected_month} {year}")

        entries = data["FishingJournal"][year][selected_month]

        if not entries:
            st.info("No entries for this month.")
        else:
            # Group entries by date
            entries_by_date = defaultdict(list)
            for entry in entries:
                date = entry.get("Date", "Unknown Date")
                entries_by_date[date].append(entry)

            for date, date_entries in entries_by_date.items():
                # Extract weather from the first entry of the day
                weather_raw = date_entries[0].get("Weather", "Unknown")
                
                catch_label = "catch" if len(date_entries) == 1 else "catches"
                with st.expander(f"📅 {date} — {len(date_entries)} {catch_label}", expanded=False):
                    # Underlined Weather Subheader
                    st.markdown("<h3 style='text-decoration: underline;'>Weather</h3>", unsafe_allow_html=True)

                    # Parse and display weather fields
                    weather_parts = [w.strip() for w in weather_raw.split(";") if ":" in w]
                    for part in weather_parts:
                        label, value = part.split(":", 1)
                        st.write(f"**{label.strip()}:** {value.strip()}")

                    st.markdown("---")

                    for idx, entry in enumerate(date_entries, 1):
                        st.markdown(f"**🎣 Catch {idx}:**")

                        if "Note" in entry:
                            st.write(f"**Note:** {entry['Note']}")
                        if "Species" in entry:
                            st.write(f"**Species:** {entry['Species']}")
                        if "SpeciesCaught" in entry:
                            st.write(f"**Species Caught:** {', '.join(entry['SpeciesCaught'])}")
                        if "Weight" in entry:
                            st.write(f"**Weight:** {entry['Weight']}")

                        st.write(f"**Lure:** {entry['Lure']}")
                        st.write(f"**Rod:** {entry['Rod']}")
                        st.write(f"**Time:** {entry['Time']}")
                        st.write(f"**Location:** {entry['Location']}")
                        st.markdown("---")
