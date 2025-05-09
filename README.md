# 💪 AI Fitness Trainer

An intelligent fitness training application that uses computer vision to track and count exercise repetitions in real-time. This application helps users monitor their workout progress by automatically counting repetitions for exercises such as bicep curls and deadlifts.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?logo=opencv&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?logo=mysql&logoColor=white)
![PHP](https://img.shields.io/badge/php-%23777BB4.svg?logo=php&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?logo=javascript&logoColor=%23F7DF1E)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0F9D58?logo=google&logoColor=white)
![XAMPP](https://img.shields.io/badge/XAMPP-FB7A24?logo=xampp&logoColor=white)

## ✨ Features

- 🔍 Real-time exercise detection and counting
- 🏋️ Support for multiple exercises (currently bicep curls and deadlifts)
- ⚖️ Separate tracking for left and right sides of the body
- 📊 Visual progress bars to monitor form
- 📈 Exercise history dashboard
- 💾 Database storage for tracking progress over time

## 🛠️ Technologies Used

- **Frontend**: 🌐 HTML, CSS, JavaScript
- **Backend**: 🐍 Flask (Python)
- **Computer Vision**: 👁️ OpenCV, MediaPipe
- **Database**: 🗄️ MySQL
- **Web Server**: 🖥️ Apache (XAMPP)

## 📥 Installation

### Prerequisites

- 🐍 Python 3.7 or higher
- 🗄️ XAMPP (for MySQL database and Apache server)
- 📂 Git

### Setup Instructions

1. **Clone the repository** 📋
   ```
   git clone https://github.com/DuyDQ123/AI-Fitness-Trainer.git
   cd AI-Fitness-Trainer
   ```

2. **Create a virtual environment** 🔮
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages** 📦
   ```
   pip install flask opencv-python mediapipe numpy mysql-connector-python psutil requests
   ```

4. **Set up the database** 🗃️
   - Start XAMPP and make sure MySQL service is running
   - Open phpMyAdmin (http://localhost/phpmyadmin)
   - Create a new database named `ai_fitness_tracker`
   - Create the following tables:

   ```sql
   CREATE TABLE bicep_curls (
       id INT AUTO_INCREMENT PRIMARY KEY,
       left_count INT NOT NULL,
       right_count INT NOT NULL,
       total_count INT NOT NULL,
       date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE deadlifts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       left_count INT NOT NULL,
       right_count INT NOT NULL,
       total_count INT NOT NULL,
       date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

## 📱 Usage

1. **Start the Flask server** 🚀
   ```
   cd ai-fitness-trainer
   python src/server.py
   ```

2. **Access the application** 🌐
   Open your web browser and go to `http://localhost:5000`

3. **Select an exercise** 🏋️‍♀️
   Click on either the "Bicep Curl" or "Deadlift" button to start tracking the exercise

4. **Stop the exercise** ✋
   Click the "Stop Exercise" button when you're finished with your set

5. **View your history** 📜
   Click on "View History" to see your previous workout statistics

## 📁 Project Structure

```
AI-FITNESS-TRAINER/
├── .htaccess                    # Apache rewrite rules
├── ai-fitness-trainer/
│   ├── assets/
│   │   └── videos/              # Exercise videos
│   ├── src/
│   │   ├── exercises/
│   │   │   ├── PoseModule.py    # MediaPipe pose detection module
│   │   │   ├── curl_count.py    # Bicep curl exercise tracker
│   │   │   └── deadlift_count.py # Deadlift exercise tracker
│   │   └── server.py            # Flask server
│   ├── static/
│   │   └── style.css            # Application styles
│   └── templates/
│       └── index.html           # Main application page
└── README.md                    # This file
```

## 🚀 Future Improvements

- ➕ Add more exercise types
- 🔐 Implement user accounts and authentication
- 📱 Create a mobile app version
- 📊 Add detailed analytics and visualization of progress
- 🤖 Implement AI-based form correction suggestions

## 📄 License

This project is licensed under the MIT License.
Project create by Duy

