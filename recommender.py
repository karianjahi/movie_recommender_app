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
        if self.method in {"random", "popular", "cluster", "factor"}:
            return f"The following movies have been recommended based on method '{self.method}:'"
    
    def get_recommendations(self):
        user_rating_dict = list_to_dict(self.rated_movies, self.ratings)
        method_function_map = {
            "random": lambda: get_random_movies(),
            "popular": lambda: get_popular_movies(user_rating_dict),
            "cluster": lambda: get_cluster_movies(user_rating_dict),
            "factor": lambda: get_nmf_movies(user_rating_dict),
        }
        if self.method in method_function_map:
            return method_function_map[self.method]()[: self.n_movies]


if __name__ == "__main__":
    method = "random"
    rated_movies = ["Chaos", "Flight", "Holiday"]
    ratings = [5, 3, 4]
    inst = MovieRecommender(method=method, rated_movies=rated_movies, ratings=ratings)
    #print(inst.get_recommendations())
    print(inst.create_message_for_webserver())

