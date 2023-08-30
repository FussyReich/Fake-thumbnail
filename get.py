from apiclient.discovery import build
import json
import pandas as pd
import requests

YOUTUBE_API_KEY = 'AIzaSyB_VBZGfozRL1ISMUQU95WIpfOuWI7wXto'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
part='snippet',
q='あもとっと',#検索クエリ
order='viewCount',#視聴回数の多い順
type='video',
maxResults=50,
).execute()

videoID=search_response['items'][0]['id']['videoId'] #print(search_response['items'][0]['id']['videoId'])
statistics=youtube.videos().list(
    #統計情報
    part='statistics',
    id=f'{videoID}',
).execute()['items'][0]['statistics']
#視聴回数=viewCount 高評価数=likeCount お気に入り数=favoriteCount コメント数=commentCount
print(statistics['viewCount']) 
#video_list=[]
def thumbanilsURL():
    for item in search_response.get('items', []):
      if item['id']['kind'] != 'youtube#video':
        continue
    thumbnailsURL=item['snippet']['thumbnails']['high']['url']
    maxThumbnailsURL=thumbnailsURL.replace('hq', 'maxres')
    print(json.dumps(thumbnailsURL, indent=2, ensure_ascii=False))
    return maxThumbnailsURL





