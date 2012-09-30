from flask import Flask, request, redirect, url_for
import os
from flask import render_template
import search
app = Flask(__name__)

@app.route('/')
def index():
	spermcount =  search.searching("Justin Bieber")
	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
