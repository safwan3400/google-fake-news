from flask import Flask, abort, jsonify, request, render_template
import json
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def get_delay():
	result=request.form
	query_title = result['title']
	query_author = result['author']
	query_text = result['maintext']
	lol = query_title + " " + query_author + " " + query_text
	link =	'https://factchecktools.googleapis.com/v1alpha1/claims:search?query=' + str(lol) + '&key=AIzaSyAKjLlNdhqE_bjTbFRybC7yXR_7ht0ZspA'
	return webbrowser.open(link, new=2)




if __name__ == '__main__':
    app.run(port=8080, debug=True)
