''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This function takes the input from the user and translates it 
        from the emotion detector module to return an answer to the user
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    emotion_list = emotion_detector(text_to_analyze)

    if emotion_list['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': \
    {emotion_list['anger']}, 'disgust': {emotion_list['disgust']}, 'fear': \
    {emotion_list['fear']}, 'joy': {emotion_list['joy']}, and 'sadness': \
    {emotion_list['sadness']}. The dominant emotion is {emotion_list['dominant_emotion']}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
