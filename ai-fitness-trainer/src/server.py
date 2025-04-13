from flask import Flask, render_template, redirect, url_for
import subprocess
import sys
import os

# Update template and static folder paths
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch/<exercise>')
def launch_exercise(exercise):
    if exercise == 'curl':
        subprocess.Popen([sys.executable, 'ai-fitness-trainer/src/exercises/curl_count.py'])
    elif exercise == 'deadlift':
        subprocess.Popen([sys.executable, 'ai-fitness-trainer/src/exercises/deadlift_count.py'])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)