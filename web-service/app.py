from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    name = "Shubhendu shukla"
    roll_number = "2022BCD0054"
    bio = "Hey i am from batch 3 "
    container_id = os.uname()[1]
    current_time = datetime.datetime.now()
    return render_template('index.html', name=name, roll_number=roll_number, bio=bio, container_id=container_id, current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)