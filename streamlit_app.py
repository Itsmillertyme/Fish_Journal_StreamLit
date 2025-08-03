# # import streamlit as st
# # import json
# # import os
# # import pandas as pd
# # import random
# # import altair as alt
# # import plotly.express as px
# # from calendar import monthrange
# # from datetime import datetime
# # from collections import defaultdict

# # # File is in the same directory
# # json_file_path = os.path.join(os.path.dirname(__file__), "Fishing_Journal_MAY2025.json")

# # # Load JSON from file
# # if not os.path.exists(json_file_path):
# #     st.error(f"JSON file not found at path: {json_file_path}")
# #     st.stop()

# # try:
# #     with open(json_file_path, "r") as f:
# #         data = json.load(f)
# # except json.JSONDecodeError as e:
# #     st.error(f"Error loading JSON: {e}")
# #     st.stop()

# # # Title
# # st.title("🎣 Fishing Journal")

# # # # Get available years
# # # years = list(data["FishingJournal"].keys())

# # years = sorted(data["FishingJournal"].keys())  # Ascending
# # years.reverse()  # Now most recent year is first

# # # Create a tab for each year
# # year_tabs = st.tabs(years)

# # for i, year in enumerate(years):
# #     with year_tabs[i]:
# #         st.header(f"📘 Entries for {year}")

# #         # Get available months for this year
# #         months = list(data["FishingJournal"][year].keys())
# #         selected_month = st.selectbox(f"Select Month", months, index=len(months) - 1, key=f"month_{year}")

# #         entries = data["FishingJournal"][year][selected_month]     

# #         if not entries:
# #             st.info("No entries for this month.")
# #         else:
# #             #MONTHLY DATA 
# #             month_number = months.index(selected_month)+1            
# #             days_in_month = monthrange(int(year), month_number)[1]
# #             number_days_successful = 0
# #             catch_data = [0] * days_in_month

# #             for entry in entries:
# #                 date_obj = datetime.strptime(entry["Date"][0:10], "%m/%d/%Y")
# #                 day = date_obj.day

# #                 if 1<= day <= days_in_month:
# #                     catch_data[day-1] += 1    

# #             for day in catch_data:
# #                 if day != 0:
# #                     number_days_successful += 1

            
# #             if number_days_successful/days_in_month < 0.2:
# #                 percentage_color = "color:red"
# #             elif number_days_successful/days_in_month < 0.5:
# #                 percentage_color = "color:yellow"
# #             else:
# #                 percentage_color = "color:green"

# #             st.subheader(f"{selected_month} {year} - Visualization")
# #             st.markdown("**Statistics**")
# #             st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Fish Caught: {len(entries)}", unsafe_allow_html=True)
# #             st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Days with a Catch: {number_days_successful}/{days_in_month} - <span style={percentage_color}>{round(number_days_successful/days_in_month *100, 2)}%</span>", unsafe_allow_html=True)
# #             st.write("")                    
# #             st.write("")                    
# #             st.write("")                    

# #             catches_per_day = []
# #             current_entry_index = 0

# #             # for i in range(1,days_in_month+1):
# #             #     if int(entries[current_entry_index]["Date"].split("/")[1]) > current_entry_index
# #             #     st.write(entries[current_entry_index]["Date"])
            





# #             days = list(range(1, days_in_month + 1))
# #             values = catch_data

# #             # Create DataFrame
# #             df = pd.DataFrame({
# #                 'Day': days,
# #                 'Value': values
# #             })        

# #             # Calculate tick values
# #             max_y = max(values) if values else 0
# #             tick_vals = list(range(0, max_y + 2)) if max_y > 0 else [0, 1]

# #             chart = alt.Chart(df).mark_bar().encode(
# #                 x=alt.X('Day:O', title='Day', axis=alt.Axis(labelAngle=0)),
# #                 y=alt.Y('Value:Q', title=" ", axis=alt.Axis(values=tick_vals,format='d'))
# #             ).properties(
# #                 width=700,
# #                 height=400,
# #                 title=f"Fish caught per day"
# #             )

# #             # Display the chart
# #             st.altair_chart(chart, use_container_width=False)

# #             lure_list = []
# #             lure_amount_list = []

# #             for entry in entries:
# #                 if entry["Lure"] in lure_list:
# #                     lure_amount_list[lure_list.index(entry["Lure"])] +=1
# #                 else:
# #                     lure_list.append(entry["Lure"])
# #                     lure_amount_list.append(1)

