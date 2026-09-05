'''
Flask Help (this is my first time using Flask)
Routes are URL paths mapped to Python functions
When someone visits that URL, Flask runs the function and sends back whatever it returns

Templates are HTML files with placeholders that Flask fills in with Python data
Templates live in a folder templates/ which Flask looks for automatically

render_template() is how you return an HTML page instead of raw text / JSON
It finds the file in templates/ and injects your data into it

'''
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# load movies, similarity
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
indices = pd.Series(movies.index, index = movies["title"]).drop_duplicates()

# create recommendation function
def recommend(title, num_recommendations = 10):
    if title not in indices:
        return None # returning None signals 'not found' back to the route
    index = indices[title]
    sim_scores = sorted(list(enumerate(similarity[index])), key = lambda x : x[1], reverse = True)
    sim_scores = sim_scores[1:num_recommendations + 1] # skip index 0, which is just the movie itself
    movie_indices = [i[0] for i in sim_scores]

    results = movies.iloc[movie_indices][["title", "vote_average"]].to_dict(orient = "records")
    return results # returns a list of dics so the template has structured data to loop over

@app.route("/")
def home():
    titles = sorted(movies["title"].tolist())
    return render_template("index.html", titles=titles)

@app.route("/recommend", methods = ["POST"])
def show_recommendations():
    selected_title = request.form.get("title")
    results = recommend(selected_title)
    if results is None:
        return render_template("recommend.html", errors = f"'{selected_title}' is not a valid title",
                               movie = selected_title)
    return render_template("recommend.html", movie = selected_title, recommendations = results)

if __name__ == "__main__":
    app.run(debug = True)