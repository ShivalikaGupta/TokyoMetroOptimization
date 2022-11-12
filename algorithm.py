from library import *
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
app = Flask(__name__)

#rendering the HTML page which has the button
@app.route("/")
def index():
    return render_template('index.html');

@app.route("/results")
def results():
    return render_template('visualize.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

path = generate_path("A01", "C01", get_successor, get_distance_to_goal)
print(len(path))
print(path)