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
    start = request.args.get('start')
    end = request.args.get('end')
    dist = request.args.get('d')
    trans = request.args.get('t')
    stops = request.args.get('st')
    # call get_heuristic with different parameters (if a param is true we use that heuristic)
    # param 1: minimize distance traveled
    # param 2: minimize transfers
    # param 3: minimize stops
    calc = calculate(start , end, dist, trans, stops)
    print(calc['path'])
    print(calc["distance"])
    print(calc["transfers"])
    print(calc["percent"])
    result = {'path' : calc["path"], 'distance' : calc["distance"], 'transfers' : calc['transfers'], 'added' : calc['added'], 'percent' : calc["percent"]}
    return jsonify(result)

@app.route('/get_name')
def get_name():
    curr = request.args.get('curr')
    out =   get_station_name(curr)
    result = {'curr': out}
    return jsonify(result)

@app.route('/all_locations')
def locations():
    out =   all_locations()
    result = {'locations': out}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

# path = generate_path("A01", "C01", get_successor, get_distance_to_goal)
# print(len(path))
# print(path)