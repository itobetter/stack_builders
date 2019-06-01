from flask import Flask, jsonify, render_template, request
from models.plate_predictor import PlatePredictor
app = Flask(__name__)

@app.route('/get_info')
def add_numbers():
    # 'abc-123', '2019/05/30 21:10:10'
    plate = request.args.get('plate', 0, type=str)
    date= request.args.get('date', 0, type=str)
    if not plate or not date:
        jsonify(info='')
    info = PlatePredictor(plate,date).get_info()
    return jsonify(info=info)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()