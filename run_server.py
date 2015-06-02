from flask import Flask
from flask import render_template
from flask import request, Response, jsonify
from operator import itemgetter
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/HighVar/<word_name>", methods=['GET'])
def high_var(word_name):
    print "We are in the correct route w/ word " + word_name 
    words = [5, 2, 2, 1, 4]
    tel = {'jack': 4098, 'sape': 4139}
    #return jsonify(tel)
    return json.dumps(tel)

if __name__ == '__main__':
    app.run()
