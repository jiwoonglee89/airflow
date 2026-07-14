import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'eedd032b014b46192ed6a9cd1de8dfce'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'bukTN1gf53q57fEKRLau74O_49QVjUdVw2M37ZSv93Utdqyok28DSQAAAAQKDQ0hAAABnyNGy56m1x-HnlkNwQ'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
