from flask import Flask, render_template, url_for
import game_of_life as gl

app = Flask(__name__)

@app.route('/')
def index():
    gl.GameOfLife(25,25)
    return render_template('index.html')

@app.route('/live')
def live():
    life = gl.GameOfLife(25, 25)
    life.form_new_generation()
    n = life.world
    return render_template('live.html', new_life=n)

if __name__ == '__main__':
    app.run(debug=True)