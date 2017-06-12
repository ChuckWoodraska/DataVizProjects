from apiclient.discovery import build
import configparser
import csv

config = configparser.ConfigParser()
config.read('config.ini')

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_DEVKEY = config['YOUTUBE']['DEVKEY']
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DEVKEY)
# Step 1 - Get playlist
playlist_id = "PLKl7PvuQ7ZefAXuokfmu7G8bAD7KjjGrB"
playlistitems_list_request = youtube.playlistItems().list(playlistId=playlist_id, part="snippet", maxResults=50)

# Step 2 - Open csv for writing data
fieldnames = ['Title', 'Duration(Seconds)', 'YoutubeVideoId']
writer = csv.DictWriter(open('../data/guinness.csv', 'w'), fieldnames=fieldnames)
writer.writeheader()

# Step 3 - Loop through playlist foreach video and extract
while playlistitems_list_request:
    playlistitems_list_response = playlistitems_list_request.execute()
    for video in playlistitems_list_response['items']:
        video_response = youtube.videos().list(id=video['snippet']['resourceId']['videoId'], part='snippet, contentDetails').execute()
        writer.writerow({'Title': video['snippet']['title'],
                         'Duration(Seconds)': video_response['items'][0]['contentDetails']['duration'].split('PT')[1].split('S')[0],
                         'YoutubeVideoId': video['snippet']['resourceId']['videoId']})
    playlistitems_list_request = youtube.playlistItems().list_next(playlistitems_list_request,
                                                                   playlistitems_list_response)


