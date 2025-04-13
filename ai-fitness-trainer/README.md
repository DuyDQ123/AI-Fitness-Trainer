# AI Fitness Trainer

AI Fitness Trainer is a web application designed to help users track their exercise performance through video analysis. The application utilizes computer vision techniques to count repetitions of specific exercises, such as curls and deadlifts, by analyzing video input.

## Project Structure

```
ai-fitness-trainer
├── src
│   ├── modules
│   │   └── PoseModule.py
│   ├── exercises
│   │   ├── curl_count.py
│   │   └── deadlift_count.py
│   └── server.py
├── static
│   └── style.css
├── templates
│   └── index.html
├── assets
│   └── videos
│       ├── curls.mp4
│       └── deadlift.mp4
├── requirements.txt
└── README.md
```

## Features

- **Pose Detection**: Utilizes OpenCV and MediaPipe to detect human poses in real-time.
- **Exercise Counting**: Automatically counts repetitions of curls and deadlifts based on arm angles.
- **Web Interface**: A simple web interface built with Flask to launch exercises and display results.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-fitness-trainer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```
   python src/server.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the buttons on the homepage to launch the curl or deadlift counting exercises.

## Requirements

- Python 3.x
- Flask
- OpenCV
- MediaPipe

## License

This project is licensed under the MIT License. See the LICENSE file for more details.