# #             df = pd.DataFrame({
# #                 'Lures': lure_list,
# #                 'Amount': lure_amount_list
# #             })

# #             custom_colors = [
# #                 '#636EFA',  # Blue (Streamlit default)
# #                 '#EF553B',  # Red
# #                 '#00CC96',  # Green
# #                 '#AB63FA',  # Purple
# #                 '#FFA15A',  # Orange
# #                 '#19D3F3',  # Light Blue
# #                 '#FF6692',  # Pink
# #                 '#B6E880',  # Light Green
# #                 '#FF97FF',  # Light Pink
# #                 '#FECB52'   # Yellow
# #             ]

# #             fig = px.pie(df, values='Amount', names='Lures', title='Lure Variety',color_discrete_sequence=custom_colors)

# #             st.plotly_chart(fig)

# #             st.markdown("---")

# #             st.subheader(f"{selected_month} {year} - Catch Data")            

# #             # Group entries by date
# #             entries_by_date = defaultdict(list)
# #             for entry in entries:
# #                 date = entry.get("Date", "Unknown Date")
# #                 entries_by_date[date].append(entry)

# #             for date, date_entries in entries_by_date.items():
# #                 # Extract weather from the first entry of the day
# #                 weather_raw = date_entries[0].get("Weather", "Unknown")
# #                 weather_parts = [w.strip() for w in weather_raw.split(";") if w.strip()]

# #                 # First part = forecast
# #                 forecast = weather_parts[0] if weather_parts else "Unknown"
# #                 details = weather_parts[1:] if len(weather_parts) > 1 else []

# #                 catch_label = "catch" if len(date_entries) == 1 else "catches"
# #                 with st.expander(f"📅 {date} — {len(date_entries)} {catch_label}", expanded=False):
# #                     # Underlined subheader with forecast inline
# #                     st.markdown(f"<h3 style='text-decoration: underline;'>Weather: {forecast}</h3>", unsafe_allow_html=True)

# #                     # Display remaining weather fields
# #                     for part in details:
# #                         if ":" in part:
# #                             label, value = part.split(":", 1)
# #                             st.write(f"**{label.strip()}:** {value.strip()}")

# #                     st.markdown("---")

# #                     for idx, entry in enumerate(date_entries, 1):
# #                         st.markdown(f"**🎣 Catch {idx}:**")

# #                         if "Note" in entry:
# #                             st.write(f"**Note:** {entry['Note']}")
                        
# #                         if "Species" in entry:
# #                             st.write(f"**Species:** {entry['Species']}")
# #                         if "SpeciesCaught" in entry:
# #                             st.write(f"**Species Caught:** {', '.join(entry['SpeciesCaught'])}")
# #                         if "Weight" in entry:
# #                             st.write(f"**Weight:** {entry['Weight']}")

# #                         st.write(f"**Lure:** {entry['Lure']}")
# #                         st.write(f"**Rod:** {entry['Rod']}")
# #                         st.write(f"**Time:** {entry['Time']}")
# #                         st.write(f"**Location:** {entry['Location']}")

# #                         if "Notes" in entry: 
# #                             st.write(f"**Catch Notes:** {entry['Notes']}")

# #                         st.markdown("---")

            
                        
# import streamlit as st
# import json
# import os
# import re
# import pandas as pd
# import random
# import altair as alt
# import plotly.express as px
# from calendar import monthrange
# from datetime import datetime
# from collections import defaultdict, Counter

# # --- Load JSON Data ---
# json_file_path = os.path.join(os.path.dirname(__file__), "Fishing_Journal_MAY2025.json")

# if not os.path.exists(json_file_path):
#     st.error(f"JSON file not found at path: {json_file_path}")
#     st.stop()

# try:
#     with open(json_file_path, "r") as f:
#         data = json.load(f)
# except json.JSONDecodeError as e:
#     st.error(f"Error loading JSON: {e}")
#     st.stop()

# # --- Page Title ---
# st.title("🎣 Fishing Journal")

# # --- Prepare Year Tabs (most recent first) ---
# years = sorted(data["FishingJournal"].keys(), reverse=True)
# year_tabs = st.tabs(years)

# for i, year in enumerate(years):
#     with year_tabs[i]:
#         st.header(f"📘 Entries for {year}")

