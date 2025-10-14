import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        emotion = json_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key=emotion.get)

        result = {'anger': emotion['anger'],
                'disgust': emotion['disgust'],
                'fear': emotion['fear'],
                'joy': emotion['joy'],
                'sadness': emotion['sadness'],
                'dominant_emotion': dominant_emotion
                }
        return json.dumps(result)
    else:
        return {"error": "Failed to get response from emotion detection service"}