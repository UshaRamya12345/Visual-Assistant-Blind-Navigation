Title:- AI-Powered Real-Time Assistive Vision System for the Visually Impaired

This project is an Edge-AI based assistive technology designed to provide real-time situational awareness for visually impaired individuals. By leveraging Computer Vision and Deep Learning, the system identifies obstacles and estimates their proximity, delivering instant audible feedback through Bluetooth earbuds.

 Key Features
Real-Time Object Detection: Powered by YOLOv8 Nano for high-speed detection of people, vehicles, and household objects.
Software-Based Distance Estimation: Uses Monocular Depth Estimation (Triangle Similarity) to classify object proximity as 'Very Close', 'Near', or 'Far' without extra sensors.
Asynchronous Voice Alerts: Implemented Multithreading to ensure that voice feedback does not cause frame-lag in the live camera feed.
Offline Capability: Designed to run entirely on-device (Edge Computing), ensuring user privacy and functionality without an internet connection.

 Technical Stack
Language: Python 3.x
AI Model: YOLOv8 (Ultralytics)
Vision Library: OpenCV
Audio Engine: Pyttsx3 (Offline TTS)
Concurrency: Python Threading

  System Architecture
Input: Real-time video stream from a mobile/laptop camera.
Processing: YOLOv8 identifies objects and calculates the Bounding Box Width.
Logic: Distance is estimated based on the pixel width relative to the focal length.
Output: Processed alerts are sent to the Text-to-Speech (TTS) engine and played via Bluetooth earbuds.

  How to Run
Install Requirements:
pip install ultralytics opencv-python pyttsx3
Run the Script:
python vision.py

 Engineering Significance:-
As an Electronics & Communication Engineering (ECE) student, this project demonstrates my ability to integrate AI software with portable hardware constraints. It focuses on System Optimization, Resource Management, and Human-Computer Interaction (HCI).
Developed by: Addepalli Usha Ramya
Institution: Usha Rama College of Engineering and Technology

