import requests
import json

def emotion_detector(text_to_analyse):  
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 
    # Return the response text from the API
    
    formatted_response = json.loads(response.text)
    
    #extracting the emotions
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Store values in a dictionary
        values_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Get the highest value and grab its key property
        highest_key = max(values_dict, key=values_dict.get)

    elif response.status_code > 300:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        highest_key = None
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': highest_key
    } 