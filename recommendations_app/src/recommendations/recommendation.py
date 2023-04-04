from src.recommendations.services.chatgpt_service import query_recommendations

class Recommendation():

    def __init__(self):
        pass

    def get_chatgpt_recommendation(self):
        return query_recommendations()

    