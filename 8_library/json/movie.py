import json

# from Dictionary to String (structure json)
movie_transformer = {"title": "Transformers 1", "studio": "marvel", "duration": "120"}
movies_json = json.dumps(movie_transformer) # string

print(movie_transformer)
print(movie_transformer["title"])

# from String (structure json) to Dictionary
movie = json.loads(movies_json)
print(movie)
print(movie["duration"])
