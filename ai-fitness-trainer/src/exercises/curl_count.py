import cv2
import numpy as np
import os
import time
import multiprocessing
import requests
from PoseModule import poseDetector

# Biến toàn cục để chia sẻ dữ liệu giữa các process
stop_signal = multiprocessing.Value('b', False)  # Biến boolean để kiểm tra tín hiệu dừng
count = multiprocessing.Value('d', 0.0)         # Số lần thực hiện tay trái (float)
count2 = multiprocessing.Value('d', 0.0)        # Số lần thực hiện tay phải (float)

# Hàm xử lý video
def process_video(stop_signal, count, count2):
    cap = cv2.VideoCapture("ai-fitness-trainer/assets/videos/Curls.mp4")
    # cap = cv2.VideoCapture(0) # Uncomment this line to use webcam
    detector = poseDetector()
    frame_count = 0
    frame_skip = 2
    dir = 0
    dir2 = 0

    while not stop_signal.value:
        success, img = cap.read()
        if not success:
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue  # Bỏ qua frame này

        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            # Xử lý pose detection và đếm số lần thực hiện
            angle1 = detector.findAngle(img, 12, 14, 16)  # Tay phải
            angle = detector.findAngle(img, 11, 13, 15)   # Tay trái
            per2 = np.interp(angle1, (60, 150), (100, 0))
            per = np.interp(angle, (60, 150), (100, 0))
            if  angle > 170 or  angle1 > 170:
                cv2.putText(
                    img,
                    "Wrong form! Keep your back straight!",
                    (300, 680),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    3
                )
            if per == 100 and dir == 0:
                with count.get_lock():
                    count.value += 0.5
                dir = 1
            if per == 0 and dir == 1:
                with count.get_lock():
                    count.value += 0.5
                dir = 0
            if per2 == 100 and dir2 == 0:
                with count2.get_lock():
                    count2.value += 0.5
                dir2 = 1
            if per2 == 0 and dir2 == 1:
                with count2.get_lock():
                    count2.value += 0.5
                dir2 = 0

            # Vẽ thanh tiến trình và hiển thị số lần thực hiện
            # Thanh tiến trình cho tay trái (bên trái màn hình)
            cv2.rectangle(img, (50, 100), (100, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (50, int(400 - (per * 3))), (100, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (50, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Thanh tiến trình cho tay phải (bên phải màn hình)
            cv2.rectangle(img, (1180, 100), (1230, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (1180, int(400 - (per2 * 3))), (1230, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per2)}%', (1180, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Hiển thị số lần thực hiện
            cv2.putText(img, f'Left Reps: {int(count.value)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.putText(img, f'Right Reps: {int(count2.value)}', (1000, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Curl Counter", img)

        # Kiểm tra stop_signal trước khi kết thúc mỗi frame
        if stop_signal.value:
            print("🛑 Stop signal detected in video process, saving data...")
            save_to_database(count, count2)
            break

        # Thoát bằng phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_signal.value = True
            break

    cap.release()
    cv2.destroyAllWindows()

# Hàm kiểm tra tín hiệu dừng
def check_stop_signal(stop_signal):
    while not stop_signal.value:
        if os.path.exists("stop_signal.txt"):
            print("🛑 Stop signal detected")
            stop_signal.value = True
        time.sleep(0.5)  # Kiểm tra tín hiệu dừng mỗi 0.5 giây

# Hàm lưu dữ liệu vào database
def save_to_database(count, count2):
    try:
        left_reps = int(count.value)
        right_reps = int(count2.value)
        data = {
            'left_count': left_reps,
            'right_count': right_reps,
            'total_count': left_reps + right_reps
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:5000/save_curl_data', json=data, headers=headers)
        if response.ok:
            print(f"✅ Data saved successfully: {data}")
        else:
            print(f"❌ Failed to save data: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error saving data: {str(e)}")

# Chạy các process song song
if __name__ == "__main__":
    stop_signal.value = False  # Đặt lại tín hiệu dừng
    video_process = multiprocessing.Process(target=process_video, args=(stop_signal, count, count2))
    stop_signal_process = multiprocessing.Process(target=check_stop_signal, args=(stop_signal,))

    video_process.start()
    stop_signal_process.start()

    video_process.join()
    stop_signal_process.join()

    # Thêm dòng sau để lưu dữ liệu khi thoát khỏi process
    # print(f"Left Reps: {count.value}, Right Reps: {count2.value}")
    # save_to_database(count, count2)
    # print("✅ Data saved after stop signal")