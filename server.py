"""
Web deployment of the application using Flask
"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """This function is used to render index page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=['GET'])
def emotion_detection():
    """This function is used to detect the emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = json.loads(emotion_detector(text_to_analyze))
    if response['dominant_emotion'] is not None:
        return f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} \
        and 'sadness': {response['sadness']}. \
        The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return "<b>Invalid text! Please try again!</b>"

if __name__ == "__main__":
    app.run(host="localhost", port="5000")
