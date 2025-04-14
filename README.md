# 🏋️‍♂️ AI Fitness Trainer

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/OpenCV-4.5+-green.svg" alt="OpenCV 4.5+"/>
  <img src="https://img.shields.io/badge/MediaPipe-0.8+-red.svg" alt="MediaPipe 0.8+"/>
  <img src="https://img.shields.io/badge/Flask-2.0+-orange.svg" alt="Flask 2.0+"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/>
</div>

<p align="center">
  <b>AI Fitness Trainer - Automatically track and analyze your exercises</b>
</p>

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [System Architecture](#-system-architecture)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Introduction

**AI Fitness Trainer** is an intelligent application that uses artificial intelligence to track, analyze, and count exercise repetitions. The project uses computer vision combined with deep learning to recognize user postures and movements, ensuring correct exercise technique and tracking workout progress.

## ✨ Features

- **Accurate posture recognition**: Uses MediaPipe to detect and track body joint points
- **Automatic rep counting**: Tracks and counts repetitions for each side (left/right)
- **Joint angle analysis**: Measures and analyzes joint angles during exercises
- **Visual display**: Progress bars and statistics displayed directly on the video
- **Data storage**: Automatically saves workout results to a database
- **User-friendly web interface**: Easy to start and stop exercises

## 💻 System Requirements

- Python 3.8+
- OpenCV 4.5+
- MediaPipe 0.8+
- Flask 2.0+
- MySQL/MariaDB 
- XAMPP (for database management)

## 🚀 Installation

### 1. Clone repository

```bash
git clone https://github.com/DuyDQ123/AI-Fitness-Trainer.git
cd AI-Fitness-Trainer
```

### 2. Install dependencies

```bash
pip install flask opencv-python mediapipe numpy requests
```

## 🛠️ Usage

### 1. Run server

```bash
python ai-fitness-trainer/src/server.py
```

### 2. Access interface

Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 3. Start exercise

- Click "Start" to begin the exercise.
- Click "Stop" to end the exercise and save data to the database.

## 🏗️ Project Structure

```
ai-fitness-trainer/ 
├── assets/ 
│   └── videos/ 
│       ├── Curls.mp4 
│       └── Deadlift.mp4 
├── src/ 
│   ├── exercises/ 
│   │   ├── curl_count.py 
│   │   ├── deadlift_count.py 
│   │   └── PoseModule.py 
│   ├── server.py 
│   └── templates/ 
│       └── index.html 
├── static/ 
│   └── style.css 
└── README.md
```

