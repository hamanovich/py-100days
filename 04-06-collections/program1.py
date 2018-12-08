from collections import namedtuple, defaultdict
from urllib.request import urlretrieve
import requests
from csv import DictReader
from os import path, mkdir

Movie = namedtuple('Movie', 'title year score')

movies_csv = 'movies.csv'
movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'


def main():
    print_header()
    full_path = get_full_path()
    add_movies_to_local_file(full_path)
    directors = get_movies_by_director(full_path)

    output_movies(directors)


def print_header():
    print('MOVIES RATING')
    print('==============')


def add_movies_to_local_file(full_path):
    if not path.exists(full_path):
        with open(movies_csv, 'w') as fout:
            urlretrieve(movie_data, full_path)


def get_full_path():
    return path.join(path.dirname(__file__), movies_csv)


def get_movies_by_director(data):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def output_movies(directors):
    director = 'EMPTY'

    while director != 'x' and director:
        director = input('Type director (or [x] to exit): ')
        print()

        if not director or director == 'x':
            break
        elif directors[director]:
            for movie in sorted(directors[director], key=lambda movie: -movie.score):
                print(f'Title: {movie.title}')
                print(f'Score: {movie.score}')
                print(f'Year: {movie.year}')
                print()
        else:
            print(f'We didn\'t find director `{director}`. Try again')

    print('Goodbye!')


if __name__ == "__main__":
    main()
