from apiclient.discovery import build
import json
import pandas as pd
import requests

YOUTUBE_API_KEY = 'AIzaSyB_VBZGfozRL1ISMUQU95WIpfOuWI7wXto'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
part='snippet',
q='桃太郎オフィス',#検索クエリ
order='viewCount',#視聴回数の多い順
type='video',
maxResults=50,
).execute()

#print(json.dumps(search_response['items'][0]['id']['videoId'],indent=2,ensure_ascii=False))
#videoID=search_response['items'][0]['id']['videoId']
statistics=youtube.videos().list(
    #統計情報
    part='statistics',
    id='BUQU5BndtpQ',
).execute()['items'][0]['statistics']
#print(json.dumps(statistics['items'][0]['statistics'], indent=2, ensure_ascii=False))
#video_list=[]
#for item in search_response.get('items', []):
#    if item['id']['kind'] != 'youtube#video':
#        continue
#    print('*' * 10)
#    print(json.dumps(item, indent=2, ensure_ascii=False))
#    print('*' * 10)

