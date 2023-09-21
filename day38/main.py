import requests
 
headers = {
    'x-app-id': 'cb4933ea',
    'x-app-key': '6111cd5919074098e0a3015e104f94a1',
    'Content-Type': 'application/json'
}
 
text_input = "Tôi đã chạy 30 phút và tập thể dục 100 đập bo"

 
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
payload = {
    'query': text_input,
    'gender': 'male',
    'weight_kg': 70,
    'height_cm': 180,
    'age': 30
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

 
exercises = data['exercises']
for exercise in exercises:
    print('Bài tập:', exercise['name'])
    print('Thời gian:', exercise['duration_min'], 'phút')
    print('Lượng calo đốt cháy:', exercise['nf_calories'], 'calo')
    print('')

