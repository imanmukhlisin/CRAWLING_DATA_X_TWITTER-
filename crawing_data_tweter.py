import requests
import json
import pandas as pd

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACF60gEAAAAAwx8eZcZMeyjfWy9gDpi32NMyrYs%3D2GXI0gfdQD68MVd1mqyi21bCYhHtybiMbkcARmK4rJ5HgMNK6d'

query = 'liga inggris'

search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {
    'query': query,
    'max_results': 50,  # Bisa 10 sampai 100 (kalau lebih harus pakai pagination)
    'tweet.fields': 'author_id,created_at,public_metrics',
    'expansions': 'author_id',
    'user.fields': 'username',
}

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'User-Agent': 'v2RecentSearchPython'
}

def connect_to_endpoint(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Request gagal: {response.status_code}, {response.text}")
    return response.json()

json_response = connect_to_endpoint(search_url, headers, query_params)

tweets_data = []
for tweet in json_response['data']:
    tweets_data.append({
        'Tweet ID': tweet['id'],
        'Author ID': tweet['author_id'],
        'Tanggal': tweet['created_at'],
        'Isi Tweet': tweet['text'],
        'Retweet Count': tweet['public_metrics']['retweet_count'],
        'Reply Count': tweet['public_metrics']['reply_count'],
        'Like Count': tweet['public_metrics']['like_count'],
        'Quote Count': tweet['public_metrics']['quote_count'],
    })

df = pd.DataFrame(tweets_data)
df.to_csv('kelompok1_22230020.csv', index=False)
print("Sukses! Data disimpan di hasil_crawling_twitter.csv")