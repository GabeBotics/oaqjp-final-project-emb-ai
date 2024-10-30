import requests, json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    # Format and find the emotion list in the returning json
    formatted_response = json.loads(response.text)

    emotion_arr = formatted_response['emotionPredictions']

    emotion_list = emotion_arr[0]['emotion']

    # Find the highest scoring emotion by looping
    highest_score = 0
    highest_emotion = ''

    for emotion, score in emotion_list.items():
        if score > highest_score:
            highest_score = score
            highest_emotion = emotion

    # Return the highest emotion and highest score
    return {"emotion": highest_emotion, "score": highest_score}