#         # --- Select Month ---
#         months = list(data["FishingJournal"][year].keys())
#         selected_month = st.selectbox(
#             "Select Month",
#             months,
#             index=len(months) - 1,
#             key=f"month_{year}"
#         )

#         entries = data["FishingJournal"][year][selected_month]

#         if not entries:
#             st.info("No entries for this month.")
#             continue  # Skip to next year tab if no entries

#         # --- Monthly Data Preparation ---
#         month_number = months.index(selected_month) + 1
#         days_in_month = monthrange(int(year), month_number)[1]
        
#         # Initialize list to count catches per day
#         catch_data = [0] * days_in_month
#         number_days_successful = 0

#         # --- Calculate Most Productive Time of Day ---
#         hour_counts = Counter()

#         for entry in entries:
#             time_str = entry.get("Time", "").strip()
#             if time_str:
#                 # Extract hour and minute using regex (handles "7:45pm", "11:00am", etc.)
#                 match = re.match(r'(\d{1,2}):(\d{2})\s*(AM|PM)', time_str, re.IGNORECASE)
#                 if match:
#                     hour = int(match.group(1))
#                     minute = int(match.group(2))
#                     meridiem = match.group(3)
#                     # Convert to 24-hour time
#                     if meridiem == 'pm' and hour != 12:
#                         hour += 12
#                     if meridiem == 'am' and hour == 12:
#                         hour = 0
#                     # Use hour as key for counting catches within that hour (e.g., 13 for 1pm)
#                     hour_counts[hour] += 1

#         if hour_counts:
#             # Find hour with max catches
#             most_common_hour, max_count = hour_counts.most_common(1)[0]

#             # Format time range string like "11:00am - 12:00pm"
#             def format_hour(h):
#                 suffix = "am" if h < 12 else "pm"
#                 hour_12 = h if 1 <= h <= 12 else (h - 12 if h > 12 else 12)
#                 return f"{hour_12}:00{suffix}"

#             productive_time_range = f"{format_hour(most_common_hour)} - {format_hour((most_common_hour + 1) % 24)}"
#         else:
#             productive_time_range = "No time data"
        

#         # Count catches for each day
#         for entry in entries:
#             # Parse date string (assumes format mm/dd/yyyy)
#             date_obj = datetime.strptime(entry["Date"][0:10], "%m/%d/%Y")
#             day = date_obj.day
#             if 1 <= day <= days_in_month:
#                 catch_data[day - 1] += 1

#         # Count how many days had at least one catch
#         for catches in catch_data:
#             if catches != 0:
#                 number_days_successful += 1

#         # --- Color coding for percentage of successful days ---
#         success_ratio = number_days_successful / days_in_month
#         if success_ratio < 0.2:
#             percentage_color = "color:red"
#         elif success_ratio < 0.5:
#             percentage_color = "color:yellow"
#         else:
#             percentage_color = "color:green"

#         # --- Display Monthly Statistics ---
#         st.subheader(f"{selected_month} {year} - Visualization")
#         st.markdown("**Statistics**")
#         st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Fish Caught: {len(entries)}", unsafe_allow_html=True)
#         st.markdown(
#             f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Days with a Catch: "
#             f"{number_days_successful}/{days_in_month} &nbsp;- &nbsp;"
#             f"<span style={percentage_color}>"
#             f"{round(success_ratio * 100, 2)}%</span>",
#             unsafe_allow_html=True
#         )
#         st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Most Productive Time: **{productive_time_range}**", unsafe_allow_html=True)

#         # Add some vertical spacing
#         st.write("")
#         st.write("")
#         st.write("")

#         # --- Prepare DataFrame for Daily Catch Chart ---
#         days = list(range(1, days_in_month + 1))
#         values = catch_data

#         df = pd.DataFrame({
#             'Day': days,
#             'Value': values
#         })

#         # Calculate tick values for Y axis (whole numbers)
#         max_y = max(values) if values else 0
#         tick_vals = list(range(0, max_y + 2)) if max_y > 0 else [0, 1]

#         # --- Altair Bar Chart for Fish Caught per Day ---
#         chart = alt.Chart(df).mark_bar().encode(
#             x=alt.X('Day:O', title='Day', axis=alt.Axis(labelAngle=0)),
#             y=alt.Y('Value:Q', title=" ", axis=alt.Axis(values=tick_vals, format='d'))
#         ).properties(
#             width=700,
#             height=400,
#             title="Fish caught per day"
#         )
#         st.altair_chart(chart, use_container_width=False)

