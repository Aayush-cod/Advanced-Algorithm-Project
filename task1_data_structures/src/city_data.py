class CityData:
    def __init__(self, name, latitude, longitude, population, distance=0.0):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        self.distance = distance

    def __repr__(self):
        return f"City({self.name}, pop={self.population}, dist={self.distance})"
