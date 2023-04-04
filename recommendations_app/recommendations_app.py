from flask import Flask
from src.recommendations.recommendation import Recommendation

app = Flask(__name__)

@app.route('/')
def get_recommendation():
    recommendation = Recommendation()
    return recommendation.get_chatgpt_recommendation()