#         # --- Prepare Data for Lure Variety Pie Chart ---
#         lure_list = []
#         lure_amount_list = []

#         for entry in entries:
#             lure = entry.get("Lure", "Unknown")
#             if lure in lure_list:
#                 lure_amount_list[lure_list.index(lure)] += 1
#             else:
#                 lure_list.append(lure)
#                 lure_amount_list.append(1)

#         df_lures = pd.DataFrame({
#             'Lures': lure_list,
#             'Amount': lure_amount_list
#         })

#         custom_colors = [
#             '#636EFA',  # Blue (Streamlit default)
#             '#EF553B',  # Red
#             '#00CC96',  # Green
#             '#AB63FA',  # Purple
#             '#FFA15A',  # Orange
#             '#19D3F3',  # Light Blue
#             '#FF6692',  # Pink
#             '#B6E880',  # Light Green
#             '#FF97FF',  # Light Pink
#             '#FECB52'   # Yellow
#         ]

#         # --- Plotly Pie Chart for Lure Variety ---
#         fig = px.pie(
#             df_lures,
#             values='Amount',
#             names='Lures',
#             title='Lure Variety',
#             color_discrete_sequence=custom_colors
#         )
#         st.plotly_chart(fig)

#         st.markdown("---")

#         # --- Detailed Catch Data by Date ---
#         st.subheader(f"{selected_month} {year} - Catch Data")

#         # Group entries by date for display
#         entries_by_date = defaultdict(list)
#         for entry in entries:
#             date = entry.get("Date", "Unknown Date")
#             entries_by_date[date].append(entry)

#         for date, date_entries in entries_by_date.items():
#             # Extract weather info from first entry of the day
#             weather_raw = date_entries[0].get("Weather", "Unknown")
#             weather_parts = [w.strip() for w in weather_raw.split(";") if w.strip()]

#             forecast = weather_parts[0] if weather_parts else "Unknown"
#             details = weather_parts[1:] if len(weather_parts) > 1 else []

#             catch_label = "catch" if len(date_entries) == 1 else "catches"

#             with st.expander(f"📅 {date} — {len(date_entries)} {catch_label}", expanded=False):
#                 # Weather forecast (underlined)
#                 st.markdown(f"<h3 style='text-decoration: underline;'>Weather: {forecast}</h3>", unsafe_allow_html=True)

#                 # Additional weather details
#                 for part in details:
#                     if ":" in part:
#                         label, value = part.split(":", 1)
#                         st.write(f"**{label.strip()}:** {value.strip()}")

#                 st.markdown("---")

#                 # Display each catch entry for the day
#                 for idx, entry in enumerate(date_entries, 1):
#                     st.markdown(f"**🎣 Catch {idx}:**")

#                     if "Note" in entry:
#                         st.write(f"**Note:** {entry['Note']}")
#                     if "Species" in entry:
#                         st.write(f"**Species:** {entry['Species']}")
#                     if "SpeciesCaught" in entry:
#                         st.write(f"**Species Caught:** {', '.join(entry['SpeciesCaught'])}")
#                     if "Weight" in entry:
#                         st.write(f"**Weight:** {entry['Weight']}")

#                     st.write(f"**Lure:** {entry.get('Lure', 'Unknown')}")
#                     st.write(f"**Rod:** {entry.get('Rod', 'Unknown')}")
#                     st.write(f"**Time:** {entry.get('Time', 'Unknown')}")
#                     st.write(f"**Location:** {entry.get('Location', 'Unknown')}")

#                     if "Notes" in entry:
#                         st.write(f"**Catch Notes:** {entry['Notes']}")

#                     st.markdown("---")
import streamlit as st
import json
import os
import pandas as pd
import altair as alt
import plotly.express as px
from calendar import monthrange
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import defaultdict, Counter
import re

# --- Load JSON Data ---
json_file_path = os.path.join(os.path.dirname(__file__), "Fishing_Journal_MAY2025.json")

if not os.path.exists(json_file_path):
    st.error(f"JSON file not found at path: {json_file_path}")
    st.stop()

try:
    with open(json_file_path, "r") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    st.error(f"Error loading JSON: {e}")
    st.stop()

