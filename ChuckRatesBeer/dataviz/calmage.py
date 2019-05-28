import calendar
import json
from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)
YEAR = 2018

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/search")
def search():
    #contact untappd
    # make table
    return jsonify()

@app.route("/predict")
def predict():
    #load model

    #fit

    return jsonify()

@app.route("/calendar")
def calendar_render():
    return render_template(
        "calmage.html"
    )

@app.route("/calendar/<int:month_id>")
def calendar_month_render(month_id):
    offset = datetime(YEAR, month_id, 1).timetuple().tm_yday
    lst = create_day_image_list(month_id, offset - 1)
    return render_template(
        "calmage.html", days=lst, month=calendar.month_name[month_id]
    )


def create_day_image_list(month, offset=0):
    c = calendar.Calendar()
    c.setfirstweekday(calendar.SUNDAY)
    with open("../data/crb_by_day.json", "r") as f:
        json_data = json.loads(f.read())
    lst = [
        {
            "img_src": "images/pics_raw/Day{}.jpg".format(x + offset),
            "index": (y + 2) % 8,
            "alt_text": "{}\n{} - {}".format(datetime(YEAR, month, x).strftime("%B %d, %Y"), json_data['Day{}'.format(x + offset)]['brewery_name'], json_data['Day{}'.format(x + offset)]['beer_name']),
            "untappd_url": json_data['Day{}'.format(x + offset)]['untappd_url']
        }
        for x, y in c.itermonthdays2(YEAR, month)
        if x
    ]
    return lst


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
