import streamlit as st
import json

# jsonString = """
# {
#   "FishingJournal": {
#     "2024": [      
#       {
#         "Date": "08/24/2024",
#         "Species": "Smallmouth Bass",
#         "Weight": "2.8 lbs",
#         "Lure": "Topwater Popper (Black & White)",
#         "Rod": "The Shrek",
#         "Time": "08:00 AM",
#         "Location": "The Camping Cove (East Bank)",
#         "Weather": "Clear skies with a high of 90°F and a low of 71°F"
#       }
#     ],
#     "2025": [
#       {
#         "Date": "02/26/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.16 lbs",
#         "Lure": "Yo-Zuri Rattl'n One Knock (Sexy Shad)",
#         "Rod": "The Fighter Jet",
#         "Time": "10:45 AM",
#         "Location": "Carbide Park (Hidden Cove, right side)",
#         "Weather": "Partly cloudy with a high of 58°F and a low of 35°F"
#       },
#       {
#         "Date": "03/03/2025",
#         "Species": "Skipjack Shad",
#         "Weight": "Dink",
#         "Lure": "Black Back and Chrome Knock-N-Trap",
#         "Rod": "The Red Rider",
#         "Time": "11:15 AM",
#         "Location": "Carbide Park (North Western Drop Off)",
#         "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
#       },
#       {
#         "Date": "03/03/2025",
#         "Species": "Skipjack Shad",
#         "Weight": "Dink",
#         "Lure": "Black Back and Chrome Knock-N-Trap",
#         "Rod": "The Red Rider",
#         "Time": "11:35 AM",
#         "Location": "Carbide Park (North Western Drop Off)",
#         "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
#       },
#       {      
#         "Date": "03/03/2025",
#         "Species": "Skipjack Shad",
#         "Weight": "Dink",
#         "Lure": "Ghost Sexy Shad Yo-Zuri DR-X Jerkbait",
#         "Rod": "The Fighter Jet",
#         "Time": "12:30 PM",
#         "Location": "Carbide Park (North Western Drop Off)",
#         "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
#       },
#       {
#         "Date": "03/27/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.7 lbs",
#         "Lure": "Red with Blue Flake Trick Worm on a Shaky Head Rig",
#         "Rod": "The Blue Jay",
#         "Time": "12:00 PM",
#         "Location": "Carbide Park (North Western Drop Off)",
#         "Weather": "Overcast with a high of 65°F and a low of 50°F"
#       },
#       {    
#         "Date": "03/28/2025",
#         "Note": "1 hour session, 21 White Bass and 3 Yellow Bass",
#         "Lure": "All White Marabou Jig",
#         "Rod": "The Blue Jay",
#         "Time": "10:45 AM",
#         "Location": "Clinch River (Mouth of Hinds Creek)",
#         "Weather": "Partly cloudy with a high of 68°F and a low of 52°F"
#       },
#       {      
#         "Date": "04/01/2025",
#         "Note": "2 hour session, 4 White Bass and 1 Shad",
#         "Lure": "All White Marabou Jig",
#         "Rod": "The Blue Jay and The Hay Penny",
#         "Time": "12:30 PM",
#         "Location": "Clinch River (Mouth of Hinds Creek and Culvert across the river)",
#         "Weather": "Clear skies with a high of 72°F and a low of 55°F"
#       },
#       {      
#         "Date": "04/05/2025",      
#         "Species": "Channel Catfish",      
#         "Weight": "~2 lbs",      
#         "Lure": "PowerBait Panfish Dots (Pink) on a Bobber Rig",      
#         "Rod": "The Dragonfly",      
#         "Time": "7:15 PM",      
#         "Location": "Lake Gisell",      
#         "Weather": "Very warm with intervals of clouds and sunshine, High: 86°F, Low: 65°F"
#       },
#       {      
#         "Date": "04/07/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1 lb",
#         "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Okeechobee Craw",
#         "Rod": "The Javelin",      
#         "Time": "11:10 AM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Cloudy, 53°F, Barometric Pressure: 29.75 inHg (Steady), Humidity: 86%"      
#       },
#       {
#         "Date": "04/07/2025",  
#         "Species": "Largemouth Bass",
#         "Weight": "Dink",
#         "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",
#         "Rod": "The Blue Jay",
#         "Time": "12:05 PM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Cloudy, 53°F, Barometric Pressure: 29.75 inHg (Steady), Humidity: 86%"
#       },
#       {      
#         "Date": "04/09/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "1.39 lbs",      
#         "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Okeechobee Craw",      
#         "Rod": "The Javelin",      
#         "Time": "11:12 AM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Sunny, 51°F, Barometric Pressure: 30.04 inHg (Steady), Humidity: 59%"      
#       },
#       {      
#         "Date": "04/09/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "1.3 lbs",      
#         "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
#         "Rod": "The Blue Jay",      
#         "Time": "12:00 PM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Sunny, 51°F, Barometric Pressure: 30.04 inHg (Steady), Humidity: 59%"      
#       },
#       {      
#         "Date": "04/15/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.7 lbs",      
#         "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
#         "Rod": "The Blue Jay",      
#         "Time": "12:27 PM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Mostly sunny, 76°F, Barometric Pressure: 30.06 inHg (Falling), Winds: SW at 10–12 mph, Humidity: 64%, MoonPhase: Waning Gibbous (~30%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/16/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.5 lbs",      
#         "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Blue Bug",      
#         "Rod": "The Javelin",      
#         "Time": "11:15 AM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Partly cloudy, 77°F, Barometric Pressure: 29.97 inHg (Steady), Winds: SSW at 12 mph, Humidity: 54%, MoonPhase: Waning Gibbous (~30%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/17/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.82 lbs",      
#         "Lure": "Strike King 1/2 oz Green Pumpkin Structure Jig with a Rage Craw trailer in Summer Craw",      
#         "Rod": "The Javelin",      
#         "Time": "11:12 AM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Cloudy, 73°F, Barometric Pressure: 29.85 inHg (Falling), Winds: SW at 10 mph, Humidity: 50%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/18/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.75 lbs",      
#         "Lure": "3/16 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
#         "Rod": "The Blue Jay",      
#         "Time": "10:54 AM",      
#         "Location": "Lake Gisell",      
#         "Weather": "Partly sunny, 70°F, Barometric Pressure: 29.92 inHg (Steady), Winds: S at 9 mph, Humidity: 48%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/18/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "Dink",      
#         "Lure": "3/16 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
#         "Rod": "The Blue Jay",      
#         "Time": "11:01 AM",      
#         "Location": "Lake Gisell",      
#         "Weather": "Partly sunny, 71°F, Barometric Pressure: 29.92 inHg (Steady), Winds: S at 9 mph, Humidity: 48%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/19/2025",      
#         "Session": "2 hour 15 minute session",      
#         "SpeciesCaught": ["4 Yellow Bass","2 Shad"],      
#         "Lure": "1/4 oz. white Rooster Tail & 1/8 oz. All White Marabou Jig",      
#         "Rod": "The Blue Jay and The Hay Penny",      
#         "Time": "8:00 AM",      
#         "Location": "Clinch River (Mouth of Hinds Creek)",      
#         "Weather": "Mostly cloudy, 67°F, Barometric Pressure: 30.02 inHg (Rising), Winds: NE at 5 mph, Humidity: 45%, MoonPhase: Waning Gibbous (~70%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/20/2025",      
#         "Session": "1 hour 15 minute session",      
#         "SpeciesCaught": ["12 Yellow Bass","3 White Bass"],      
#         "Lure": "1/8 oz. All White Marabou Jig",      
#         "Rod": "The Blue Jay",      
#         "Time": "8:45 AM",      
#         "Location": "Clinch River (Mouth of Hinds Creek)",    
#         "Weather": "Sunny, 69°F, Barometric Pressure: 30.12 inHg (Rising), Winds: E at 7 mph, Humidity: 44%, MoonPhase: Third Quarter (~50%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/21/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.5 lbs",      
#         "Lure": "Dirty Jigs Tour Level 3/8 oz PB&J Finesse Football Jig with a Rage Bug trailer in Junebug",      
#         "Rod": "The Javelin",      
#         "Time": "11:20 AM",      
#         "Location": "Carbide Park – North Western Drop Off",      
#         "Weather": "Partly cloudy, 72°F, Barometric Pressure: 30.18 inHg (Steady), Winds: SE at 6 mph, Humidity: 42%, MoonPhase: Waning Crescent (~40%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/26/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.6 lbs",      
#         "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",      
#         "Rod": "The Blue Jay",      
#         "Time": "1:50 PM",      
#         "Location": "Lake Gisell",      
#         "Weather": "Cloudy, 75°F, Barometric Pressure: 30.05 inHg (Falling), Winds: S at 8 mph, Humidity: 52%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/26/2025",      
#         "Species": "Largemouth Bass",      
#         "Weight": "0.5 lbs",      
#         "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",      
#         "Rod": "The Blue Jay",      
#         "Time": "2:14 PM",      
#         "Location": "Lake Gisell",      
#         "Weather": "Cloudy, 75°F, Barometric Pressure: 30.05 inHg (Falling), Winds: S at 8 mph, Humidity: 52%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
#       },
#       {      
#         "Date": "04/27/2025",      
#         "Session": "3 hour session",      
#         "SpeciesCaught": ["4 White Bass","3 Yellow Bass","1 Drum","1 Rainbow Trout","1 Shad"],      
#         "Lure": "1/8 oz All-White Marabou Jig",      
#         "Rod": "The Blue Jay and The Hay Penny",      
#         "Time": "8:30 AM",      
#         "Location": "Clinch River (Mouth of Hinds Creek)",      
#         "Weather": "Partly sunny, 66°F, Barometric Pressure: 30.15 inHg (Steady), Winds: N at 5 mph, Humidity: 45%, MoonPhase: Waning Crescent (~30%), BiteForecast: Good"      
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.02 lbs",
#         "Lure": "Greenfish Tackle Badger 1/2 oz Flip Jig in Junebug with a Rage Bug trailer in Junebug",
#         "Rod": "The Javelin",
#         "Time": "11:01 AM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "0.80 lbs",
#         "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
#         "Rod": "The Javelin",
#         "Time": "11:27 AM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.15 lbs",
#         "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
#         "Rod": "The Javelin",
#         "Time": "11:53 AM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.24 lbs",
#         "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
#         "Rod": "The Javelin",
#         "Time": "12:02 PM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.28 lbs",
#         "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",
#         "Rod": "The Blue Jay",
#         "Time": "12:33 PM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/28/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.16 lbs",
#         "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",
#         "Rod": "The Blue Jay",
#         "Time": "12:40 PM",
#         "Location": "Carbide Park – North Western Drop Off",
#         "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/29/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "0.5 lbs",
#         "Lure": "Strike King 1/2 oz Peanut Butter Bug Structure Jig with a Rage Bug trailer in Smoke Purple Black Flake",
#         "Rod": "The Javelin",
#         "Time": "10:55 AM",
#         "Location": "Clark Center Park – Northern Dock",
#         "Weather": "Mostly cloudy; 81°F high, 64°F low, current 79°F; Barometric Pressure: 30.23 inHg (Rising); Winds: S at 13 mph; Humidity: 53%; MoonPhase: Waning Crescent (~15%); BiteForecast: Good"
#       },
#       {
#         "Date": "04/29/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "2.28 lbs",
#         "Lure": "Strike King 1/2 oz Peanut Butter Bug Structure Jig with a Rage Bug trailer in Smoke Purple Black Flake",
#         "Rod": "The Javelin",
#         "Time": "11:01 AM",
#         "Location": "Clark Center Park – Northern Dock",
#         "Weather": "Mostly cloudy; 81°F high, 64°F low, current 79°F; Barometric Pressure: 30.23 inHg (Rising); Winds: S at 13 mph; Humidity: 53%; MoonPhase: Waning Crescent (~15%); BiteForecast: Good"
#       },
#       {
#         "Date": "05/05/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.25 lb.",
#         "Lure": "Strike King Bleeding Jig 1/4oz Rage with a Baby Menace trailer in Green Pumpkin",
#         "Rod": "The Blue Jay",
#         "Time": "11:13 AM",
#         "Location": "Carbide Park (Northern Dock)",
#         "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
#       },
#       {
#         "Date": "05/05/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1 lb.",
#         "Lure": "Strike King Bleeding Jig 1/4oz Rage with a Baby Menace trailer in Green Pumpkin",
#         "Rod": "The Blue Jay",
#         "Time": "11:30 AM",
#         "Location": "Carbide Park (Northern Dock)",
#         "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
#       },
#       {
#         "Date": "05/05/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "0.5 lb.",
#         "Lure": "3/16 oz Screw‑Lock Shaky Head with a Rage Menace trailer in Black and Blue",
#         "Rod": "The Blue Jay",
#         "Time": "11:41 AM",
#         "Location": "Carbide Park (Northern Dock)",
#         "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
#       },
#       {
#         "Date": "05/05/2025",
#         "Species": "Largemouth Bass",
#         "Weight": "1.5 lb.",
#         "Lure": "3/16 oz Screw‑Lock Shaky Head with a Baby Menace trailer in Green Pumpkin",
#         "Rod": "The Javelin",
#         "Time": "12:32 PM",
#         "Location": "Carbide Park (Northern Dock)",
#         "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
#       }
#     ]
#   }
# }
# """
jsonString = """
{
  "FishingJournal": {
    "2024": {
      "August" : [
        {
          "Date": "08/24/2024",
          "Species": "Smallmouth Bass",
          "Weight": "2.8 lbs",
          "Lure": "Topwater Popper (Black & White)",
          "Rod": "The Shrek",
          "Time": "08:00 AM",
          "Location": "The Camping Cove (East Bank)",
          "Weather": "Clear skies with a high of 90°F and a low of 71°F"
        }
      ]      
    },
    "2025": {
      "January" : [],
      "February" : [
        {
          "Date": "02/26/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.16 lbs",
          "Lure": "Yo-Zuri Rattl'n One Knock (Sexy Shad)",
          "Rod": "The Fighter Jet",
          "Time": "10:45 AM",
          "Location": "Carbide Park (Hidden Cove, right side)",
          "Weather": "Partly cloudy with a high of 58°F and a low of 35°F"
        }
      ],
      "March" : [
        {
          "Date": "03/03/2025",
          "Species": "Skipjack Shad",
          "Weight": "Dink",
          "Lure": "Black Back and Chrome Knock-N-Trap",
          "Rod": "The Red Rider",
          "Time": "11:15 AM",
          "Location": "Carbide Park (North Western Drop Off)",
          "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
        },
        {
          "Date": "03/03/2025",
          "Species": "Skipjack Shad",
          "Weight": "Dink",
          "Lure": "Black Back and Chrome Knock-N-Trap",
          "Rod": "The Red Rider",
          "Time": "11:35 AM",
          "Location": "Carbide Park (North Western Drop Off)",
          "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
        },
        {      
          "Date": "03/03/2025",
          "Species": "Skipjack Shad",
          "Weight": "Dink",
          "Lure": "Ghost Sexy Shad Yo-Zuri DR-X Jerkbait",
          "Rod": "The Fighter Jet",
          "Time": "12:30 PM",
          "Location": "Carbide Park (North Western Drop Off)",
          "Weather": "Mostly cloudy with a high of 62°F and a low of 42°F"
        },
        {
          "Date": "03/27/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.7 lbs",
          "Lure": "Red with Blue Flake Trick Worm on a Shaky Head Rig",
          "Rod": "The Blue Jay",
          "Time": "12:00 PM",
          "Location": "Carbide Park (North Western Drop Off)",
          "Weather": "Overcast with a high of 65°F and a low of 50°F"
        },
        {    
          "Date": "03/28/2025",
          "Note": "1 hour session, 21 White Bass and 3 Yellow Bass",
          "Lure": "All White Marabou Jig",
          "Rod": "The Blue Jay",
          "Time": "10:45 AM",
          "Location": "Clinch River (Mouth of Hinds Creek)",
          "Weather": "Partly cloudy with a high of 68°F and a low of 52°F"
        }
      ],
      "April" : [
        {      
          "Date": "04/01/2025",
          "Note": "2 hour session, 4 White Bass and 1 Shad",
          "Lure": "All White Marabou Jig",
          "Rod": "The Blue Jay and The Hay Penny",
          "Time": "12:30 PM",
          "Location": "Clinch River (Mouth of Hinds Creek and Culvert across the river)",
          "Weather": "Clear skies with a high of 72°F and a low of 55°F"
        },
        {      
          "Date": "04/05/2025",      
          "Species": "Channel Catfish",      
          "Weight": "~2 lbs",      
          "Lure": "PowerBait Panfish Dots (Pink) on a Bobber Rig",      
          "Rod": "The Dragonfly",      
          "Time": "7:15 PM",      
          "Location": "Lake Gisell",      
          "Weather": "Very warm with intervals of clouds and sunshine, High: 86°F, Low: 65°F"
        },
        {      
          "Date": "04/07/2025",
          "Species": "Largemouth Bass",
          "Weight": "1 lb",
          "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Okeechobee Craw",
          "Rod": "The Javelin",      
          "Time": "11:10 AM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Cloudy, 53°F, Barometric Pressure: 29.75 inHg (Steady), Humidity: 86%"      
        },
        {
          "Date": "04/07/2025",  
          "Species": "Largemouth Bass",
          "Weight": "Dink",
          "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",
          "Rod": "The Blue Jay",
          "Time": "12:05 PM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Cloudy, 53°F, Barometric Pressure: 29.75 inHg (Steady), Humidity: 86%"
        },
        {      
          "Date": "04/09/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "1.39 lbs",      
          "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Okeechobee Craw",      
          "Rod": "The Javelin",      
          "Time": "11:12 AM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Sunny, 51°F, Barometric Pressure: 30.04 inHg (Steady), Humidity: 59%"      
        },
        {      
          "Date": "04/09/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "1.3 lbs",      
          "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
          "Rod": "The Blue Jay",      
          "Time": "12:00 PM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Sunny, 51°F, Barometric Pressure: 30.04 inHg (Steady), Humidity: 59%"      
        },
        {      
          "Date": "04/15/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.7 lbs",      
          "Lure": "1/8 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
          "Rod": "The Blue Jay",      
          "Time": "12:27 PM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Mostly sunny, 76°F, Barometric Pressure: 30.06 inHg (Falling), Winds: SW at 10–12 mph, Humidity: 64%, MoonPhase: Waning Gibbous (~30%), BiteForecast: Good"      
        },
        {      
          "Date": "04/16/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.5 lbs",      
          "Lure": "Strike King 1/2 oz Peanut Butter Structure Jig with a Rage Bug trailer in Blue Bug",      
          "Rod": "The Javelin",      
          "Time": "11:15 AM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Partly cloudy, 77°F, Barometric Pressure: 29.97 inHg (Steady), Winds: SSW at 12 mph, Humidity: 54%, MoonPhase: Waning Gibbous (~30%), BiteForecast: Good"      
        },
        {      
          "Date": "04/17/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.82 lbs",      
          "Lure": "Strike King 1/2 oz Green Pumpkin Structure Jig with a Rage Craw trailer in Summer Craw",      
          "Rod": "The Javelin",      
          "Time": "11:12 AM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Cloudy, 73°F, Barometric Pressure: 29.85 inHg (Falling), Winds: SW at 10 mph, Humidity: 50%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
        },
        {      
          "Date": "04/18/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.75 lbs",      
          "Lure": "3/16 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
          "Rod": "The Blue Jay",      
          "Time": "10:54 AM",      
          "Location": "Lake Gisell",      
          "Weather": "Partly sunny, 70°F, Barometric Pressure: 29.92 inHg (Steady), Winds: S at 9 mph, Humidity: 48%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
        },
        {      
          "Date": "04/18/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "Dink",      
          "Lure": "3/16 oz. Screw lock Shaky head with a Trick Worm in Junebug",      
          "Rod": "The Blue Jay",      
          "Time": "11:01 AM",      
          "Location": "Lake Gisell",      
          "Weather": "Partly sunny, 71°F, Barometric Pressure: 29.92 inHg (Steady), Winds: S at 9 mph, Humidity: 48%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
        },
        {      
          "Date": "04/19/2025",      
          "Session": "2 hour 15 minute session",      
          "SpeciesCaught": ["4 Yellow Bass","2 Shad"],      
          "Lure": "1/4 oz. white Rooster Tail & 1/8 oz. All White Marabou Jig",      
          "Rod": "The Blue Jay and The Hay Penny",      
          "Time": "8:00 AM",      
          "Location": "Clinch River (Mouth of Hinds Creek)",      
          "Weather": "Mostly cloudy, 67°F, Barometric Pressure: 30.02 inHg (Rising), Winds: NE at 5 mph, Humidity: 45%, MoonPhase: Waning Gibbous (~70%), BiteForecast: Good"      
        },
        {      
          "Date": "04/20/2025",      
          "Session": "1 hour 15 minute session",      
          "SpeciesCaught": ["12 Yellow Bass","3 White Bass"],      
          "Lure": "1/8 oz. All White Marabou Jig",      
          "Rod": "The Blue Jay",      
          "Time": "8:45 AM",      
          "Location": "Clinch River (Mouth of Hinds Creek)",    
          "Weather": "Sunny, 69°F, Barometric Pressure: 30.12 inHg (Rising), Winds: E at 7 mph, Humidity: 44%, MoonPhase: Third Quarter (~50%), BiteForecast: Good"      
        },
        {      
          "Date": "04/21/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.5 lbs",      
          "Lure": "Dirty Jigs Tour Level 3/8 oz PB&J Finesse Football Jig with a Rage Bug trailer in Junebug",      
          "Rod": "The Javelin",      
          "Time": "11:20 AM",      
          "Location": "Carbide Park – North Western Drop Off",      
          "Weather": "Partly cloudy, 72°F, Barometric Pressure: 30.18 inHg (Steady), Winds: SE at 6 mph, Humidity: 42%, MoonPhase: Waning Crescent (~40%), BiteForecast: Good"      
        },
        {      
          "Date": "04/26/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.6 lbs",      
          "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",      
          "Rod": "The Blue Jay",      
          "Time": "1:50 PM",      
          "Location": "Lake Gisell",      
          "Weather": "Cloudy, 75°F, Barometric Pressure: 30.05 inHg (Falling), Winds: S at 8 mph, Humidity: 52%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
        },
        {      
          "Date": "04/26/2025",      
          "Species": "Largemouth Bass",      
          "Weight": "0.5 lbs",      
          "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",      
          "Rod": "The Blue Jay",      
          "Time": "2:14 PM",      
          "Location": "Lake Gisell",      
          "Weather": "Cloudy, 75°F, Barometric Pressure: 30.05 inHg (Falling), Winds: S at 8 mph, Humidity: 52%, MoonPhase: Waning Crescent (~25%), BiteForecast: Good"      
        },
        {      
          "Date": "04/27/2025",      
          "Session": "3 hour session",      
          "SpeciesCaught": ["4 White Bass","3 Yellow Bass","1 Drum","1 Rainbow Trout","1 Shad"],      
          "Lure": "1/8 oz All-White Marabou Jig",      
          "Rod": "The Blue Jay and The Hay Penny",      
          "Time": "8:30 AM",      
          "Location": "Clinch River (Mouth of Hinds Creek)",      
          "Weather": "Partly sunny, 66°F, Barometric Pressure: 30.15 inHg (Steady), Winds: N at 5 mph, Humidity: 45%, MoonPhase: Waning Crescent (~30%), BiteForecast: Good"      
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.02 lbs",
          "Lure": "Greenfish Tackle Badger 1/2 oz Flip Jig in Junebug with a Rage Bug trailer in Junebug",
          "Rod": "The Javelin",
          "Time": "11:01 AM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "0.80 lbs",
          "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
          "Rod": "The Javelin",
          "Time": "11:27 AM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.15 lbs",
          "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
          "Rod": "The Javelin",
          "Time": "11:53 AM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.24 lbs",
          "Lure": "Strike King 1/2 oz Hard Candy Structure Jig with a Rage Bug trailer in Junebug",
          "Rod": "The Javelin",
          "Time": "12:02 PM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.28 lbs",
          "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",
          "Rod": "The Blue Jay",
          "Time": "12:33 PM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/28/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.16 lbs",
          "Lure": "3/16 oz Screw-Lock Shaky head with a Rage Menace in Bama Bug",
          "Rod": "The Blue Jay",
          "Time": "12:40 PM",
          "Location": "Carbide Park – North Western Drop Off",
          "Weather": "Partly cloudy; 82.9°F high, 51.1°F low, current 66.9°F; Barometric Pressure: 30.10 inHg (Steady); Winds: Light and variable at ~5 mph; Humidity: 67%; MoonPhase: Waning Crescent (~20%); BiteForecast: Good"
        },
        {
          "Date": "04/29/2025",
          "Species": "Largemouth Bass",
          "Weight": "0.5 lbs",
          "Lure": "Strike King 1/2 oz Peanut Butter Bug Structure Jig with a Rage Bug trailer in Smoke Purple Black Flake",
          "Rod": "The Javelin",
          "Time": "10:55 AM",
          "Location": "Clark Center Park – Northern Dock",
          "Weather": "Mostly cloudy; 81°F high, 64°F low, current 79°F; Barometric Pressure: 30.23 inHg (Rising); Winds: S at 13 mph; Humidity: 53%; MoonPhase: Waning Crescent (~15%); BiteForecast: Good"
        },
        {
          "Date": "04/29/2025",
          "Species": "Largemouth Bass",
          "Weight": "2.28 lbs",
          "Lure": "Strike King 1/2 oz Peanut Butter Bug Structure Jig with a Rage Bug trailer in Smoke Purple Black Flake",
          "Rod": "The Javelin",
          "Time": "11:01 AM",
          "Location": "Clark Center Park – Northern Dock",
          "Weather": "Mostly cloudy; 81°F high, 64°F low, current 79°F; Barometric Pressure: 30.23 inHg (Rising); Winds: S at 13 mph; Humidity: 53%; MoonPhase: Waning Crescent (~15%); BiteForecast: Good"
        }
      ],
      "May" : [
        {
          "Date": "05/05/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.25 lb.",
          "Lure": "Strike King Bleeding Jig 1/4oz Rage with a Baby Menace trailer in Green Pumpkin",
          "Rod": "The Blue Jay",
          "Time": "11:13 AM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
        },
        {
          "Date": "05/05/2025",
          "Species": "Largemouth Bass",
          "Weight": "1 lb.",
          "Lure": "Strike King Bleeding Jig 1/4oz Rage with a Baby Menace trailer in Green Pumpkin",
          "Rod": "The Blue Jay",
          "Time": "11:30 AM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
        },
        {
          "Date": "05/05/2025",
          "Species": "Largemouth Bass",
          "Weight": "0.5 lb.",
          "Lure": "3/16 oz Screw‑Lock Shaky Head with a Rage Menace trailer in Black and Blue",
          "Rod": "The Blue Jay",
          "Time": "11:41 AM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
        },
        {
          "Date": "05/05/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.5 lb.",
          "Lure": "3/16 oz Screw‑Lock Shaky Head with a Baby Menace trailer in Green Pumpkin",
          "Rod": "The Javelin",
          "Time": "12:32 PM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Mostly cloudy; 62°F high, 48°F low; current 58°F; Barometric Pressure: 29.98 inHg (Falling); Winds: SW at 10–15 mph; Humidity: 58%; MoonPhase: Waxing Gibbous (~53%); BiteForecast: Good"
        },
        {
          "Date": "05/06/2025",
          "Species": "Largemouth Bass",
          "Weight": "~1 lb",
          "Lure": "3/16 oz Screw‑Lock Shaky Head with a Rage Menace trailer in MM Moonlight",
          "Rod": "The Blue Jay",
          "Time": "11:13 AM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Partly cloudy; high 73°F, low 51°F; current 62°F; Barometric Pressure: 30.00 inHg (Steady); Winds: SW at 10 mph; Humidity: 55%; MoonPhase: Waxing Gibbous (~60%); BiteForecast: Good"
        },
        {
          "Date": "05/06/2025",
          "Species": "Largemouth Bass",
          "Weight": "~0.5 lb",
          "Lure": "3/16 oz Screw‑Lock Shaky Head with a Rage Menace trailer in MM Moonlight",
          "Rod": "The Blue Jay",
          "Time": "11:30 AM",
          "Location": "Carbide Park (Northern Dock)",
          "Weather": "Partly cloudy; high 73°F, low 51°F; current 62°F; Barometric Pressure: 30.00 inHg (Steady); Winds: SW at 10 mph; Humidity: 55%; MoonPhase: Waxing Gibbous (~60%); BiteForecast: Good"
        },
        {
          "Date": "05/09/2025",
          "Species": "Largemouth Bass",
          "Weight": "1.16 lbs",
          "Lure": "3/16 oz Screw‑Lock Shaky Head with a Strike King 3X Elaztech Finesse Worm in Junebug",
          "Rod": "The Blue Jay",
          "Time": "10:59 AM",
          "Location": "Carbide Park (Northern Rocky Bank)",
          "Weather": "Mostly cloudy; high 66°F, low 50°F; current 60°F; Barometric Pressure: 29.94 inHg (Falling); Winds: SW at 10–12 mph; Humidity: 62%; MoonPhase: Waxing Gibbous (~90%); BiteForecast: Good"
        },
        {
          "Date": "05/09/2025",
          "Species": "Largemouth Bass",
          "Weight": "~0.7 lbs",
          "Lure": "Texas Rigged Yum Dinger in Green Pumpkin with Red Flake on a 3/0 EWG with 3/8 oz tungsten",
          "Rod": "The Javelin",
          "Time": "10:36 AM",
          "Location": "Carbide Park (Northern Rocky Bank)",
          "Weather": "Mostly cloudy; high 66°F, low 50°F; current 60°F; Barometric Pressure: 29.94 inHg (Falling); Winds: SW at 10–12 mph; Humidity: 62%; MoonPhase: Waxing Gibbous (~90%); BiteForecast: Good"
        }
      ]
    }
  }
}
"""

