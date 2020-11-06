import csv

# Opening a title_basics.tsv
with open("imdb_databases\\title_basics.tsv", 'r', encoding='utf-8') as titles_handler:
    reader = csv.DictReader(titles_handler, delimiter="\t")
    tb_keys = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes',
            'genres']

# Creating movies0.csv with a new header
        with open("movies0.csv", 'w', encoding='utf-8') as movies:
            writer = csv.writer(movies)
            writer.writerow(['movie_id', 'primaryTitle', 'isAdult', 'startYear', 'runtimeMinutes', 'genres'])

            for row in reader:
                if (row['titleType'] == "movie" or row['titleType'] == "tvMovie") and (row["startYear"] != "\\N") \
                    and (int(row["startYear"]) > 1950) and (row['runtimeMinutes'] != "\\N"):

                    writer.writerow([row["tconst"], row["primaryTitle"], row['isAdult'], int(row["startYear"]),
                                    int(row['runtimeMinutes']), row["genres"]])
