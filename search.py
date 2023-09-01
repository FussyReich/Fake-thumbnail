from apiclient.discovery import build
import json
import pandas as pd
import requests
import glob

YOUTUBE_API_KEY = 'AIzaSyB_VBZGfozRL1ISMUQU95WIpfOuWI7wXto'
#YOUTUBE_API_KEY='AIzaSyCKCZjShvqfwLk21MYu_u8MlHyMTG3m5-Q'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)  

#検索情報
search_response = youtube.search().list(
part='snippet',
q='あもとっと',#検索クエリ
order='viewCount',#視聴回数の多い順
type='video',
maxResults=50,
).execute()
#videoID=search_response['items'][0]['id']['videoId'] #print(search_response['items'][0]['id']['videoId'])

def get_thumbanailsURL():
  i=1
  for item in search_response.get('items', []):
    if item['id']['kind'] != 'youtube#video':
      continue
    thumbnailsURL=item['snippet']['thumbnails']['high']['url']
    maxThumbnailsURL=thumbnailsURL.replace('hq', 'maxres')
    videoID=item['id']['videoId']
    statistics=youtube.videos().list(
      part='statistics',#統計情報
      id=f'{videoID}',
    ).execute()['items'][0]['statistics']
    URL={
      "maxThumbnailsURL":{
        "url":maxThumbnailsURL,
        "videoId":videoID,
        "statistics":statistics,
      }
    }
    fileName=(f'./json/{i}.json')
    with open(fileName, 'w') as f:
      json.dump(URL, f, indent=2, ensure_ascii=False)
      i+=1
  print(maxThumbnailsURL)
  return maxThumbnailsURL

get_thumbanailsURL()


  


