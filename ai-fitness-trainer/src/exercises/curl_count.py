import cv2
import numpy as np
import time
import requests
from PoseModule import poseDetector
import PoseModule as pm



cap = cv2.VideoCapture("ai-fitness-trainer/assets/videos/Curls.mp4")

detector = pm.poseDetector()
count = 0
count2 = 0
dir = 0
dir2 = 0

# Thêm hàm lưu dữ liệu vào database
def save_to_database(count, count2):
    try:
        # Tính số lần thực hiện thực tế (một chu kỳ đầy đủ)
        left_reps = int(count // 1)  # Làm tròn xuống
        right_reps = int(count2 // 1)

        data = {
            'left_count': left_reps,    # Số lần thực hiện tay trái
            'right_count': right_reps,  # Số lần thực hiện tay phải
            'total_count': left_reps + right_reps  # Tổng số lần thực hiện
        }
        
        # Gửi dữ liệu qua API POST
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://localhost:5000/save_curl_data', 
            json=data,
            headers=headers
        )
        
        # Debug thông tin phản hồi từ server
        print(f"Request data: {data}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
        if response.ok:
            print(f"✅ Data saved successfully: Left={left_reps}, Right={right_reps}, Total={left_reps + right_reps}")
        else:
            print(f"❌ Failed to save data: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error saving data: {str(e)}")

# Thêm hàm kiểm tra tín hiệu dừng
def check_stop_signal():
    try:
        response = requests.get('http://localhost:5000/check_exercise_status')
        if response.ok:
            data = response.json()
            return data.get('stop', False)
    except Exception as e:
        print(f"❌ Error checking stop signal: {str(e)}")
    return False

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    #img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #right arm
        angle1 = detector.findAngle(img, 12, 14, 16)
        #left arm
        angle = detector.findAngle(img, 11, 13, 15)
        per2 = np.interp(angle1, (60, 170), (100, 0))
        per = np.interp(angle, (60, 170), (100, 0))
       #for right arm (60, 170), (0, 100) is the range of motion
        # print(angle, per)
        #check for curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        if per2 == 100:
            if dir2 == 0:
                count2 += 0.5
                dir2 = 1
        if per2 == 0:
            if dir2 == 1:
                count2 += 0.5
                dir2 = 0

        # Draw left arm stats (bên trái màn hình)
        # Progress bar background
        cv2.rectangle(img, (20, 150), (120, 400), (0, 255, 0), 3)
        # Progress bar fill
        bar_height = int(np.interp(per, (0, 100), (400, 150)))
        cv2.rectangle(img, (20, bar_height), (120, 400), (0, 255, 0), cv2.FILLED)
        # Percentage text
        cv2.putText(img, f'left arm', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.putText(img, f'{int(per)}%', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        # Rep counter
        cv2.putText(img, f'Count: {int(count)}', (10, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Draw right arm stats (bên phải màn hình)
        # Progress bar background
        cv2.rectangle(img, (1100, 150), (1200, 400), (0, 255, 0), 3)
        # Progress bar fill
        bar_height2 = int(np.interp(per2, (0, 100), (400, 150)))
        cv2.rectangle(img, (1100, bar_height2), (1200, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'right arm', (1090, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        # Percentage text
        cv2.putText(img, f'{int(per2)}%', (1090, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        # Rep counter
        cv2.putText(img, f'Count: {int(count2)}', (1090, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    # Kiểm tra tín hiệu dừng
    if check_stop_signal():
        save_to_database(count, count2)  # Lưu dữ liệu khi dừng
        break

cv2.imshow("Curl Counter", img)

cap.release()
cv2.destroyAllWindows()