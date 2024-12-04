movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

#print total movies count

print(len(movies))


#print movie titles

movie_title=[m.get("title")for m in movies]

print(movie_title)


#print malayalam movies

malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]

print(malayalam_movies)


#print movie with maximum_duration

max_movie=max(movies,key=lambda m:m.get("run_time"))

print(max_movie)


#print movies with minimum duration

min_movie=min(movies,key=lambda m:m.get("run_time"))

print(min_movie)


#print most runtime movies

most_runtime_movie=max(movies,key=lambda m:m.get("run_time"))

most_runtime_movie_run_time=most_runtime_movie.get("run_time")

print(most_runtime_movie_run_time)

most_runtime_movies=[m.get("title") for m in movies if m.get("run_time")==most_runtime_movie_run_time]

print(most_runtime_movies)


#print malayalam movies count

malayalam_movies_count=[m for m in movies if m.get("language")=="malayalam"]

print(len(malayalam_movies_count))

#print maximum languages

all_movies=[m.get("language") for m in movies]

print(all_movies)

movie_count={m:all_movies.count(m) for m in all_movies}

print(movie_count)















