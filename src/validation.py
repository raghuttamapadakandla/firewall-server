import os
import requests

def callGPT(request):
    api_key = os.environ['OPENAI_KEY']
    query = request.headers[
        'X-Forwarded-For'] + 'On a scale of 1 to 10, rate how malicious this data packet seems. With 1 being the least likely and 10 being the most likely.'
    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers={
                                 "Authorization": "Bearer " + api_key,
                                 "Content-Type": "application/json"
                             },
                             json={
                                 "model": "gpt-3.5-turbo",
                                 "messages": [{
                                     "role": "user",
                                     "content": query
                                 }],
                                 "temperature": 0.5
                             })
    return (response.json())
