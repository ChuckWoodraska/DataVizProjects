import requests
import json

access_token = ""

response = requests.get('https://api.instagram.com/v1/users/self/media/recent?access_token={}'.format(access_token))
print(response.text)
print(len(json.loads(response.text)['data']))
for pic_data in json.loads(response.text)['data']:
    pic_url = pic_data['images']['standard_resolution']['url']
    p = requests.get(pic_url, stream=True)
    print(p.url)
    if p.status_code == 200:
        with open('../data/pics/{}.jpg'.format(pic_data['created_time']), 'wb') as f:
            for chunk in p.iter_content(1024):
                f.write(chunk)
    print(pic_data['caption']['text'])
    print(pic_data['images']['standard_resolution']['url'])