import cs50
import csv

# Creating the db file and the tables that will be used
open(f"movies0.db", "w")
db = cs50.SQL("sqlite:///movies0.db")
db.execute("CREATE TABLE movies (id NUMERIC, title TEXT, is_adult INT, year NUMERIC, runtime NUMERIC, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (movie_id NUMERIC, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))")
db.execute("CREATE TABLE ratings (movie_id NUMERIC, rating NUMERIC, numVotes NUMERIC, FOREIGN KEY(movie_id) REFERENCES movies(id))")

# Opening the created movies0 and separating it in two different tables (movies and genres)
with open("movies0.csv", "r", encoding='utf-8') as titles:
    reader = csv.DictReader(titles)
    id_list = []
    for row in reader:
        id = float(row["movie_id"][2:])
        db.execute("INSERT INTO movies (id, title, is_adult, year, runtime) VALUES(?, ?, ?, ?, ?)", id,
                   row["primaryTitle"], row['isAdult'], row['startYear'], row['runtimeMinutes'])

# Appending movie_ids to create the foreign keys for the rating table
        id_list.append(id)

# Checking for invalid values in the genres column
        if (row['genres'] != '\\N') and (row['genres'] is not None) and (row['genres'] != ''):
            for genre in row["genres"].split(","):
                db.execute("INSERT INTO genres (movie_id, genre) VALUES(?, ?)", id, genre)

# Opening the imdb ratings.tsv and only adding to the table the rows that match the ids in the list
with open("imdb_databases\\ratings.tsv", 'r', encoding='utf-8') as ratingstsv:
    reader = csv.DictReader(ratingstsv, delimiter="\t")

    for row in reader:
        id_rating = float(row["tconst"][2:])

        if id_rating in list:
            rating = float(row["averageRating"])
            numVotes = int(row["numVotes"])
            db.execute("INSERT INTO ratings (movie_id, rating, numVotes) VALUES(?, ?, ?)", id_rating, rating, numVotes)
