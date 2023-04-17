from flask import Flask, render_template
import settings
import sqlite3


app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie')
def movie():
    data_list = []
    conn = sqlite3.connect('Study\crawler and data_visualization\DouBan\douban_crawl\douban_top250.db')
    cur = conn.cursor()
    sql = '''
        select * from movie250
    '''
    for row in cur.execute(sql):
        data_list.append(row)
    cur.close()
    conn.close()
    return render_template('movie.html', movies = data_list)


@app.route('/score')
def score():
    x_data = []
    y_data = []
    conn = sqlite3.connect('Study\crawler and data_visualization\DouBan\douban_crawl\douban_top250.db')
    cur = conn.cursor()
    sql = '''
        select score, count(score) from movie250 group by score order by count(score) DESC
    '''
    for row in cur.execute(sql):
        x_data.append(str(row[0]))
        y_data.append(row[1])
    cur.close()
    conn.close()
    return render_template('score.html', x_data = x_data, y_data = y_data)


@app.route('/word')
def word():
    return render_template('word.html')


if __name__ == '__main__':
    app.run()