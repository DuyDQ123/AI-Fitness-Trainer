# AI Fitness Trainer

AI Fitness Trainer là một ứng dụng sử dụng OpenCV và Mediapipe để theo dõi và đếm số lần thực hiện các bài tập thể dục như bicep curls và deadlifts.

## Cách sử dụng

1. **Cài đặt môi trường**:
   - Cài đặt các thư viện cần thiết:
     ```bash
     pip install flask opencv-python mediapipe numpy requests
     ```

2. **Chạy server**:
   - Chạy Flask server:
     ```bash
     python ai-fitness-trainer/src/server.py
     ```

3. **Truy cập giao diện**:
   - Mở trình duyệt và truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. **Bắt đầu bài tập**:
   - Nhấn nút "Start" để bắt đầu bài tập.
   - Nhấn nút "Stop" để dừng bài tập và lưu dữ liệu vào database.

## Cấu trúc dự án

GitHub Copilot
Dưới đây là các bước để lưu lại thay đổi, đẩy lên GitHub và thêm file README.md:

1. Tạo file README.md
Tạo file README.md trong thư mục gốc của dự án (AI-FITNESS-TRAINER) và thêm nội dung mô tả dự án:

ai-fitness-trainer/ 
├── assets/ 
│ └── videos/ 
│ ├── Curls.mp4 
│ └── Deadlift.mp4 
├── src/ 
│ ├── exercises/ 
│ │ ├── curl_count.py 
│ │ ├── deadlift_count.py 
│ │ └── PoseModule.py 
│ ├── server.py 
│ └── templates/ 
│   └── index.html 
├── static/ 
│   └── style.css 
└── README.md

