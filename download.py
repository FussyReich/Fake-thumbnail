import search as s
import requests
import time

def download():
  nowTime=time.time()
  i=1
  while True:
    if time.time() - nowTime > 5:
      break  
    URL=s.get_thumbanailsURL()
    print(f'{URL}')
    response=requests.get(URL)
    #画像をファイルに保存
    with open(f'./Thumbnails/{i}.png', 'wb') as f:
      f.write(response.content)
    i+=1

download()