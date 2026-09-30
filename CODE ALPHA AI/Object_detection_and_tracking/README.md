# Object Detection using YOLO

## 📌 Project Overview

This project implements a real-time object detection system using a pre-trained YOLO model. The system captures video from a webcam and detects objects in real time, drawing bounding boxes around them.

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

## 🚀 Features

* Real-time object detection using webcam
* Detection of multiple objects simultaneously
* Bounding boxes and labels displayed on detected objects
* Fast and efficient detection using a pre-trained YOLO model

## 🛠️ Technologies Used

* Python
* OpenCV
* Ultralytics YOLO

## ⚙️ How It Works

1. The program accesses the system webcam.
2. Each video frame is captured and passed to the YOLO model.
3. The model detects objects present in the frame.
4. Bounding boxes and labels are drawn around detected objects.
5. The processed frame is displayed in real time.

## 📂 Project Structure

CodeAlpha_ObjectDetection
│
├── object_detection.py
├── requirements.txt
└── README.md

## ▶️ How to Run the Project

1. Install the required libraries

pip install opencv-python ultralytics

2. Run the Python script

python object_detection.py

3. The webcam will open and start detecting objects in real time.

Press **Q** on the keyboard to stop the program.

## 📊 Example

The system can detect objects such as:

* Person
* Laptop
* Phone
* Bottle
* Chair

## 🎯 Internship Task

This project was developed for **Task 4: Object Detection and Tracking** as part of the CodeAlpha Artificial Intelligence Internship Program.

## 👨‍💻 Author

Jatin
Computer Science Engineering Student
Artificial Intelligence & Machine Learning
