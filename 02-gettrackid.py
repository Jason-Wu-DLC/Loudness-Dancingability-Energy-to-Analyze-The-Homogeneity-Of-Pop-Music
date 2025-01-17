import json
import requests
import pandas as pd
import pause

# Read the data produced by the previous script
chartdata = pd.read_csv('billboard.csv', sep=',')
chartdata = chartdata.T.to_dict().values()

for entry in chartdata:

    # Build query (consists of artist and title)
    query = entry['artist'] + ' ' + entry['title']
    print('Searching', query)

    token = 'BQC-OqSMeATPn1jboU3AIfkB8H15eQZFO7-4pjdSLMoAHdtGKEyn-r70ST6ivcqnyoRlU991squ2_fgIH5E'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    # Set parameters
    params = (
        ('q', query),
        ('type', 'track'),
        ('limit', '1'),
    )

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)  # Make request

    print(response)  # We want code [200] here

    data = json.loads(response.text)  # Convert response to text/dict

    try:  # Not every query returns a positive result. If we try to get information from a response of a failed search, it crashes the script because that information is not there, hence the try/except logic
        trackid = data['tracks']['items'][0]['id']  # Isolate track id
        print(trackid)
    except:
        trackid = ''
        print('Track id not found')

    entry['trackid'] = trackid  # Add track id to the active dictionary

    savedata = pd.DataFrame(chartdata)  # Convert list data to a dataframe
    savedata.to_csv('spotify_trackid.csv', sep=',', index=False)  # Save dataframe to file

    pause.seconds(.15)  # Pause in between requests