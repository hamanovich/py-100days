from collections import namedtuple, defaultdict
import urllib
import requests
import os
import pathlib
from csv import DictReader

Movie = namedtuple('Movie', 'title year score')

URL = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'tmp')
MOVIES = os.path.join(DIRECTORY, 'movies.csv')

pathlib.Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(URL, MOVIES)


def main():
    print_header()
    directors = get_movies_by_director(MOVIES)

    output_movies(directors)


def print_header():
    print('MOVIES RATING')
    print('==============')


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
