

# Loudness, Dancingability, and Energy Analysis of Pop Music

This project investigates the homogeneity of pop music from 1970 to 2020 using metrics like loudness, dancingability, and energy. By combining data scraping, Spotify API integration, and visualization, it explores trends and correlations in pop music across five decades.

# Workflow

Data Collection: Billboard Hot 100 data is scraped annually.

Spotify Integration: Track IDs are retrieved for each song, followed by the extraction of audio features such as danceability, energy, and loudness.

Data Cleaning: The collected data is cleaned to ensure accuracy and consistency.

Analysis: Statistical trends and correlations are analyzed to uncover insights.

Visualization: Graphs illustrate how pop music characteristics have evolved over time.

# Key Scripts

01-scraping.py: Collects Billboard data.

02-gettrackid.py and 03-getaudiofeatures.py: Fetch Spotify track IDs and audio features.

04-cleaning.py: Preprocesses and cleans data.

Visualization:

07-danceability_all.py: Danceability trends.

08-energy_all.py: Energy trends.

09-loudness_all.py: Loudness trends.
