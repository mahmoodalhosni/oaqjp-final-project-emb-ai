from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, \
        'joy': {response['joy']} and 'sadness': {response['sadness']}. \
        The dominant emotion is <b>{response['dominant_emotion']}</b>."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)