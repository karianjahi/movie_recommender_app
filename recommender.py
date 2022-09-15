from utils import (
    list_to_dict,
    get_nmf_movies,
    get_cluster_movies,
    get_popular_movies,
    get_random_movies,
)


class MovieRecommender:
    def __init__(self, method: str, rated_movies: list, ratings: list, n_movies=5):
        self.method = method
        self.rated_movies = rated_movies
        self.ratings = ratings
        self.n_movies = n_movies

    def __repr__(self):
        return f'Recommend movies based on method "{self.method}" '

    def create_message_for_webserver(self):
        general_message = "The following movies have been recommended based on method "

        if self.method == "random":
            return f"{general_message}'{self.method}:'"

        if self.method == "popular":
            return f"{general_message}'{self.method}:'"

        if self.method == "cluster":
            return f"{general_message}'{self.method}:'"

        if self.method == "factor":
            return f"{general_message}'{self.method}:'"

    def get_recommendations(self):
        user_rating_dict = list_to_dict(self.rated_movies, self.ratings)
        if self.method == "random":
            return get_random_movies()[: self.n_movies]
        if self.method == "popular":
            return get_popular_movies(user_rating_dict)[: self.n_movies]
        if self.method == "cluster":
            return get_cluster_movies(user_rating_dict)[: self.n_movies]
        if self.method == "factor":
            return get_nmf_movies(user_rating_dict)[: self.n_movies]


if __name__ == "__main__":
    method = "random"
    rated_movies = ["Chaos", "Flight", "Holiday"]
    ratings = [5, 3, 4]
    inst = MovieRecommender(method=method, rated_movies=rated_movies, ratings=ratings)
    #print(inst.get_recommendations())
    print(inst.create_message_for_webserver())

