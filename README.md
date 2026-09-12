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
<img width="1872" height="4160" alt="IMG_20260912_051304 jpg" src="https://github.com/user-attachments/assets/d87ef138-977a-4f6a-9ab4-ce51b9e28450" />



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
<img width="605" height="468" alt="arc" src="https://github.com/user-attachments/assets/4558bb98-3025-4d0a-b561-18279771cd16" />

Hardware Architecture & InterfacingThe circuit diagram illustrates the primary interface configuration for the Arduino Uno microcontroller:Display Interface: $16\times 2$ character LCD controlled over the I2C bus (A4/SDA and A5/SCL), minimizing required digital I/O pins.Visual & Audio Output: Digital pin D9 drives a red LED status indicator in series with a $1\text{ k}\Omega$ pull-down/current-limiting resistor (R1). Pin D10 powers an audible buzzer/transducer connected to common ground.Power Distribution: System components operate off a unified $+5\text{V}$ supply and shared ground line (U1_GND).


# Schematic & Circuit
<img width="671" height="454" alt="schm" src="https://github.com/user-attachments/assets/16c994e5-00cf-49e5-b889-0db95b462692" />

Circuit schematic of the Smart Classroom Drowsiness Detection System. The Arduino UNO serves as the main controller and interfaces with a 16×2 I2C LCD for displaying classroom status, a red LED with a 1 kΩ current-limiting resistor for visual alerts, and a buzzer for audible warnings. The LCD communicates with the Arduino through the I2C SDA and SCL lines, while all components share a common 5V power supply and ground. The circuit provides visual and audible alerts when the detected classroom drowsiness level exceeds the configured threshold.
*Add caption explaining connections*



# Build Photos
<img width="1872" height="4160" alt="IMG_20260912_065055 jpg" src="https://github.com/user-attachments/assets/8ffc23c7-4019-44d8-bfc4-36b6cc7673aa" />
Arduino UNO: The main controller of the hardware system. It receives the classroom status from the Python program through serial communication and controls the LCD, LED, and buzzer according to the detected drowsiness level.
16×2 I2C LCD: Displays the current classroom condition, such as “CLASS STATUS NORMAL”, “DROWSINESS ALERT!”, or “CLASS SUSPENDED!”. The I2C interface allows the LCD to communicate with the Arduino using fewer pins.
Red LED: Acts as a visual warning indicator. It turns ON when the system detects a high level of classroom drowsiness or an alert condition.
1 kΩ Resistor: Connected in series with the red LED to limit the current flowing through it and protect the LED from excessive current.
Buzzer: Provides an audible warning when drowsiness crosses the defined threshold, helping to immediately attract attention in the classroom.
Push Button: Can be used as a manual input/control component for the hardware system, depending on the programmed functionality.
Breadboard: Provides a convenient platform for assembling and testing the circuit without soldering.
Jumper Wires: Used to establish electrical connections between the Arduino, LCD, LED, buzzer, resistor, and power/ground rails.
USB Cable: Connects the Arduino UNO to the computer, providing power and enabling serial communication between the Python drowsiness-detection program and the Arduino.





### Project Demo
Working Demonstration:
The system uses a webcam to continuously monitor the user's facial behavior. The detection software analyzes facial characteristics such as eye/blink and drowsiness-related activity and classifies the current state as normal or drowsy. The classification result is communicated to an Arduino UNO, which controls a 16×2 LCD, LED, and buzzer. During normal operation, the LCD displays “CLASS STATUS – NORMAL”. When drowsiness is detected, the LCD changes to “DROWSINESS ALERT!” and the hardware alert indicators are activated. Once the user's condition returns to normal, the system automatically returns to the normal state.


---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



