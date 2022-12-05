import pandas as pd
from flask import Flask, render_template, request
# load the dataset
df = pd.read_csv('conn_attack.csv')

# after doing data explortion and number of algoritem this is the best algoritm we find for detecting outliers/ anomaly
# we set the low and upper bound for the good src values
upper_limit = df['src_bytes'].mean() + 3*df['src_bytes'].std()
lower_limit = df['src_bytes'].mean() - 3*df['src_bytes'].std()

# app for geting data and return answer
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/results',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
        src_bytes = request.form['src']
        dst_bytes = request.form['dst']
        duration = request.form['duration']
        if (float(src_bytes) < upper_limit )and (float(src_bytes) > lower_limit):
            return f"this is detected as a begin file : 0"
        else:
            return f"this is detected as a begin file : 1"
        