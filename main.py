import helper
import cs50
from random import randint
import os

rating = helper.select_rating()
genre = helper.select_genre()
num_votes = helper.select_num_votes()
runtime = helper.select_runtime()

open(f"cleaned_dbs\\movies0.db", "r")
db = cs50.SQL("sqlite:///cleaned_dbs\\movies0.db")

query_count = f"""SELECT count(title) FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN genres ON ratings.movie_id = genres.movie_id
WHERE rating > {rating} and genre like '{genre}' and numVotes > {num_votes} and runtime < {runtime}"""

query_result = db.execute(query_count)
max_num = int(query_result[0]['count(title)'])

random = randint(0, max_num)

query_select_movie = f"""SELECT * FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN genres ON ratings.movie_id = genres.movie_id
WHERE rating > {rating} and genre like '{genre}' and numVotes > {num_votes} and runtime < {runtime}"""
query_result = db.execute(query_select_movie)


print(f"Your movie is: {query_result[random-1]['title']}. It's a movie from {query_result[random-1]['year']} and it "
      f"is {query_result[random-1]['runtime']} minutes long.")

os.system("pause")