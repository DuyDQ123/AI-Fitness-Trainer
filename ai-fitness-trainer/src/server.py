from flask import Flask, render_template, redirect, url_for, jsonify, request
import subprocess
import sys
import os
import psutil
import mysql.connector
from datetime import datetime
import time
import requests

# Đường dẫn đến templates và static
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Biến toàn cục để lưu process đang chạy
current_exercise_process = None

# Thêm biến toàn cục để kiểm soát tín hiệu dừng
stop_signal = {'stop': False}

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

def check_stop_signal(stop_signal):
    while not stop_signal.value:
        if os.path.exists("stop_signal.txt"):
            print("🛑 Stop signal detected")
            stop_signal.value = True
        time.sleep(0.5)  # Kiểm tra tín hiệu dừng mỗi 0.5 giây

def save_to_database(count, count2):
    try:
        left_reps = int(count.value)
        right_reps = int(count2.value)
        data = {
            'left_count': left_reps,
            'right_count': right_reps,
            'total_count': left_reps + right_reps
        }
        print(f"📊 SAVING DATA: {data}")  # Thêm log nổi bật
        headers = {'Content-Type': 'application/json'}
        print(f"📡 Sending to: http://localhost:5000/save_curl_data")
        response = requests.post('http://localhost:5000/save_curl_data', json=data, headers=headers)
        print(f"📨 Response: {response.status_code} - {response.text}")
        
        if response.ok:
            print(f"✅ DATA SAVED SUCCESSFULLY: {data}")
        else:
            print(f"❌ FAILED TO SAVE: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ ERROR SAVING DATA: {str(e)}")
        import traceback
        traceback.print_exc()  # In chi tiết lỗi

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch/<exercise>')
def launch_exercise(exercise):
    # Xóa file stop_signal.txt nếu tồn tại
    if os.path.exists("stop_signal.txt"):
        os.remove("stop_signal.txt")
        print("🗑️ Removed existing stop_signal.txt")

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
    # Tạo file để báo hiệu dừng
    with open("stop_signal.txt", "w") as f:
        f.write("stop")
    # KHÔNG terminate process ngay, chỉ tạo file và trả về luôn
    # Để process con tự phát hiện và lưu dữ liệu rồi thoát
    return jsonify({'status': 'stop signal sent'})

@app.route('/check_exercise_status')
def check_exercise_status():
    is_running = current_exercise_process and current_exercise_process.poll() is None
    # Thêm stop signal vào response
    return jsonify({
        'isRunning': is_running,
        'stop': stop_signal['stop']
    })

@app.route('/save_curl_data', methods=['POST'])
def save_curl_data():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 415
            
        data = request.get_json()
        print(f"Received data: {data}")  # Log dữ liệu nhận được
        
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
