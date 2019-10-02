# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE
    
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"lat: {self.lat} lon: {self.lon}"

c1 = LatLon(10, -1232)
print(c1)
# print(c1.lat, c1.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE

class Waypoint:
    def __init__(self, name, LatLon):
        self.name = name
        self.LatLon = LatLon
    def __str__(self):
        return f"name: {self.name} lat: {self.LatLon.lat} lon: {self.LatLon.lon}"

w = Waypoint("ocean", c1)
print(w)
# print(w.name, w.LatLon.lat, w.LatLon.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE
class Geocache:
    def __init__(self, Waypoint, difficulty):
        self.waypoint = Waypoint
        self.difficulty = difficulty
    def __str__(self):
        return f"name: {self.waypoint.name} with difficulty: {self.difficulty} at lat: {self.waypoint.LatLon.lat} lon: {self.waypoint.LatLon.lon}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE

g = Geocache(w, 7)
# print(g.waypoint.name, g.difficulty)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE

# print(g)

# Print it--also make this print more nicely
# print(geocache)
