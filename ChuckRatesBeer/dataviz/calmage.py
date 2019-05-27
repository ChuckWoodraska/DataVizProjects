import calendar
from datetime import datetime

from flask import Flask, render_template
app = Flask(__name__)
YEAR = 2018

@app.route("/<int:month_id>")
def calendar_render(month_id):
    offset = datetime(YEAR, month_id, 1).timetuple().tm_yday
    lst = create_day_image_list(month_id, offset-1)
    return render_template('calmage.html', days=lst, month=calendar.month_name[month_id])



def create_day_image_list(month, offset=0):
    c = calendar.Calendar()
    c.setfirstweekday(calendar.SUNDAY)
    lst = [{"img_src": "images/pics_raw/Day{}.jpg".format(x+offset), "index": (y + 2) % 8, "alt_text": datetime(YEAR, month, x).strftime("%B %d, %Y")} for x, y in c.itermonthdays2(YEAR, month) if x]
    return lst



if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)

# Add beer name and brewery to alt text
# Add untappd checkin link
# change chuckratesbeer json to dict with day of year as key