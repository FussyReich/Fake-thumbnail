from apiclient.discovery import build
import json
import pandas as pd
import requests
import glob

#YOUTUBE_API_KEY = 'AIzaSyB_VBZGfozRL1ISMUQU95WIpfOuWI7wXto'
YOUTUBE_API_KEY='AIzaSyC_4Wj9v7fRtYTFZjt18TJLhkTS_GDYgoY'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)  

#検索情報
search_response = youtube.search().list(
part='snippet',
q='べあてぃぼん',#検索クエリ
order='viewCount',#視聴回数の多い順
type='video',
maxResults=50,
).execute()

channelID=search_response['items'][0]['snippet']['channelId']
channel=youtube.channels().list(
  part='snippet,contentDetails',
  id=channelID, #channelID
).execute()['items'][0]['contentDetails']
playlistid=channel['relatedPlaylists']['uploads']

def getVideoIds(playlist_id, page_token):
  items_info = youtube.playlistItems().list(
    part='contentDetails', 
    playlistId=playlist_id, 
    maxResults=50, 
    pageToken=page_token
  ).execute()
  video_ids = list(map(lambda item: item['contentDetails']['videoId'], items_info['items']))
  if 'nextPageToken' in items_info:
    video_ids.extend(getVideoIds(playlist_id, items_info['nextPageToken']))
  return video_ids


def getVideo_id():
  for Video_id in getVideoIds(playlistid,''):
    statistics=youtube.videos().list(
      part='snippet,statistics',#統計情報
      id=Video_id,
    ).execute()


def thumbanails():
  i=1
  for item in search_response.get('items', []):
    if item['id']['kind'] != 'youtube#video':
      continue
    for Video_id in getVideoIds(playlistid,''):
      statistics=youtube.videos().list(
        part='snippet,statistics',#統計情報
        id=Video_id,
      ).execute()['items'][0]
      thumbnailsURL=statistics['snippet']['thumbnails']['high']['url']
      URL={
        "ThumbnailsURL":{
          "url":thumbnailsURL,
          "videoId":Video_id,
          "statistics":statistics['statistics'],
        }
      }
      fileName=(f'./json/{i}.json')
      #response=requests.get(maxThumbnailsURL)
      response=requests.get(thumbnailsURL)
      #with open(f'./Good_Thumbnails/{i}.png', 'wb') as f:
      #  f.write(response.content)
      with open(f'./Thumbnails/{i}.png', 'wb') as f:
        f.write(response.content)
      with open(fileName, 'w') as f:
        json.dump(URL, f, indent=2, ensure_ascii=False)
        i+=1
      print(thumbnailsURL)

thumbanails()


  


