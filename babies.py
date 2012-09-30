from flask import Flask, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap
import os
from flask import render_template
import search
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST'

	return render_template('index.html')

if __name__ == '__main__':
		app.run(debug=True)
