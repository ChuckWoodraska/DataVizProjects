import calendar

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    c = calendar.Calendar()
    c.setfirstweekday(calendar.SUNDAY)
    print(c.itermonthdays2(2019, 1))
    lst = [(y + 2) % 8 for x, y in c.itermonthdays2(2019, 1) if x]
    return render_template('calmage.html', jan_days=lst)