from flask import Flask, request
import os
from flask import render_template
import search

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def print_form():
    name = request.args.get('name')
#        print name
#       print render_template('index.html',result = request.args['name'])
#        return render_template('index.html',result = request.args['name'])
    if name == "Chris Wiggins":
        spermcount = 300
    else:
        spermcount = search.searching(name)
    return render_template('result.html', count = spermcount)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
