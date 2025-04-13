from flask import Flask, render_template, redirect, url_for, jsonify, request
import subprocess
import sys
import os
import psutil
import mysql.connector
from datetime import datetime

# Đường dẫn đến templates và static
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Biến toàn cục để lưu process đang chạy
current_exercise_process = None

# Thông tin cấu hình cơ sở dữ liệu
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ai_fitness_tracker',
    'port': 3306
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("✅ Database connected.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database connection failed: {err}")
        raise

def launch_script(path):
    """Launch a Python script as a subprocess"""
    global current_exercise_process
    if os.path.exists(path):
        current_exercise_process = subprocess.Popen([sys.executable, path])
        print(f"▶️ Running {path}")
        return True
    else:
        print(f"❌ Script not found: {path}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch/<exercise>')
def launch_exercise(exercise):
    script_map = {
        'curl': 'ai-fitness-trainer/src/exercises/curl_count.py',
        'deadlift': 'ai-fitness-trainer/src/exercises/deadlift_count.py'
    }
    script_path = script_map.get(exercise)
    if script_path and launch_script(script_path):
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Exercise not found'}), 404

@app.route('/stop_exercise', methods=['POST'])
def stop_exercise():
    global current_exercise_process
    try:
        if current_exercise_process:
            # Gửi tín hiệu dừng đến chương trình
            current_exercise_process.terminate()
            current_exercise_process = None
            print("✅ Exercise stopped successfully")
            
            # Lưu dữ liệu vào database (giả sử bạn có API để lưu dữ liệu)
            # Gửi tín hiệu đến bài tập để lưu dữ liệu
            return jsonify({'status': 'success', 'message': 'Exercise stopped and data saved!'})
        else:
            return jsonify({'status': 'error', 'message': 'No exercise running'}), 400
    except Exception as e:
        print(f"❌ Error stopping exercise: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/check_exercise_status', methods=['GET'])
def check_exercise_status():
    # Trả về trạng thái bài tập
    return jsonify({'stop': False})  # Trả về True nếu cần dừng

@app.route('/save_curl_data', methods=['POST'])
def save_curl_data():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 415
            
        data = request.get_json()
        print(f"Received data: {data}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        INSERT INTO bicep_curls (left_count, right_count, total_count)
        VALUES (%s, %s, %s)
        """
        values = (
            data.get('left_count', 0),
            data.get('right_count', 0),
            data.get('total_count', 0)
        )
        
        cursor.execute(query, values)
        conn.commit()
        print("✅ Curl data saved successfully")
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"❌ Error saving curl data: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/save_deadlift_data', methods=['POST'])
def save_deadlift_data():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 415
            
        data = request.get_json()
        print(f"Received data: {data}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        INSERT INTO deadlifts (left_count, right_count, total_count)
        VALUES (%s, %s, %s)
        """
        values = (
            data.get('left_count', 0),
            data.get('right_count', 0),
            data.get('total_count', 0)
        )
        
        cursor.execute(query, values)
        conn.commit()
        print("✅ Deadlift data saved successfully")
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"❌ Error saving deadlift data: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/view_data')
def view_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Get curl data
        cursor.execute("SELECT * FROM bicep_curls ORDER BY date_time DESC LIMIT 5")
        curl_data = cursor.fetchall()
        
        # Get deadlift data
        cursor.execute("SELECT * FROM deadlifts ORDER BY date_time DESC LIMIT 5")
        deadlift_data = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'curl_data': curl_data,
            'deadlift_data': deadlift_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
