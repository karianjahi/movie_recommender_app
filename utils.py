import random
import pandas as pd

MOVIES = pd.read_csv("data/movies.csv")
MOVIE_TITLES = list(MOVIES["title"])


def list_to_dict(keys: list, values: list):
    adict = {}
    for key, value in zip(keys, values):
        adict[key] = value
    return adict


def get_random_movies():
    movie_titles = list(MOVIES["title"])
    random.shuffle(movie_titles)
    return movie_titles


def get_popular_movies(user_rating_dict):
    ...
    return [f"popular movie {i}" for i in range(1, 100)]


def get_cluster_movies(user_rating_dict):
    ...
    return [f"cluster movie {i}" for i in range(1, 100)]


def get_nmf_movies(user_rating_dict):
    ...
    return [f"nmf movie {i}" for i in range(1, 100)]


if __name__ == "__main__":
    rated_movies = ["Chaos", "Flight", "Holiday"]
    ratings = [5, 3, 4]
    user_rating_dict = list_to_dict(rated_movies, ratings)
    print(get_nmf_movies(user_rating_dict))
