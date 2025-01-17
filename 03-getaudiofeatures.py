import json
import requests
import pandas as pd
import time

# Read the data produced by the previous script
spotifydata = pd.read_csv('spotify_trackid.csv',sep=',')
spotifydata = spotifydata.T.to_dict().values()

for entry in spotifydata:

	token = 'BQAisSCJXcU6GWz31_lYmE_m8LuhImOVKB30nrBQxYPVNASl3Terex_rqb6J56o0AeX5SIDpCgPWyqR_qKs'
	headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer ' + token,
	}

	trackid = entry['trackid'] # Add in the trackid

	try: # Not every song has a valid trackid, if not available, the request would fail and crash the script, hence the try-except.

		print('Querying',trackid)

		response = requests.get('https://api.spotify.com/v1/audio-features/'+trackid, headers=headers) # Make request

		print(response) # [200] in case of success
		data = json.loads(response.text) # Convert response to text/dict

		# Get every audio feature from the response and add it as a key in the active dictionary
		entry['danceability'] = data['danceability']
		entry['energy'] = data['energy']
		entry['key'] = data['key']
		entry['loudness'] = data['loudness']
		entry['mode'] = data['mode']
		entry['speechiness'] = data['speechiness']
		entry['acousticness'] = data['acousticness']
		entry['instrumentalness'] = data['instrumentalness']
		entry['liveness'] = data['liveness']
		entry['valence'] = data['valence']
		entry['tempo'] = data['tempo']

		savedata = pd.DataFrame(spotifydata) # Convert list data to a dataframe
		savedata.to_csv('spotify_audiofeatures.csv',sep=',',index=False) # Save dataframe to file

		#time.sleep(.15) # Pause in between requests

	except:
		print('No audio features returned',trackid)
