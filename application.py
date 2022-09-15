from flask import Flask
from flask import render_template
from flask import request
from utils import MOVIE_TITLES


from recommender import MovieRecommender
# Tell the flask app that this is the source file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("landing_page.html", movies=MOVIE_TITLES)

@app.route("/recommender")
def recommender():
    method = request.args.getlist("method")[0]
    rated_movies = request.args.getlist("title")
    ratings = request.args.getlist("rating")
    inst = MovieRecommender(method=method, rated_movies=rated_movies, ratings=ratings)
    recs = inst.get_recommendations()
    message = inst.create_message_for_webserver()
    return render_template("recommender.html", recs=recs, message=message)

if __name__ == "__main__":
    app.run(debug=True, port=5000)