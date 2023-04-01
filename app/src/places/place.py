class Place():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_location(self):
        return f"{self.latitude}, {self.longitude}"

    