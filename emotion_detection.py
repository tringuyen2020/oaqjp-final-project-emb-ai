import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        result = {'anger': json_data['emotionPredictions'][0]['emotion']['anger'],
                'disgust': json_data['emotionPredictions'][0]['emotion']['disgust'],
                'fear': json_data['emotionPredictions'][0]['emotion']['fear'],
                'joy': json_data['emotionPredictions'][0]['emotion']['joy'],
                'sadness': json_data['emotionPredictions'][0]['emotion']['sadness'],
                'dominant_emotion': json_data['producerId']['name']
                }
        return json.dumps(result)
    else:
        return {"error": "Failed to get response from emotion detection service"}