# --- Page Title ---
st.title("🎣 Fishing Journal")

# --- Prepare Year Tabs (most recent first) ---
years = sorted(data["FishingJournal"].keys(), reverse=True)
year_tabs = st.tabs(years)
most_recent_year = -1

for i, year in enumerate(years):
    with year_tabs[i]:
        if int(year) > int(most_recent_year):
            most_recent_year = year

        st.header(f"📘 Entries for {year}")

        # --- Select Month ---
        months = list(data["FishingJournal"][year].keys())
        selected_month = st.selectbox(
            "Select Month",
            months,
            index=len(months) - 1,
            key=f"month_{year}"
        )

        entries = data["FishingJournal"][year][selected_month]

        if not entries:
            st.info("No entries for this month.")
            continue  # Skip to next year tab if no entries

        # --- Monthly Data Preparation ---
        month_number = months.index(selected_month) + 1
        days_in_month = monthrange(int(year), month_number)[1]
        now = datetime.now(ZoneInfo("America/New_York"))
        current_month = now.month
        current_year = now.year
 
        if current_month == month_number and current_year == int(most_recent_year):
            days_stat_calc = now.day
        else:
            days_stat_calc = days_in_month
        
        # Initialize list to count catches per day
        catch_data = [0] * days_in_month 
        number_days_successful = 0

        # Count catches for each day
        for entry in entries:
            # Parse date string (assumes format mm/dd/yyyy)
            date_obj = datetime.strptime(entry["Date"][0:10], "%m/%d/%Y")
            day = date_obj.day
            if 1 <= day <= days_in_month:
                catch_data[day - 1] += 1

        # Count how many days had at least one catch
        for catches in catch_data:
            if catches != 0:
                number_days_successful += 1

        # --- Calculate Most Productive Time of Day ---
        hour_counts = Counter()

        for entry in entries:
            time_str = entry.get("Time", "").strip()
            if time_str:
                match = re.match(r'(\d{1,2}):(\d{2})\s*(AM|PM)', time_str, re.IGNORECASE)
                if match:
                    hour = int(match.group(1))
                    meridiem = match.group(3).lower()
                    # Convert to 24-hour format
                    if meridiem == 'pm' and hour != 12:
                        hour += 12
                    if meridiem == 'am' and hour == 12:
                        hour = 0
                    hour_counts[hour] += 1

        if hour_counts:
            most_common_hour, max_count = hour_counts.most_common(1)[0]

            def format_hour(h):
                h = h % 24
                if h == 0:
                    hour_12 = 12
                    suffix = "AM"
                elif 1 <= h < 12:
                    hour_12 = h
                    suffix = "AM"
                elif h == 12:
                    hour_12 = 12
                    suffix = "PM"
                else:
                    hour_12 = h - 12
                    suffix = "PM"
                return f"{hour_12}:00 {suffix}"

            productive_time_range = f"{format_hour(most_common_hour)} - {format_hour((most_common_hour + 1) % 24)}"
        else:
            productive_time_range = "No time data"

        # --- Color coding for percentage of successful days ---
        success_ratio = number_days_successful / days_stat_calc
        if success_ratio < 0.2:
            success_percentage_color = "color:red"
        elif success_ratio < 0.5:
            success_percentage_color = "color:yellow"
        else:
            success_percentage_color = "color:green"

        catches_ratio = len(entries)/days_stat_calc
        if catches_ratio < 0.5:
            catches_percentage_color = "color:red"
        elif catches_ratio < 0.75:
            catches_percentage_color = "color:yellow"
        else:
            catches_percentage_color = "color:green"

        # --- Display Monthly Statistics ---
        st.subheader(f"{selected_month} {year} - Visualization")
        st.markdown("**Statistics**")
        st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Fish Caught: {len(entries)}", unsafe_allow_html=True)        
        st.markdown(
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fish Caught/Day: "
            f"{len(entries)}/{days_stat_calc} - "
            f"<span style={catches_percentage_color}>"
            f"{round(catches_ratio * 100, 2)}%</span>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Days with a Catch: "
            f"{number_days_successful}/{days_in_month} - "
            f"<span style={success_percentage_color}>"
            f"{round(success_ratio * 100, 2)}%</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Most Productive Time: **{productive_time_range}**", unsafe_allow_html=True)

        # Add some vertical spacing
        st.write("")
        st.write("")
        st.write("")

        # --- Prepare DataFrame for Daily Catch Chart ---
        days = list(range(1, days_in_month + 1))
        values = catch_data

        df = pd.DataFrame({
            'Day': days,
            'Value': values
        })

        # Calculate tick values for Y axis (whole numbers)
        max_y = max(values) if values else 0
        tick_vals = list(range(0, max_y + 2)) if max_y > 0 else [0, 1]

        # --- Altair Bar Chart for Fish Caught per Day ---
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('Day:O', title='Day', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Value:Q', title=" ", axis=alt.Axis(values=tick_vals, format='d'))
        ).properties(
            width=700,
            height=400,
            title="Fish caught per day"
        )
        st.altair_chart(chart, use_container_width=False)

        # --- Prepare Data for Lure Variety Pie Chart ---
        lure_list = []
        lure_amount_list = []

        for entry in entries:
            lure = entry.get("Lure", "Unknown")
            if lure in lure_list:
                lure_amount_list[lure_list.index(lure)] += 1
            else:
                lure_list.append(lure)
                lure_amount_list.append(1)

        df_lures = pd.DataFrame({
            'Lures': lure_list,
            'Amount': lure_amount_list
        })

        custom_colors = [
            '#636EFA',  # Blue (Streamlit default)
            '#EF553B',  # Red
            '#00CC96',  # Green
            '#AB63FA',  # Purple
            '#FFA15A',  # Orange
            '#19D3F3',  # Light Blue
            '#FF6692',  # Pink
            '#B6E880',  # Light Green
            '#FF97FF',  # Light Pink
            '#FECB52'   # Yellow
        ]

        # --- Plotly Pie Chart for Lure Variety ---
        fig = px.pie(
            df_lures,
            values='Amount',
            names='Lures',
            title='Lure Variety',
            color_discrete_sequence=custom_colors
        )
        st.plotly_chart(fig)

        # --- Prepare Data for Species Variety Pie Chart ---
        fish_list = []
        fish_amount_list = []        

        for entry in entries:
            fish = entry.get("Species")
            if not fish:
                continue

            if fish in fish_list:
                fish_amount_list[fish_list.index(fish)] += 1
            else:
                fish_list.append(fish)
                fish_amount_list.append(1)

        df_fish = pd.DataFrame({
            'Fish': fish_list,
            'Amount': fish_amount_list
        })

        # --- Plotly Pie Chart for Lure Variety ---
        fig2 = px.pie(
            df_fish,
            values='Amount',
            names='Fish',
            title='Fish Variety',
            color_discrete_sequence=custom_colors
        )
        st.plotly_chart(fig2)

        st.markdown("---")

        # --- Detailed Catch Data by Date ---
        st.subheader(f"{selected_month} {year} - Catch Data")

        # Group entries by date for display
        entries_by_date = defaultdict(list)
        for entry in entries:
            date = entry.get("Date", "Unknown Date")
            entries_by_date[date].append(entry)

        for date, date_entries in entries_by_date.items():
            # Extract weather info from first entry of the day
            weather_raw = date_entries[0].get("Weather", "Unknown")
            weather_parts = [w.strip() for w in weather_raw.split(";") if w.strip()]

            forecast = weather_parts[0] if weather_parts else "Unknown"
            details = weather_parts[1:] if len(weather_parts) > 1 else []

            catch_label = "catch" if len(date_entries) == 1 else "catches"

            with st.expander(f"📅 {date} — {len(date_entries)} {catch_label}", expanded=False):
                # Weather forecast (underlined)
                st.markdown(f"<h3 style='text-decoration: underline;'>Weather: {forecast}</h3>", unsafe_allow_html=True)

                # Additional weather details
                for part in details:
                    if ":" in part:
                        label, value = part.split(":", 1)
                        st.write(f"**{label.strip()}:** {value.strip()}")

                st.markdown("---")

                # Display each catch entry for the day
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

                    st.write(f"**Lure:** {entry.get('Lure', 'Unknown')}")
                    st.write(f"**Rod:** {entry.get('Rod', 'Unknown')}")
                    st.write(f"**Time:** {entry.get('Time', 'Unknown')}")
                    st.write(f"**Location:** {entry.get('Location', 'Unknown')}")

                    if "Notes" in entry:
                        st.write(f"**Catch Notes:** {entry['Notes']}")

                    st.markdown("---")
