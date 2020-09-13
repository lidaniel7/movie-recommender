from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/recommendations/', methods=['GET', 'POST'])
def recommendations():

	def load_recommendations(): 
	    item_similarity_df = pd.read_csv("item_similarity_df.csv",index_col=0)
	    # item_similarity_df = pd.read_csv("similarities_genre.csv", index_col=0)
	    print("item_similarity_df cached in memory")
	    return item_similarity_df
	item_similarity_table = load_recommendations()

	def get_similar_movie(movie_name, user_rating):
		similar_score = item_similarity_table[movie_name]
		similar_movies = similar_score.sort_values(ascending=False)
		return similar_movies
	output = []
	# for movie_id, movie in request.json():
	# 	similar_movies = similar_movies.append(get_similar_movie(movie["title"], movie["rating"]))
	movie_name = request.json["movie_name"]
	user_rating = request.json["user_rating"]
	similar_movies = get_similar_movie(movie_name, user_rating)
	for movie,rating in similar_movies.iteritems():
		output.append(movie)
	output = jsonify(output[1:50])
	output.headers.add("Access-Control-Allow-Origin", "*")

	return output

	# output = []
	# for similar_movie in get_similar_movie(movie.name):
	# 	output.append(similar_movie)
	# return jsonify(output)


	# if (request.method == 'POST'):
	# 	some_json = request.get_json()
	# 	# return jsonify({'you sent': some_json})
	# 	return "Hello"
	# else:
	# 	output = []
	# 	for similar_movie in get_similar_movie(movie):
	# 		output.append(similar_movie)
	# 	# for movie in item_similarity_table:
	# 	# 	output.append(movie)
	# 	return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)