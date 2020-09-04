import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csv_file:
            movie_file_reader = csv.DictReader(csv_file)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                description = row["Description"]
                runtime_minutes = row["Runtime (Minutes)"]
                director = Director(row["Director"])
                genres = set([Genre(genre) for genre in row["Genre"].split(',')])
                actors = set([Actor(name) for name in row["Actors"].split(',')])

                movie = Movie(title, release_year)
                movie.description = description
                movie.runtime_minutes = runtime_minutes
                movie.director = director
                movie.genre = genres
                movie.actor = actors

                self.__dataset_of_directors.add(director)
                self.__dataset_of_genres |= genres
                self.__dataset_of_actors |= actors
                self.__dataset_of_movies.append(movie)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres