import os
import subprocess
from flask import Flask, render_template

#with open("files/somefile", "r") as f:
#    content = f.read()

content = subprocess.call('scripts/get-envTemp.py',shell=True)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/beer')
def beer():
  return render_template("readfile.html", content=content)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)
