AI Fitness Trainer
<div align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+"/> <img src="https://img.shields.io/badge/OpenCV-4.5+-green.svg" alt="OpenCV 4.5+"/> <img src="https://img.shields.io/badge/MediaPipe-0.8+-red.svg" alt="MediaPipe 0.8+"/> <img src="https://img.shields.io/badge/Flask-2.0+-orange.svg" alt="Flask 2.0+"/> <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/> </div> <p align="center"> <b>AI Fitness Trainer - Automatically track and analyze your exercises</b> </p>
📋 Table of Contents
Introduction
Features
Demo
System Requirements
Installation
Usage
System Architecture
Technologies Used
Project Structure
Contributing
License
🎯 Introduction
AI Fitness Trainer is an intelligent application that uses computer vision and machine learning to track, analyze, and count exercise repetitions. The system detects body postures and movements in real-time, providing feedback on exercise form and keeping track of workout progress. Whether you're doing bicep curls or deadlifts, this application helps ensure proper technique and consistent tracking.

✨ Features
Real-time pose detection: Uses MediaPipe to accurately track body movements
Automatic rep counting: Tracks and counts repetitions for each side (left/right)
Form analysis: Measures joint angles to ensure correct exercise form
Visual feedback: Progress bars and statistics displayed directly on video
Exercise history: View and track your workout progress over time
Database integration: Automatically saves workout results to a MySQL database
User-friendly interface: Easy-to-use web interface for controlling exercises
🎬 Demo
<img alt="AI Fitness Trainer Demo" src="https://example.com/demo.gif">
💻 System Requirements
Operating System: Windows, macOS, or Linux
Python: 3.8 or higher
Libraries:
OpenCV 4.5+
MediaPipe 0.8+
Flask 2.0+
MySQL Connector Python
NumPy
Hardware:
Webcam or camera
4GB RAM or higher recommended
Display with resolution of 1280x720 or higher
Database: MySQL/MariaDB (via XAMPP or standalone)
🚀 Installation
1. Clone the repository
git clone https://github.com/DuyDQ123/AI-Fitness-Trainer.git
cd AI-Fitness-Trainer
2. Create and activate a virtual environment (optional but recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install required libraries
pip install -r requirements.txt
4. Set up the database
CREATE TABLE bicep_curls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    left_count INT,
    right_count INT,
    total_count INT,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE deadlifts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    left_count INT,
    right_count INT,
    total_count INT,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
Install and start XAMPP (or any MySQL server)
Create a new database named ai_fitness_tracker
Run the following SQL commands to create necessary tables:
🎮 Usage
1. Start the server
python ai-fitness-trainer/src/server.py
2. Access the web interface
Open your browser and navigate to:

http://127.0.0.1:5000 if running locally
Or http://<your-ip-address>:5000 if accessing from another device
3. Using the application
Start an exercise: Click on "Start Bicep Curl Counter" or "Start Deadlift Counter"
Perform the exercise: Position yourself in front of the camera and perform the exercise
View progress: Watch your real-time progress on the video feed
Stop the exercise: Click "Stop Exercise" when finished
View history: Click "View Exercise History" to see your past workouts
4. Keyboard shortcuts
Press q to quit the exercise window
Press ESC to exit the application
🔄 System Architecture
The AI Fitness Trainer uses a multi-tier architecture:

Presentation Layer: Web interface built with HTML, CSS, and JavaScript
Application Layer: Flask server handling requests and business logic
Computer Vision Layer: OpenCV and MediaPipe for pose detection and analysis
Data Layer: MySQL database for storing workout data
The system uses a client-server model where:

The Flask server handles HTTP requests and serves the web interface
Computer vision processing happens in separate Python processes
Data is exchanged via JSON over HTTP requests
🛠️ Technologies Used
Backend: Python, Flask
Computer Vision: OpenCV, MediaPipe
Frontend: HTML, CSS, JavaScript
Database: MySQL/MariaDB
Process Management: Python subprocess module
Data Serialization: JSON
📁 Project Structure
ai-fitness-trainer/
├── assets/
│   └── videos/
│       ├── Curls.mp4
│       └── Deadlift.mp4
├── src/
│   ├── exercises/
│   │   ├── curl_count.py         # Bicep curl detection and counting
│   │   ├── deadlift_count.py     # Deadlift detection and counting
│   │   └── PoseModule.py         # Pose detection and analysis module
│   └── server.py                 # Flask server handling API requests
├── static/
│   └── style.css                 # CSS styles for the web interface
├── templates/
│   └── index.html                # Main web interface template
├── README.md                     # Project documentation
├── requirements.txt              # Required Python packages
└── .gitignore                    # Git ignore file
👥 Contributing
Contributions are welcome! Here's how you can contribute:

Fork the repository
Create your feature branch: git checkout -b feature/amazing-feature
Commit your changes: git commit -m 'Add some amazing feature'
Push to the branch: git push origin feature/amazing-feature
Open a Pull Request
Please make sure your code follows the existing style and includes appropriate tests.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center"> Developed with ❤️ by <a href="https://github.com/DuyDQ123">DuyDQ123</a> </p>
