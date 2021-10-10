from flask import Flask, request, jsonify
from metro_news.db.news import NewsManager

app = Flask(__name__)


@app.get("/metro/news")
def root():
    day = request.args.get('day', default=0, type=int)
    month = request.args.get('month', default=0, type=int)
    year = request.args.get('year', default=0, type=int)
    days = day + month * 30 + year * 365
    returned = NewsManager().get_period_ago(period=days)
    return jsonify(returned)


if __name__ == "__main__":
    app.run()