# try:
#     data = json.loads(jsonString)
# except json.JSONDecodeError as e:
#     st.error(f"Error loading JSON: {e}")
#     st.stop()

# # Title
# st.title("🎣 Fishing Journal")

# # Let user pick a year
# years = list(data["FishingJournal"].keys())
# selected_year = st.selectbox("Select Year", years)

# # Let user pick a year
# months = list(years["FishingJournal"].keys())
# selected_year = st.selectbox("Select Year", months)

# # Display entries for that year
# st.header(f"Entries for {selected_year}")

# for entry in data["FishingJournal"][selected_year]:
#     st.subheader(f"📅 {entry.get('Date', 'Unknown Date')}")
    
#     if "Session" in entry:
#         st.write(f"**Session:** {entry['Session']}")
    
#     if "Species" in entry:
#         st.write(f"**Species:** {entry['Species']}")
#     if "SpeciesCaught" in entry:
#         st.write(f"**Species Caught:** {', '.join(entry['SpeciesCaught'])}")
    
#     if "Weight" in entry:
#         st.write(f"**Weight:** {entry['Weight']}")
    
#     st.write(f"**Lure:** {entry['Lure']}")
#     st.write(f"**Rod:** {entry['Rod']}")
#     st.write(f"**Time:** {entry['Time']}")
#     st.write(f"**Location:** {entry['Location']}")
#     st.write(f"**Weather:** {entry['Weather']}")
    
#     st.markdown("---")  # Divider

# Load JSON
try:
    data = json.loads(jsonString)
except json.JSONDecodeError as e:
    st.error(f"Error loading JSON: {e}")
    st.stop()

# Title
st.title("🎣 Fishing Journal")

# Get available years
years = list(data["FishingJournal"].keys())
selected_year = st.selectbox("Select Year", years)

# Get available months for selected year
months = list(data["FishingJournal"][selected_year].keys())
selected_month = st.selectbox("Select Month", months)

# Display entries
st.header(f"Entries for {selected_month} {selected_year}")

entries = data["FishingJournal"][selected_year][selected_month]

if not entries:
    st.info("No entries for this month.")
else:
    for entry in entries:
        st.subheader(f"📅 {entry.get('Date', 'Unknown Date')}")
        
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
        st.write(f"**Weather:** {entry['Weather']}")
        st.markdown("---")