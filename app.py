from flask import Flask , render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "HEAD"])
def index():
  return render_template('index.html')

@app.route('/index.html', methods=["GET","HEAD"])
def index2():
  return render_template('index.html')

@app.route('/about.html', methods=["GET", "HEAD"])
def about():
  return render_template('about.html')

@app.route('/volunteer.html', methods=["GET","HEAD"])
def volunteer():
  return render_template('volunteer.html')

@app.route('/events.html', methods=["GET","HEAD"])
def events():
  return render_template('events.html')

@app.route('/contact.html', methods=["GET","HEAD"])
def contact():
  return render_template('contact.html')

@app.route('/donate.html', methods=["GET","HEAD"])
def donate():
  return render_template('donate.html')


if __name__ == '__main__':
  app.run()
