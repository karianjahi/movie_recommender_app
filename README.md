# movie_recommender_app
This is a movie recommender web app

# Create a Object-Oriented-Programming module
- We create a class called `MovieRecommender`
- The class accepts the following arguments:
  - `method`: string
  - `rated_movies`: rated movie list
  - `ratings`: ratings list
  - `n_movies`: no. of movies to return
- Class methods:
  - `get_recommendations()`: This is where all recommenders are implemented. 
  - All recommenders are imported from `utils.py` which also has a function that converts 2 lists into one dictionary as required by all the methods.

  # Flask
  - We created `application.py` file
  - add 2 functions:
    - hello_world for the landing page
    - recommender for the recommender page
    - We run the application.py file using debug=True and open the link in the browser
    - We modify the 2 returned objects to html
    - We create the templates folder and create the index.hmtl and recommender.html and format them to take a html standard convention
    - We import `render_template`  to allow html rendering and to carry along key-value pairs to the html page.
    - We include Jinja tags `{}` to enclose variables that are carried from the application.py file to the html pages
    - We learn how to loop with jinja tags
      - {% for i in values %}
      - ...
      - {% endfor}
    - We then do away with static user input and create a form with movie titles and ratings in the index.html file
    - We import the `request` method from flask to allow us to make `post` and `get` requests
    - We implement the submission of input from the user and catch the output
    - We then pass the outputs to the recommender python file as expected and make recommendations
    - We observe the recommendations with a message on which method was selected
  - We use `css` styling to beautify the page.