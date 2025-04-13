from flask import Flask, render_template, redirect, url_for, jsonify
import subprocess
import sys
import os
import psutil

# Update template and static folder paths
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Biến toàn cục để lưu process
current_exercise_process = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch/<exercise>')
def launch_exercise(exercise):
    global current_exercise_process
    if exercise == 'curl':
        current_exercise_process = subprocess.Popen([sys.executable, 'ai-fitness-trainer/src/exercises/curl_count.py'])
    elif exercise == 'deadlift':
        current_exercise_process = subprocess.Popen([sys.executable, 'ai-fitness-trainer/src/exercises/deadlift_count.py'])
    return jsonify({'status': 'success'})

@app.route('/stop_exercise', methods=['POST'])
def stop_exercise():
    global current_exercise_process
    if current_exercise_process:
        process = psutil.Process(current_exercise_process.pid)
        for child in process.children(recursive=True):
            child.terminate()
        process.terminate()
        current_exercise_process = None
    return jsonify({'status': 'success'})

@app.route('/check_exercise_status')
def check_exercise_status():
    global current_exercise_process
    is_running = False
    if current_exercise_process:
        is_running = current_exercise_process.poll() is None
    return jsonify({'isRunning': is_running})

if __name__ == '__main__':
    app.run(debug=True)