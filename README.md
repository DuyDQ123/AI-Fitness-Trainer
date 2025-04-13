# AI Fitness Trainer

An AI-powered fitness training application that counts exercise repetitions using computer vision.

## Features

- Real-time pose detection
- Bicep curl counter for both arms
- Deadlift counter
- Progress visualization
- Web interface for exercise selection

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Flask
- NumPy

## Setup

1. Clone the repository
```bash
git clone https://github.com/DuyDQ123/AI-Fitness-Trainer.git
cd AI-Fitness-Trainer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python ai-fitness-trainer/src/server.py
```

## Usage

1. Open `http://localhost:5000` in your browser
2. Select an exercise (Bicep Curls or Deadlift)
3. Position yourself in front of the camera
4. Press 'q' to quit the exercise window