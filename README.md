<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# Lecture Drowsiness Detection System 🎯


## Basic Details
### Team Name: PIXEL PUNKS


### Team Members
- Member 1: Neha Deepak - [College of Engineering Perumon ]
- Member 2: Krishnaveni M L- [College of Engineering Perumon]

### Project Description
A smart system that detects student drowsiness during lectures using OpenCV with real-time alerts.

### The Problem (that doesn't exist)
How can we stop students from accidentally completing their lecture by sleeping through it?

### The Solution (that nobody asked for)
Solving the greatest unsolved problem in engineering: keeping students awake for one more slide.

## Technical Details
### Technologies/Components Used
For Software:
- Python, ML
- OpenCV, Arduino IDE, MediaPipe, 
- OpenCV,Arduino IDE, MediaPipe, Numpy, LiquidCrystal I2C
- ArduinoIDE, VS CODE, Serial Monitor

For Hardware:
- Arduino UNO
- LCD 16x2 I2C
- Buzzer, LED, Push Button, Jumper wires & Breadboard

### Implementation
For Software:VS Code, Python3.12.10 , Arduino IDE
# Installation
python -m pip install --upgrade pip
python -m pip install opencv-python mediapipe numpy scikit-learn pyserialpython --version

# Run
python cam_tst.py, python drowsiness_prob.py

### Project Documentation
For Software:

# Screenshots (Add at least 3)
<img width="1872" height="4160" alt="IMG_20260912_065055 jpg" src="https://github.com/user-attachments/assets/90777e5b-f603-408d-b115-0e422da7dd7c" />


The image demonstrates the real-time execution of a Smart Classroom Drowsiness Detection System using facial landmark mesh tracking, 
eye aspect ratio (EAR) analysis, and Arduino integration for alert triggers.
**Facial Mesh:** MediaPipe/TensorFlow Lite facial landmark mapping with individual EAR values.
**Classroom Metrics:** Tracks active student count, class drowsiness percentage, and state counters (Sleeping, Drowsy, Yawning).
**Hardware Integration:** Real-time alert triggering via Arduino connection on `COM6`.

<img width="4160" height="1872" alt="IMG_20260912_064703 jpg" src="https://github.com/user-attachments/assets/ddf469f6-2128-4cbe-aa2d-6e818303e785" />

![Hardware Setup - Class Status Display]
*Hardware integration setup featuring an Arduino Uno connected to a 16x2 LCD screen displaying "CLASS STATUS NORMAL", alongside a breadboard wired with indicator components and a buzzer.*
Low Drowsiness Threshold: The Python vision pipeline (drowsy_prob.py) is calculating an overall classroom drowsiness percentage below the trigger threshold (in the previous screen, class drowsiness was at 0%).

![Uploading IMG_20260912_064715.jpg.jpeg…]()

The message "DROWSINESS ALERT!" on the LCD screen indicates that the system has detected fatigue, sleepiness, or distraction exceeding safe limits in the classroom environment.
This state corresponds to the warning triggers shown in your Python console log (such as Arduino command: ALARM), activating physical safety measures:
Warning Trigger: The vision script has calculated that drowsiness or sleeping metrics have breached the threshold limit.
Hardware Response: The Arduino receives the alert signal over serial communication, driving the 1602 LCD to display the warning message alongside activating physical indicators like the buzzer or warning LEDs to grab attention.



# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
<img src="C:\Users\KRISHNA_VENI\OneDrive\Documents\IMG_20260912_065055.jpg.jpeg">
Components shown 

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



