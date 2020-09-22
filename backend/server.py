from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

#get poster image links from movie database
@app.route('/movielinks/', methods=['GET', 'POST', "OPTIONS"])
@cross_origin()
def getLinks():
	def load_recommendations():
		item_similarity_df = pd.read_csv("movies_metadata.csv")
		return item_similarity_df

	output = []
	df1 = load_recommendations()
	df2 = df1.set_index("original_title", drop = False)
	movies = request.json["movies"]
	for movie in movies:
		try:
			output.append(str(df2.loc[movie, "poster_path"]))
		except KeyError:
			continue
	return jsonify(output)

#return top 10 movie recommendations given a film
@app.route('/recommendations/', methods=['GET', 'POST', "OPTIONS"])
@cross_origin()
def recommendations():

	def load_recommendations():
		item_similarity_df = pd.read_csv("similarities.csv", index_col=0)
		return item_similarity_df

	def get_similar_movie(movie_name, user_rating):
		similar_score = item_similarity_table[movie_name]
		similar_movies = similar_score.sort_values(ascending=False)
		return similar_movies
	

	item_similarity_table = load_recommendations()
	output = []
	movie_name = request.json["movie_name"]
	user_rating = request.json["user_rating"]
	similar_movies = get_similar_movie(movie_name, user_rating)
	for movie,rating in similar_movies.iteritems():
		output.append(movie)
	output = jsonify(output[1:10])

	return output


if __name__ == '__main__':
    app.run(debug=True)