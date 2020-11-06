def select_genre():
    """asks the user for a genre from the list of genres. also shows what genres are available"""
    genre_list = ['drama', 'mystery', 'romance', 'comedy', 'musical', 'biography', 'fantasy', 'war', 'action',
                  'adventure', 'family', 'crime', 'thriller', 'western', 'history', 'horror', 'film-noir', 'sci-fi',
                  'sport', 'animation', 'music', 'adult', '']
    while True:
        genre = input("Genre: ")
        genre = genre.lower()
        if (genre == '') or (genre in genre_list):
            genre = f'%{genre}%'
            return genre
        elif genre == 'list':
            print(genre_list)
        else:
            print("This isn't a valid genre! Choose a valid genre from the list (type 'list') or nothing if you don't "
                  "want to choose a genre.")


def select_rating():
    """asks the user for a minimum rating between 0 and 10"""
    while True:
        try:
            rating = input("Minimum rating: ")

            if rating == '':
                return 0

            rating = float(rating)

            if 10.0 >= rating >= 0.0:
                return rating
            else:
                print("Choose a rating between 0 and 10.")

        except ValueError:
            print("This isn't a number!")


def select_num_votes():
    """asks the user for a minimum rating between 0 and 10"""
    while True:
        try:
            num_votes = input("Minimum number of votes (0 to 200): ")

            if num_votes == '':
                return 0

            num_votes = float(num_votes)

            if 200 >= num_votes >= 0.0:
                return num_votes
            else:
                print("Choose a minimum number of votes between 0 and 200.")

        except ValueError:
            print("This isn't a number!")


def select_runtime():
    """asks the user for the maximum runtime"""
    while True:
        try:
            runtime = input("Max movie length (90 or more minutes): ")

            if runtime == '':
                return 100000

            runtime = float(runtime)

            if 10000 >= runtime >= 90:
                return runtime
            else:
                print("Choose a maximum movie length equals or above 90.")

        except ValueError:
            print("This isn't a number!")
