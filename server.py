from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja/')
def tmnt():
  return render_template("tmnt.html", color='home')

@app.route('/ninja/<color>')
def tmnt_color(color):
      
      return render_template("tmnt.html", color=color)
app.run(debug=True) # run our server