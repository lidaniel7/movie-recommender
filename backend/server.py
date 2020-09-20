from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# def load_ids():
# 	idmap = pd.read_csv("movies_metadata.csv")
# 	return idmap

# idmap = load_ids()

# @app.route('/recommendations/links/<str>', methods=['GET', 'POST'])
# def getpaths():
# 	request.json["movie_name"]

@app.route('/movielinks/', methods=['GET', 'POST', "OPTIONS"])
@cross_origin()
def getLinks():
	def load_recommendations():
		item_similarity_df = pd.read_csv("movies_metadata.csv")
		# item_similarity_df = pd.read_csv("similarities_genre.csv", index_col=0)
		# item_similarity_df = pd.read_csv("similarities3.csv", index_col=0)
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
	# for original_title in metadata_table.iteritems():
	# 	output.append(original_title

	return jsonify(output)


@app.route('/recommendations/', methods=['GET', 'POST', "OPTIONS"])
@cross_origin()
def recommendations():

	# if request.method == "OPTIONS":
	# 	response = make_response()
	# 	response.headers["Access-Control-Allow-Origin"] = "*"
	# 	print("options called")
	# 	return response

	def load_recommendations():
		# item_similarity_df = pd.read_csv("item_similarity_df.csv", index_col=0)
		# item_similarity_df = pd.read_csv("similarities_genre.csv", index_col=0)
		item_similarity_df = pd.read_csv("similarities3.csv", index_col=0)
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
	# output.headers["Access-Control-Allow-Origin"] = "*"

	return output


	# for movie_id, movie in request.json():
	# 	similar_movies = similar_movies.append(get_similar_movie(movie["title"], movie["rating"]))

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