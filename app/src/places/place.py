from src.places.services.foursquare_places_service import query_place
class Place():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_location(self):
        return query_place(self.latitude, self.longitude)

    