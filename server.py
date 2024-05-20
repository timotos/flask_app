"""
This module provides functions for creation of flask server.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
This function creates sentiment detector
"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!"
    emotion_scores = {
    'anger': response['anger'],
    'disgust': response['disgust'],
    'fear': response['fear'],
    'joy': response['joy'],
    'sadness': response['sadness']
    }
    dominant_emotion = response['dominant_emotion']
    formatted_string  = (
        f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, "
        f"'disgust': {emotion_scores['disgust']}, "
        f"'fear': {emotion_scores['fear']}, "
        f"'joy': {emotion_scores['joy']} and "
        f"'sadness': {emotion_scores['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return formatted_string

@app.route("/")
def render_index_page():
    """
This function renders background html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    